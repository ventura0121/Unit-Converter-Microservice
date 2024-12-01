import zmq

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:5555")

    while True:
        # Collect user input
        command = input("Enter 'convert' to convert or 'shutdown' to stop the service: ").strip().lower()
        
        if command == "shutdown":
            socket.send_json({"command": "shutdown"})
            print("Shutdown command sent to microservice.")
            break
        
        if command == "convert":
            amount = float(input("Enter the amount to convert: "))
            from_unit = input("Enter the unit to convert from: ").strip()
            to_unit = input("Enter the unit to convert to: ").strip()
            
            # Send request
            request = {"amount": amount, "from_unit": from_unit, "to_unit": to_unit}
            socket.send_json(request)
            
            # Receive response
            response = socket.recv_json()
            print("Response:", response)
        else:
            print("Invalid command. Try again.")

    socket.close()
    context.term()

if __name__ == "__main__":
    main()
