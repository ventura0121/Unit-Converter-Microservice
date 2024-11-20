# Unit-Converter-Microservice

## This repository contains a Unit Converter Microservice that provides conversion functionality for various unit types (e.g., length, weight, temperature) via a ZeroMQ communication protocol. This README provides instructions for how to programmatically request data from the microservice and receive the results.

### Communication Contract

The microservice receives requests via ZeroMQ in the form of a JSON object containing the following fields:
```plaintext
{
  "amount": <numeric value>,
  "from_unit": "<unit to convert from>",
  "to_unit": "<unit to convert to>"
}
```
* amount: The numeric value you want to convert (e.g., 100).
* from_unit: The unit you are converting from (e.g., meters).
* to_unit: The unit you are converting to (e.g., feet).

The microservice will respond with a JSON object that contains:
```plaintext
{
  "converted_value": <converted value>,
  "to_unit": "<target unit>"
}
```
* converted_value: The result of the conversion (e.g., 328.084).
* to_unit: The unit the amount was converted to (e.g., feet).

### How to Programmatically Request Data from the Microservice
To request data from the microservice, you need to send a JSON message to the microservice over ZeroMQ. Below are the steps and example code for doing so.
Install the required package pyzmq if you haven't already:
1. pip install pyzmq
2. Set up the ZeroMQ client to send a request to the microservice.
3. Create a request message with the following parameters:
* amount: The numeric value to be converted.
* from_unit: The unit from which you are converting.
* to_unit: The unit to which you are converting.
4. Send the request and wait for the response.
```plaintext
import zmq

# Create a ZeroMQ context and socket
context = zmq.Context()
socket = context.socket(zmq.REQ)

# Connect to the microservice (running on port 5555)
socket.connect("tcp://localhost:5555")

# Prepare the request message
request_data = {
    "amount": 100,        # Amount to convert
    "from_unit": "meters",  # Unit to convert from
    "to_unit": "feet"      # Unit to convert to
}

# Send the request to the microservice
socket.send_json(request_data)

# Receive the response from the microservice
response = socket.recv_json()

# Print the response data (converted value)
print("Converted value:", response)
```
Example Request
```plaintext
{
  "amount": 100,
  "from_unit": "meters",
  "to_unit": "feet"
}
```
The microservice will respond with:
```plaintext
{
  "converted_value": 328.084,
  "to_unit": "feet"
}
```
### How to Programmatically Receive Data from the Microservice
Once you send a request, the microservice will respond with a JSON message containing the converted value and target unit.
1. After sending the request, the client will wait for the response from the microservice.
2. The microservice responds with a JSON message containing the conversion result.

```plaintext
# The response is already captured with socket.recv_json()
# This will be a dictionary containing the conversion result

response = socket.recv_json()

# Access the data from the response
converted_value = response['converted_value']
to_unit = response['to_unit']

# Use the data as needed
print(f"Converted value: {converted_value} {to_unit}")

```
For the input 100 meters to feet, the response would be:

```plaintext
{
  "converted_value": 328.084,
  "to_unit": "feet"
}
```

![image](https://github.com/user-attachments/assets/c4e6fb56-634c-4108-9b6c-3ae5ad9a82fc)

