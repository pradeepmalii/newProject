# tcp-server.py

import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 5000
server_socket.bind((host, port))
server_socket.listen(5)
print("TCP Server waiting for connection...")
conn, addr = server_socket.accept()
print("Connected to:", addr)
while True:
 data = conn.recv(1024).decode()
 if not data:
  break
 print("Client:", data)
 response = input("Server: ")
 conn.send(response.encode())
conn.close()
server_socket.close()



# 1. What is difference between TCP and UDP?
# TCP is connection-oriented, ensures data is delivered in order, checks for errors, and retransmits
# lost packets. making it slower but highly reliable.
# UDP is connectionless and does not guarantee delivery, order, or error checking making it faster
# and more efficient for real-time applications.
# 2. What is the loop back address?
# The loopback address is a special IP address used by a computer to communicate with itself. The
# most commonly used loopback address is 127.0.0.1 in IPv4. It is mainly used for testing and
# troubleshooting network software without involving external network connections.
# 3. What is the use of a socket library in python?
# The socket library in Python is used to enable communication between different devices over a
# network using protocols like TCP and UDP. It provides the tools to create client-server
# applications by allowing programs to send and receive data through sockets, which act as
# endpoints of communication.

