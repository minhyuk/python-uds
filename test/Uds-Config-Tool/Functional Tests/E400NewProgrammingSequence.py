from uds import createUdsConnection
from uds import ihexFile
from struct import pack, unpack
import hashlib
from time import sleep, time
from uds import DecodeFunctions


# Function to calculate a key from a seed and an ECU key using MD5 hashing
# Args:
#    seed: A list of integers representing the seed value.
#    ecuKey: A list of integers representing the ECU key (not used in the function, but might be for future implementations or standards compliance).
# Returns:
#    A list of integers representing the calculated key.
# 1. Defines a device secret, 'deviceSecret', as a list of predefined integers.
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

    sbl = ihexFile("TGT-ASSY-1383_v2.1.0_sbl.hex")

    app = ihexFile("e400_uds_test_app_e400.ihex")

    e400 = createUdsConnection("Bootloader.odx", "Bootloader", reqId=0x601, resId=0x651, interface="peak")

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

    b = calculateKeyFromSeed(a, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    print("Calculated Key: {0}".format(b))

    a = e400.securityAccess("Programming Key", b)
    print("Security Access Granted")

    print("Setting up transfer of Secondary Bootloader")
    transmitAddress = sbl.transmitAddress
    transmitLength = sbl.transmitLength

    a = e400.requestDownload([0], transmitAddress, transmitLength)
    # print(a)

    print("Transferring Secondary Bootloader")
    chunks = sbl.transmitChunks(sendChunksize=1280)
    for i in range(len(chunks)):
        a = e400.transferData(i + 1, chunks[i])

    print("Finished Transfer")
    a = e400.transferExit()

    print("Jumping to Secondary Bootloader")
    a = e400.routineControl("Start Secondary Bootloader", 1, [DecodeFunctions.buildIntFromList(transmitAddress)])
    # print(a)


    print("In Secondary Bootloader")
    print("Erasing Memory")

    transmitAddress = app.transmitAddress
    transmitLength = app.transmitLength
    a = e400.routineControl("Erase Memory", 1, [("memoryAddress", [DecodeFunctions.buildIntFromList(transmitAddress)]), ("memorySize", [DecodeFunctions.buildIntFromList(transmitLength)])])
    # print(a)

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

    print("Setting up transfer for Application")

    print("Transferring Application")
    blocks = app.blocks

    for i in blocks:
        chunks = i.transmitChunks(1280)
        transmitAddress = i.transmitAddress
        transmitLength = i.transmitLength
        a = e400.requestDownload([0], transmitAddress, transmitLength)

        for j in range(0, len(chunks)):
            a = e400.transferData(j + 1, chunks[j])


    # for i in range(0, len(chunks)):
    #
    #     a = e400.transferData(i+1, chunks[i])

    print("Transfer Exit")
    a = e400.transferExit()

    a = e400.routineControl("Check Valid Application", 0x01)

    working = True
    while working:

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