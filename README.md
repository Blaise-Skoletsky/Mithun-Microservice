# Mithun-Microservice

The microservice uses the ZeroMQ pipeline. Microservice awaits a string from the client file. It takes in either 'verb', 'adjective', 'place', 'plural-noun', or 'body'. Once microservice gets this word, it will send a randomized word of that category to that type. testfile.py shows how to send one of these strings and can be used to test the microservice.py file. 