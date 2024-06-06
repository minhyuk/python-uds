"""
This script demonstrates the usage of LinTp class for establishing a LIN Transport Protocol connection. It imports the LinTp
class from the uds module and the 'sleep' function from the time module. In the main block, a LinTp connection is created
with a node address of 0x0A.

Two transactions are then attempted using the LinTp connection. The first transaction involves sending a list 'a' and receiving
a response 'b'. The response is printed after the send and receive operations are successfully completed. If an exception occurs,
it is caught and the program continues without interruption. The same process is repeated with a different list 'a' for the
second transaction.

Finally, the closeConnection method is called to properly close the LinTp connection. Overall, this script showcases basic
yet essential functionalities of setting up a LinTp connection, sending messages, receiving responses, handling exceptions, and
closing the connection properly.
"""
from uds import LinTp
from time import sleep

if __name__ == "__main__":

    connection = LinTp(nodeAddress=0x0A)

    sleep(0.1)
    a = [0xb2, 0x01, 0xFF, 0x7F, 0xFF, 0x7F]
    try:

        connection.send(a)
        b = connection.recv(1)
        print(b)
    except:
        pass

    a = [0x22, 0xF1, 0x8C]
    try:

        connection.send(a)
        b = connection.recv(1)
        print(b)
    except:
        pass


    connection.closeConnection()
