import zmq

def main():
    # Create a ZeroMQ context and a REQ socket
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")  # Connect to the microservice

    # Send a valid conversion request (e.g., converting 100 meters to kilometers)
    request = {
        "category": "length",
        "value": 100,
        "from_unit": "meter",
        "to_unit": "kilometer"
    }
    print(f"Sending request: {request}")
    socket.send_json(request)  # Send the request to the server

    # Receive and display the response from the microservice
    response = socket.recv_json()
    print("Received response:", response)

    # Send an invalid conversion request (e.g., with an invalid unit)
    invalid_request = {
        "category": "length",
        "value": 100,
        "from_unit": "invalid_unit",
        "to_unit": "kilometer"
    }
    print(f"\nSending invalid request: {invalid_request}")
    socket.send_json(invalid_request)  # Send the invalid request

    # Receive and display the invalid response from the microservice
    invalid_response = socket.recv_json()
    print("Received invalid response:", invalid_response)

if __name__ == "__main__":
    main()
