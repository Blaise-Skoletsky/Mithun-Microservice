# Mithun-Microservice

The microservice uses the ZeroMQ pipeline to generate a random ing-verb, adjective, plural noun, place, or body part.
It then sends this word back to the client who requested the word. 


Dependencies: 
    -ZeroMQ: Can be installed with pip i zmq

Microservice can be ran using python3 microservice.py

Communication Contract: 

    Requesting Data:

    To request data make sure to have the client side code using a Request socket. This program will use the socket.send_string command to send a key-word relating to what you want sent back. Key words that work are 'verb', 'adjective', 'place', 'plural-noun', and 'body'. Any other word sent will result in an error. 

    Once the microservice recieves the word, (recive steps located below), that word will be used as a variable to trigger the word that is sent back. Ex, place being recieved by the microservice would mke the randomizer function trigger on the places array, causing a place to be sent back. 

    Code of this example: 

        Client side request:


        socket.send_string('place')

        //Now we enter a loop to await the responce from our request: 

        while True:

            //Responce recieves the word we wanted.
            responce = socket.recv_string()
        
    Microservice code: 

        //A loop is checking at all times for a request from the client:
        while True:
            message = socket.recv_string()
            
            // If no message is found, nothing happens.
            // If found, perform some actions:
            result = randomizer(message)

            //responce to request
            socket.send_string(result)


Recieving Data:

    In order to recieve data from the microservice, after requesting enter a while loop that uses the socket.recv_string. This loop should be done right after making the request discussed prior.


IMPORTANT: In order for the microservie to be closed, send the string 'close' at the end of the client program using the socket.send_string() method. This will allow the program to close naturally. 


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
