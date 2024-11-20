import zmq

# Setup ZeroMQ context and socket
context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

def main():
    print("Unit Converter Test Program")
    print("Type 'exit' to quit at any time.")
    print("-" * 40)

    while True:
        try:
            # Get user input for amount, from_unit, and to_unit
            user_input = input("Enter amount, from_unit, and to_unit separated by spaces (e.g., '100 celsius fahrenheit'): ")
            if user_input.lower() == 'exit':
                print("Exiting program. Goodbye!")
                break

            # Parse the input
            parts = user_input.split()
            if len(parts) != 3:
                print("Invalid input. Please provide amount, from_unit, and to_unit separated by spaces.")
                continue

            amount = float(parts[0])  # Convert the first part to a float
            from_unit = parts[1].lower()  # Standardize to lowercase for consistency
            to_unit = parts[2].lower()

            # Create the request dictionary
            request = {'amount': amount, 'from_unit': from_unit, 'to_unit': to_unit}

            # Send the request to the microservice
            print(f"Sending request: {request}")
            socket.send_json(request)

            # Receive and display the response
            response = socket.recv_json()
            print(f"Received response: {response}")
            print("-" * 40)

        except ValueError:
            print("Invalid input. Amount must be a number.")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
