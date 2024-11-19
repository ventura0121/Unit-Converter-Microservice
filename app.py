import zmq
import json
from converters import convert_length, convert_weight, convert_temperature

# Set up ZeroMQ context and socket for receiving requests
context = zmq.Context()
socket = context.socket(zmq.REP)  # REP (reply) socket to respond to client requests
socket.bind("tcp://*:5555")  # Listening on TCP port 5555

def handle_conversion(data):
    category = data.get('category')
    value = data.get('value')
    from_unit = data.get('from_unit')
    to_unit = data.get('to_unit')
    
    if not category or not from_unit or not to_unit:
        return {"error": "Category, from_unit, and to_unit must all be specified."}

    if category not in ['length', 'weight', 'temperature']:
        return {"error": "Unsupported category. Choose 'length', 'weight', or 'temperature'."}

    try:
        if category == 'length':
            result = convert_length(value, from_unit, to_unit)
        elif category == 'weight':
            result = convert_weight(value, from_unit, to_unit)
        elif category == 'temperature':
            result = convert_temperature(value, from_unit, to_unit)
        return {
            'original_value': value,
            'original_unit': from_unit,
            'converted_value': result,
            'converted_unit': to_unit
        }
    except ValueError as e:
        return {"error": str(e)}

# Server loop
while True:
    # Wait for the next request from the client
    message = socket.recv_json()
    print(f"Received request: {message}")
    
    # Handle the conversion
    response = handle_conversion(message)
    
    # Send the response back to the client
    socket.send_json(response)
