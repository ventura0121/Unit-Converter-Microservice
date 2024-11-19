import zmq
import json

# Create a ZeroMQ context and socket for sending requests
context = zmq.Context()
socket = context.socket(zmq.REQ)  # REQ (request) socket to send requests to the server
socket.connect("tcp://localhost:5555")  # Connect to the server on port 5555

def send_conversion_request(category, value, from_unit, to_unit):
    request = {
        'category': category,
        'value': value,
        'from_unit': from_unit,
        'to_unit': to_unit
    }
    
    # Send the conversion request to the server
    socket.send_json(request)
    
    # Receive the response from the server
    response = socket.recv_json()
    print("Received response:", response)

# Example: Request to convert 100 meters to kilometers
send_conversion_request('length', 100, 'meter', 'kilometer')
