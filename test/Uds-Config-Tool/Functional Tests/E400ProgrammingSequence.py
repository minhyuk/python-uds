from uds import createUdsConnection
from struct import pack, unpack
import hashlib
from time import sleep, time


class ihexData(object):

    # Constructor (__init__) method for initializing an instance with default attributes
    # Args:
    #    self: The instance of the class.
    # 1. Initializes the '__startAddress' attribute to 0, representing the starting address.
    # 2. Initializes the '__size' attribute to 0, representing the size of the data.
    # 3. Initializes the '__data' attribute to an empty list, representing the data storage.
    def __init__(self):
    
            self.__startAddress = 0
            self.__size = 0
            self.__data = []

    @property
    # Method to get the starting address
    # Args:
    #    self: The instance of the class.
    # Returns:
    #    The value of the '__startAddress' attribute.
    def startAddress(self):
            return self.__startAddress

    @startAddress.setter
    # Method to set the starting address
    # Args:
    #    self: The instance of the class.
    #    value: The value to set for the '__startAddress' attribute.
    # Sets the '__startAddress' attribute to the provided value.
    def startAddress(self, value):
            self.__startAddress = value

    @property
    # Method to get the data
    # Args:
    #    self: The instance of the class.
    # Returns:
    #    The value of the '__data' attribute.
    def data(self):
            return self.__data

    @data.setter
    # Method to set the data
    # Args:
    #    self: The instance of the class.
    #    value: The value to set for the '__data' attribute.
    # Sets the '__data' attribute to the provided value.
    def data(self, value):
            self.__data = value

    # Method to append data to the existing data
    # Args:
    #    self: The instance of the class.
    #    value: The value to be appended to the '__data' attribute.
    # Appends the provided value to the '__data' attribute by concatenating it.
    def addData(self, value):
            self.__data += value

    # Method to get data from a specific address with a given size
    # Args:
    #    self: The instance of the class.
    #    address: The starting address from which to get the data.
    #    size: The amount of data to retrieve.
    # Raises:
    #    NotImplementedError: Indicates that this method is not yet implemented.
    def getDataFromAddress(self, address, size):
            raise NotImplementedError("getDataFromAddress Not yet implemented")


class ihexFile(object):

    # Constructor (__init__) method for initializing an instance with hexadecimal file data
    # Args:
    #    self: The instance of the class.
    #    filename: The name of the hex file to be processed (optional).
    #    padding: The padding byte value to use for gaps in data (default: 0xFF).
    #    continuousBlocking: Boolean flag to indicate whether continuous blocking should be applied (default: True).
    # 1. Opens the hex file for reading.
    # 2. Initializes an empty list '__blocks' to store the data blocks.
    # 3. Initializes variables for end-of-file flag 'eof_flag', line counter 'linecount', current and next address,
    #    current block 'currentBlock', and base address 'baseAddress'.
    # 4. Processes each line of the hex file in a loop until end-of-file is reached:
    #    a. Reads a line from the hex file and checks if it starts with ":".
    #       - Raises an exception if the line format is unexpected.
    #    b. Converts the line (excluding the initial ":") from hex to bytes.
    #    c. Extracts the main data fields from the byte array: data length, address, record type, data, and checksum.
    #    d. Calculates the checksum and verifies it matches the one from the file.
    #       - Raises an exception if the checksums do not match.
    #    e. Processes the line based on the record type:
    #       - Record type 0x00 (Data Record): Adds data to the current block, handling any gaps with padding if necessary.
    #       - Record type 0x01 (End Of File Record): Sets end-of-file flag and appends the current block to '__blocks'.
    #       - Record type 0x02 (Extended Segment Address): Raises "Not implemented" exception.
    #       - Record type 0x03 (Start Segment Address): Raises "Not implemented" exception.
    #       - Record type 0x04 (Extended Linear Address): Initializes a new block and sets the base address.
    #       - Record type 0x05 (Start Linear Address): Raises "Not implemented" exception.
    # 5. Increments the line counter for each processed line.
    # Note: The code includes commented-out print statements for debugging purposes.
    def __init__(self, filename=None, padding=0xFF, continuousBlocking=True):
    
            hexFile = open(filename, 'r')
    
            self.__blocks = []
    
            eof_flag = False
            linecount = 1
    
            currentAddress = None
            nextAddress = None
    
            currentBlock = None
            baseAddress = 0
    
            while not eof_flag:
    
                line = hexFile.readline()
    
                if line[0] != ":":
                    raise Exception("Unexpected line on line {0}".format(linecount))
    
                lineArray = bytes.fromhex(line[1:])
    
                # get the main data
                index = 0
                dataLength = lineArray[index]
                index += 1
                address = (lineArray[index] << 8) | (lineArray[index+1])
                index += 2
                recordType = lineArray[index]
                index += 1
                data = lineArray[index: index+dataLength]
                index += dataLength
                checksum = lineArray[index]
    
                calculatedChecksum = 0
    
                for i in range(len(lineArray)-1):
                    calculatedChecksum = (calculatedChecksum + lineArray[i]) % 256
    
                calculatedChecksum = ( ~calculatedChecksum + 1 ) %256
    
                if calculatedChecksum != checksum:
                    raise Exception("Checksum on line {0} does not match. Actual: {1}, Calculated: {2}".format(linecount,
                                                                                                               checksum,
                                                                                                               calculatedChecksum))
    
                # print("Length: {0:#x}, Address: {1:#x}, recordType: {2:#x}, data: {3}, checksum: {4:#x}, calculatedChecksum: {5:#x}".format(dataLength,
                #                                                                                                                             address,
                #                                                                                                                             recordType,
                #                                                                                                                             data,
                #                                                                                                                             checksum,
                #                                                                                                                             calculatedChecksum))
    
    
    
                if recordType == 0x00:
                    if currentAddress is None:
                        currentBlock.startAddress = baseAddress + address
    
                    if nextAddress is not None:
                        if address != nextAddress:
                            if continuousBlocking:
                                paddingBlock = []
                                [paddingBlock.append(padding) for i in range(0, address-nextAddress)]
                                currentBlock.addData(paddingBlock)
                            else:
                                # print("new block")
                                pass
                    currentBlock.addData(data)
                    currentAddress = address
                    nextAddress = address + dataLength
    
    
    
                elif recordType == 0x01:
                    eof_flag = True
                    if currentBlock is not None:
                        self.__blocks.append(currentBlock)
                elif recordType == 0x02:
                    raise NotImplemented("Not implemented extended segment address")
                elif recordType == 0x03:
                    raise NotImplemented("Start segment address not implemented")
                elif recordType == 0x04:
                    # print("New block")
                    if currentBlock is None:
                        currentBlock = ihexData()
                        baseAddress = (address << 16)
                    else:
                        self.__blocks.append(currentBlock)
    
                elif recordType == 0x05:
                    raise NotImplemented("Start linear address not implemented")
    
                linecount += 1
    
                pass

    # Method to get the list of data blocks
    # Args:
    #    self: The instance of the class.
    # Returns:
    #    The value of the '__blocks' attribute, which is a list of data blocks.
    def getBlocks(self):
            return self.__blocks


# Function to calculate a key from a seed and an ECU key using MD5 hashing
# Args:
#    seed: A list of integers representing the seed value.
#    ecuKey: A list of integers representing the ECU key (not used in the function).
# Returns:
#    A list of integers representing the calculated key.
# 1. Defines a device secret, 'deviceSecret', as a list of integers.
# 2. Concatenates 'deviceSecret', 'seed', and 'deviceSecret' again to form the MD5 input, 'md5Input'.
# 3. Packs 'md5Input' into a binary string 'c' using the 'pack' function from the struct module.
# 4. Calculates the MD5 hash of 'c' using 'hashlib.md5' and gets the binary digest.
# 5. Unpacks the MD5 digest into a tuple of integers 'dUnpack' using the 'unpack' function from the struct module.
# 6. Converts the tuple 'dUnpack' into a list 'sendList'.
# 7. Returns 'sendList', representing the calculated key derived from the seed and device secret.
def calculateKeyFromSeed(seed, ecuKey):

    deviceSecret = [0x46, 0x45, 0x44, 0x43, 0x42, 0x41, 0x39, 0x38, 0x37, 0x36, 0x35, 0x34, 0x33, 0x32, 0x31, 0x30]

    md5Input = deviceSecret + seed + deviceSecret
    c = pack('%sB' % len(md5Input), *md5Input)
    d = hashlib.md5(c).digest()
    dUnpack = unpack('%sB' % 16, d)
    sendList = [val for val in dUnpack]

    return sendList


if __name__ == "__main__":

    #secondaryBootloaderContainer = chunkIhexFile("TGT-ASSY-1383_v2.1.0_sbl.hex")
    #print(secondaryBootloaderContainer)
    secondaryBootloader = ihexFile("TGT-ASSY-1383_v2.1.0_sbl.hex")
    blocks = secondaryBootloader.getBlocks()
    blockData = blocks[0].data
    smallerChunks = []
    chunk = []
    count = 0
    for i in range(0, len(blockData)):
        chunk.append(blockData[i])
        count += 1
        if count == 1280:
            smallerChunks.append(chunk)
            chunk = []
            count = 0

    if len(chunk) != 0:
        smallerChunks.append(chunk)

    e400 = createUdsConnection("Bootloader.odx", "Bootloader", reqId=0x600, resId=0x650, interface="peak")

    a = e400.readDataByIdentifier("ECU Serial Number")
    print("Serial Number: {0}".format(a["ECU Serial Number"]))

    a = e400.readDataByIdentifier("PBL Part Number")
    print("PBL Part Number: {0}".format(a["PBL Part Number"]))

    a = e400.readDataByIdentifier("PBL Version Number")
    print("PBL Version Number: {0}".format(a["PBL Version Number"]))

    a = e400.diagnosticSessionControl("Programming Session")
    print("In Programming Session")

    a = e400.securityAccess("Programming Request")
    print("Security Key: {0}".format(a))

    b = calculateKeyFromSeed(a, [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
    print("Calculated Key: {0}".format(b))

    a = e400.securityAccess("Programming Key", b)
    print("Security Access Granted")

    print("Setting up transfer of Secondary Bootloader")
    a = e400.requestDownload([0], [0x40, 0x03, 0xe0, 0x00], [0x00, 0x00, 0x0e, 0x56])
    #print(a)

    print("Transferring Secondary Bootloader")
    for i in range(len(smallerChunks)):
        a = e400.transferData(i+1, smallerChunks[i])

    print("Finished Transfer")
    a = e400.transferExit()

    print("Jumping to Secondary Bootloader")
    a = e400.routineControl("Start Secondary Bootloader", 1, [0x4003e000])
    #print(a)

    print("Erasing Memory")
    a = e400.routineControl("Erase Memory", 1, [("memoryAddress",[0x00080000]), ("memorySize",[0x000162e4])])
    #print(a)

    working = True
    while working:

        a = e400.routineControl("Erase Memory", 3)
        #print(a)
        if(a['Erase Memory Status']) == [0x30]:
            print("Erased memory")
            working = False
        elif(a['Erase Memory Status'] == [0x31]):
            print("ABORTED")
            raise Exception("Erase memory unsuccessful")
        sleep(0.001)

    application = ihexFile("e400_uds_test_app_e400.ihex")
    blocks = application.getBlocks()
    blockData = blocks[0].data
    smallerChunks = []
    chunk = []
    count = 0
    for i in range(0, len(blockData)):
        chunk.append(blockData[i])
        count += 1
        if count == 1280:
            smallerChunks.append(chunk)
            chunk = []
            count = 0

    if len(chunk) != 0:
        smallerChunks.append(chunk)

    print("Setting up transfer for Application")
    a = e400.requestDownload([0], [0x00, 0x08, 0x00, 0x00], [0x00, 0x01, 0x62, 0xe4])

    print("Transferring Application")
    for i in range(0, len(smallerChunks)):

        a = e400.transferData(i+1, smallerChunks[i])

    print("Transfer Exit")
    a = e400.transferExit()

    a = e400.routineControl("Check Valid Application", 0x01)

    working = True
    while working:
        # a = e400.send([0x31, 0x03, 0x03, 0x04])
        # print(a)
        # if a[4] == 0x30:
        #     working = False
        #     print("Success")
        # elif a[4] == 0x31:
        #     working = False
        #     print("Aborted")
        a = e400.routineControl("Check Valid Application", 0x03)

        routineStatus = a["Valid Application Status"][0]
        applicationPresent = a["Valid Application Present"][0]

        if routineStatus == 0x30:
            working = False
            print("Routine Finished")

            if applicationPresent == 0x01:
                print("Application Invalid")
            elif applicationPresent == 0x02:
                print("Application Valid")
        elif routineStatus == 0x31:
            working = False
            print("Aborted")
        elif routineStatus == 0x32:
            #print("Working")
            pass

        sleep(0.01)


    e400.ecuReset("Hard Reset", suppressResponse=True)



