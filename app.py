import zmq
from converters import convert_units

def main():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")
    
    print("Microservice is running...")
    
    while True:
        message = socket.recv_json()
        if message.get("command") == "shutdown":
            print("Shutting down the microservice...")
            break
        
        try:
            amount = message["amount"]
            from_unit = message["from_unit"]
            to_unit = message["to_unit"]
            converted_value = convert_units(amount, from_unit, to_unit)
            response = {"converted_value": converted_value, "to_unit": to_unit}
        except Exception as e:
            response = {"error": str(e)}
        
        socket.send_json(response)
    
    socket.close()
    context.term()

if __name__ == "__main__":
    main()
