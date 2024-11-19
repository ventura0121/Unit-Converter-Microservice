# Unit-Converter-Microservice

## This repository contains a Unit Converter Microservice that provides conversion functionality for various unit types (e.g., length, weight, temperature) via a ZeroMQ communication protocol. This README provides instructions for how to programmatically request data from the microservice and receive the results.

### Communication Contract
1. Requesting Data from the Microservice
The microservice accepts requests in JSON format over ZeroMQ. The request should contain the following fields:
* category: The type of units you are converting (e.g., "length", "temperature").
* value: The value you want to convert.
* from_unit: The unit of the value to be converted.
* to_unit: The target unit to convert to.

  e.g
  {
  "category": "length",
  "value": 100,
  "from_unit": "meter",
  "to_unit": "kilometer"
}


2. Receiving Data from the Microservice
Once the request is sent, the microservice will respond with a JSON object that includes the following fields:

* original_value: The original value sent in the request.
* original_unit: The unit of the original value.
* converted_value: The converted value.
* converted_unit: The unit of the converted value.
  
  e.g
{
  "original_value": 100,
  "original_unit": "meter",
  "converted_value": 0.1,
  "converted_unit": "kilometer"
}


3. How to Programmatically Request and Receive Data
To interact with the microservice programmatically, use ZeroMQ to send and receive JSON-encoded requests and responses.
import zmq

Establish ZeroMQ context and socket
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

Define the conversion request
request = {
    "category": "length",
    "value": 100,
    "from_unit": "meter",
    "to_unit": "kilometer"
}

Send the request
socket.send_json(request)

Receive and print the response
response = socket.recv_json()
print("Received response:", response)


4. If the microservice receives an invalid request (e.g., missing or unsupported units), it will return an error response. Below is an example of how you can handle errors:

### UML Sequence Diagram
+----------------+              +-------------------------+
|    Client      |              |  Unit Converter Service |
+----------------+              +-------------------------+
        |                                  |
        |     Request Conversion           |
        |--------------------------------->|
        |                                  |
        |                                  | 
        |           Process Request        |
        |                                  |
        |            Send Response         |
        |<---------------------------------|
        |                                  |
        |        Receive Response          |
        |                                  |
        |        (Original, Converted)     |
        +----------------------------------+


