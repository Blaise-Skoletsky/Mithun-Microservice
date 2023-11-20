import zmq


context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")


socket.send_string("adjective")

while True:
    

    # Receive the response from the server
    response = socket.recv_string()
    print("Received response from server: %s" % response)
    break

socket.send_string('close')


socket.close()
context.term()