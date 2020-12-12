#this http server uses the python sockets module!

#uses tcp server socket + IPv4 protocols(AF_INET)

#imports
from socket import *
import random

#Initialising the socket
sock = socket.socket(AF_INET, SOCK_STREAM)

#assigning the hostname
host = 'stevenson'

#Assigning a port number to the socket
#using random number between 8080-9000
port = random.randint(8080, 9000)

#binding the socket server and address
sock.bind((host, port))

#listen for one connection at a time
sock.listen(1)

#when the user is connected send the user a file

conn, addr = sock.accept()
try:
    #assinging the contents of the the file to a variable called message
    message = open('serving_text_file.txt').read()
    #since sockets work with bytes, we have to encode the string into bytes
    sock.send(str(message).encode())
    print(f'sent the message to the connection {conn} and address{addr}')
except Exceptions as e:
    print ('An error occured')
    print(e)
