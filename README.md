# Mithun-Microservice

The microservice uses the ZeroMQ pipeline to generate a random ing-verb, adjective, plural noun, place, or body part.
It then sends this word back to the client who requested the word. 


Dependencies: 
    -ZeroMQ: Can be installed with pip i zmq

Microservice can be ran using python3 microservice.py

Communication Contract: 

    Requesting Data:

    To request data make sure to have the client side code using a Request socket. This program will use the socket.send_string command to send a word 


To recieve data, use the socket.recv() command. This should recive some information sent from the other file to this file. In this instance, A request for a word is sent to the microservice.py file. The file recieves the data by setting the message variable equal to socket.recv(). This information has to be decoded into utf-8 characters, which can be done by setting the recieved message variable = to message.decode('utf-8).

To request data, you would have to send information to the other file, using socket.send_string. When the other file recieves this string, it will use the contents to send back some answer. For example in this microservice the main project sends a key-phrase to the microservice, this acts as a request to the microservice, as it sees this phrase and uses it to send back a certain word. 





UML Sequence Diagram: 

Microservice should be ran before the client side code. 



[ Client-Side ]           [ Microservice ] 
       .                          |       
       .    Connect to socket     |
       . <----------------------  |
       |                          |
       |                          |
       |                          |
       |    Sends a keyword       |
       |    to be generated       |
       |  --------------------->  | 
       |                          | 
       |                          |
       |                          |
       |                          |
       |                          |
       |    Send back random      |
       |    generated word        |
       |  <---------------------- |
       |                          |
       |                          |
       |                          |
       |                          |
