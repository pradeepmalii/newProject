from xmlrpc.server import SimpleXMLRPCServer
# Create RPC server
server = SimpleXMLRPCServer(("localhost", 8000))
print("RPC Server is running on port 8000...")
# Define remote functions
def add(a, b):
 return a + b
def subtract(a, b):
 return a - b
def multiply(a, b):
 return a * b
def divide(a, b):
 if b == 0:
  return "Error: Division by zero"
 return a / b
# Register functions
server.register_function(add, "add")
server.register_function(subtract, "subtract")
server.register_function(multiply, "multiply")
server.register_function(divide, "divide")
# Run server
server.serve_forever()


# 1. Explain Remote Procedure Call (RPC)
# Remote Procedure Call (RPC) is a protocol that allows a program to execute a procedure or
# function on a different computer (remote system) as if it were a local function call. When an RPC
# is made, the client sends a request to the server, which processes it and returns the result. This
# mechanism is widely used in distributed systems to enable communication between applications
# running on different machines without requiring the programmer to manage low-level networking
# details.
# 2. What is different between TCP and UDP?
# Transmission Control Protocol (TCP) and User Datagram Protocol (UDP) are both transport layer
# protocols used for communication over networks, but they differ in how they transmit data.
# TCP is connection-oriented, ensures data is delivered in order, checks for errors, and retransmits
# lost packets. making it slower but highly reliable.
# UDP is connectionless and does not guarantee delivery, order, or error checking making it faster
# and more efficient for real-time applications.
# 3. Explain Telnet
# Telnet is a network protocol used to remotely access and manage computers over a network,
# typically through a command-line interface. It allows a user to log into another machine and
# execute commands as if they were physically present at that system. Telnet operates over TCP
# and is simple to use, but it is considered insecure because it transmits data, including usernames
# and passwords, in plain text without encryption.