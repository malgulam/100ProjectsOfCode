import socket

#initialising socket
s = socket.socket()
#assinging host and port
host = socket.gethostname()
port = 8082
print (f"FTP active\nHostname:{host}\nPort:{port}")
#binding the hostname and port
s.bind((host, port))
#listen to just one connection at a time
s.listen(1)
conn, addr = s.accept()
print (f'{addr} has just connected')
