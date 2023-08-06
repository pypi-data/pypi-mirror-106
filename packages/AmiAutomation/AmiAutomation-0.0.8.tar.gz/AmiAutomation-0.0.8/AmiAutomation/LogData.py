import zlib, struct, time, os
import datetime as dt
import pandas as pd
import numpy as np
import xml.etree.ElementTree as ET

class Bag:
    Key = str()
    _frame = None

class FrameHeader:
    _version = 0;
    _flags = 0;
    _rawSize = 0;
    _tag = None; 
    
class FrameBase:
    _header = FrameHeader()

class LogData:
    _fileName = str()
    _data = None
    _mainTrendsNames = None
    _mainDivisors = None
    dataFrame = pd.DataFrame()
    properties = None

def _getDatatype (dataTypeEnum):
    thisdict = {
    3: ("?",1), #bool
    4: ("c",1), #char
    5: ("b",1), #signed char (SByte)
    6: ("B",1), #unsigned char (Byte)
	7: ("h",2), #short (Int16)
	8: ("H",4), #unsigned char (UInt16)
	9: ("i",4), #int (Int32)
	10: ("I",4), #unsigned int (UInt32)
	11: ("q",8), #long long (Int64)
	12: ("Q",8), #unsigned long long (UInt64)
	13: ("f",4), #float (Single)
	14: ("d",8), #double (Double)
	15: ("d",16), #(Decimal) May not work
    16: ("D",8), #(DateTime) May not work
    18: ("s",1), #char[] (String) 
	19: ("Q",16), #(Guid) May not work
	20: ("p",1), #char [] (Binary)
    }
    return thisdict[dataTypeEnum]

def _IntModeDivisor(mode):
    intMode = mode % 100
    switcher = {
        0: 100, #impedance
        1: 100, #current
        2: 100 #resistance
    }
    if intMode in switcher:
        return switcher[intMode]
    else:
        return 1
    
def _ExtModeDivisor(mode):
    extMode =mode / 100 
    switcher = {
        1: 100, #current
        2: 10, #voltage
        3: 10000, #PF
        4: 100, #MW
        5: 10 #RWI
    }
    if extMode in switcher:
        return switcher[extMode]
    else:
        return 1

def _RegModeDivisor(mode):
    div = _ExtModeDivisor(mode)
    if div ==1:
        return _IntModeDivisor(mode)
    else:
        return div

def _getDivisors(divList, RegModeList):
    divColumnReturn = []
    for i,div in enumerate(divList):
        regulationMode = RegModeList[i]
        if div<0:
            if (div == -1): #Int. mode
                divColumnReturn.append(_IntModeDivisor(regulationMode))
            elif (div == -2): #Ext. mode
                divColumnReturn.append(_ExtModeDivisor(regulationMode))
            elif (div== -3): #Int. or Ext. mode
                divColumnReturn.append(_RegModeDivisor(regulationMode))
        else:
            divColumnReturn.append(div)
    return divColumnReturn

def _readString(bytesArray,bytePos):
    #https://docs.microsoft.com/en-us/openspecs/sharepoint_protocols/ms-spptc/1eeaf7cc-f60b-4144-aa12-4eb9f6e748d1?redirectedfrom=MSDN
    pos = bytePos
    index = 0
    strLen = 0
    while True:
        length = bytesArray[pos]
        strLen |= (length & 0x7F) << (7*index)
        index += 1
        pos += 1
        if length & 0x80 == 0: #Number complete
            break
               
    value = bytesArray[pos:pos+strLen].decode()
    pos += strLen
    
    return value, pos

def _processVersionN(version, Properties, bytesArray, innerBufferSize):
    """
    Unpacks binary file according to its properties

    Parameters
    ----------
    version : int
        binary version  
        
    Properties : dict
        Dictionary containing at least 'StartTime', 'Increment' & 'Definition' properties
    
    bytesArray : byte[] 
        array containing the file to process  
        
    innerBufferSize : int
        size of samples data
        
    Returns
    -------
    LogData
        Structure containing most file data

    """
    # utcStartTime = Properties['StartTime']
    # incrementMillisecs = Properties['Increment']
    # incrementTicks = incrementMillisecs * 10000.0
    # definition = Properties['Definition']
    
    
    root = ET.fromstring(Properties["Definition"])
    
    if version == 3:
        nodes = root.findall(".//object[@logged='y']/field")
    elif version == 2:
        nodes = root.findall(".//object[@logged='y']/field")
    elif version == 1:
        nodes = root.findall("//object/field")
    else:
        print("Unknown packet version: ", version)
        
    varNames = []
    trendsNames = []
    divisors = []
    fieldTypes = []
    
    listBitMapElement = []
    d_c = []
    
    for index, field in enumerate(nodes):
        fieldType = field.attrib['type']
        fieldTypes.append(fieldType if fieldType == "s" else None)
        if field.attrib['type'] == "s":
                        
            varName = field.text.strip()
            varNames.append(varName)
            if varName != "":
                trendsNames.append(varName)
                option = field.attrib['div']
                try:
                    divisor = float(option)
                    if divisor == 0:
                        divisor = 1
                except:
                    if option == 'I':
                        divisor = -1
                    elif option == "E":
                        divisor = -2
                    elif option == "I|E":
                        divisor = -3
                divisors.append(divisor)
                
        else:
            listBitMapElement.append(index)
            bit = 0
            for bits in field:
                bit += 1
                varNames.append(bits.text)
                if varNames[-1]:
                    trendsNames.append(varNames[-1])
                    divisors.append(1)
    
            d_c.append(bit)

    listOfSamples = []
    
    #Obtain stream data from InnerBuffer
    appendListOfSamples = listOfSamples.append
    dataArray = np.ndarray(shape=(int((innerBufferSize/2)/len(fieldTypes)),len(fieldTypes)), dtype='h', buffer=bytesArray)
    
    bitMapCount = 0    
    for i in range(len(dataArray[0,:])):
        if (bitMapCount < len(listBitMapElement)):
            if listBitMapElement[bitMapCount] == i:
                for bit in range(d_c[bitMapCount]):
                    series = dataArray[:,i] >> bit & 1
                    appendListOfSamples(series)
                bitMapCount+=1
                continue
        appendListOfSamples(dataArray[:,i])
        
    arraySamples = np.transpose(listOfSamples, axes=None)
    
    logData = LogData()
    logData._data = arraySamples
    logData._mainTrendsNames = trendsNames
    logData._mainDivisors = divisors
    logData.properties = Properties
    
    return logData

def binStreamToDF(file):
    """
    Unpacks binary file stream into LogData
    
    Parameters
    ----------
    file : stream
        stream of binary file
        

    Returns
    -------
    LogData
        Structure containing most file data

    """
    #header
    TAGS = file.read(4)
    if TAGS != b'TAGS':
        print("Error with Tags header")
    versionHeader = file.read(1)
    if versionHeader == b'\xFF':
        print("Corrupt header, version can never reach 255")
    flags = file.read(1)
    if flags.hex() == '40':
        compressed = True
    else:
        compressed = False
    
    #properties    
    bytePos = 0    
    if compressed:
        bytesArray = zlib.decompress(file.read())
    else:
        bytesArray = file.read()
        
    version = bytesArray[bytePos]
    
    if version != 0:
        print ("Error unserializing properties, version " + version + " is not supported")
        
    bytePos+=1
    itemsCount = bytesArray[bytePos:bytePos+4]
    intItemsCount = int.from_bytes(itemsCount, "little")
    bytePos+=4
    
    Properties = dict()
    
    for items in range(intItemsCount): 
        
        strLen = bytesArray[bytePos]
        bytePos += 1
        
        key = bytesArray[bytePos:bytePos+strLen].decode()
        bytePos += strLen
        
        dataTypeEnum = bytesArray[bytePos]
        bytePos += 1
        
        dataType, size = _getDatatype(dataTypeEnum)
        if dataType == "s":#string
            value, bytePos = _readString(bytesArray, bytePos)
        elif dataType == "D":#Datetime
            value, bytePos = _readString(bytesArray, bytePos)
            value = value.rstrip('0') #Remove trailing 0s
            value = dt.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
        else:    
            value = struct.unpack(dataType, bytesArray[bytePos:bytePos+size])[0]
            bytePos += size
    
        Properties[key] = value
    
    if 'Increment' in Properties:
        Properties['Increment'] = dt.timedelta(milliseconds = Properties['Increment'] )
    
    count = struct.unpack("h", bytesArray[bytePos:bytePos+2])[0]
    bytePos += 2
    
    _hash = dict()
    _frames = []
    
    for element in range(count):
        
        bag = Bag()
        
        contains = struct.unpack("?", bytesArray[bytePos:bytePos+1])[0]
        bytePos += 1
        
        if contains:
            strLen = bytesArray[bytePos]
            bytePos += 1
            bag.Key= bytesArray[bytePos:bytePos+strLen].decode()
            bytePos += strLen
            _hash[bag.Key] = bag
            
        frameHeader = FrameHeader()
        frameHeader._tag = bytesArray[bytePos:bytePos+4]
        bytePos += 4
        frameHeader._version = bytesArray[bytePos]
        bytePos += 1
        if frameHeader._version == b'\xFF':
            print("Corrupt header, invalid version.")
        frameHeader._flags = bytesArray[bytePos] & 0xF0 #Only read what I understand
        bytePos += 1
        frameHeader._rawSize = struct.unpack("i", bytesArray[bytePos:bytePos+4])[0]
        bytePos += 4
        if frameHeader._rawSize == 0:
            print("Corrupt header, tag size can't be zero.")
            
        frameBase = FrameBase()
        frameBase._header = frameHeader
        
        if frameBase._header._tag != b"BLOB":
            print("Just BLOB validated for now")
            
        #Inner Properties 
        innerVersion = bytesArray[bytePos]
        bytePos += 1    
        if innerVersion != 0:
            print ("Error unserializing properties, version " + innerVersion + " is not supported")
            
        innerItemsCount = struct.unpack('i', bytesArray[bytePos:bytePos+4])[0]
        bytePos+=4
        if innerItemsCount!=0: #itemsCount should be zero
            print("Error")
        innerLength = struct.unpack('i', bytesArray[bytePos:bytePos+4])[0]
        bytePos+=4
    
        bag._frame = frameBase
        _frames.append(bag)   
        
    if 'Version' in Properties:
        if Properties['Version'] == 1:
            logData = _processVersionN(1, Properties, bytesArray[bytePos:bytePos+innerLength], innerLength)
        elif Properties['Version'] == 2:
            logData = _processVersionN(2, Properties, bytesArray[bytePos:bytePos+innerLength], innerLength)
        elif Properties['Version'] == 3:
            logData = _processVersionN(3, Properties, bytesArray[bytePos:bytePos+innerLength], innerLength)
        else:
            print("Unknown version")
    
    dFrame = pd.DataFrame(logData._data, columns=logData._mainTrendsNames )
    
    step = np.arange(start = 0, stop=len(logData._data), step=1, dtype=np.int16)
    listOfTimeStamps = logData.properties['StartTime']+logData.properties['Increment']*pd.Series(step)
    dFrame["Timestamp"] = listOfTimeStamps
    dFrame.set_index("Timestamp",inplace=True)
        
    try:
        divColumns = _getDivisors(logData._mainDivisors,dFrame["RegStatus.RegulationMode"] )
    except:
        divColumns = logData._mainDivisors
        
    logData.dataFrame = dFrame.div(divColumns, axis='columns')
    del logData._data
    
    return logData

def binFileToDF(path):
    """
    Unpacks binary file into LogData
    
    Parameters
    ----------
    path : str
        Complete file path
        
    Returns
    -------
    LogData
        Structure containing most file data

    """
    
    file = open(path, "rb")
    
    logData = binStreamToDF(file)
    logData._fileName = os.path.basename(path)
    
    file.close()
    return logData