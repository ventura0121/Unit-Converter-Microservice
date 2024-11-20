import zmq
import json

def convert_units(amount, from_unit, to_unit):
    """Converts units based on predefined conversion factors."""
    conversion_factors = {
        # Length conversions
        ('meters', 'kilometers'): 0.001,
        ('kilometers', 'meters'): 1000,
        ('inches', 'feet'): 1 / 12,
        ('feet', 'inches'): 12,
        ('feet', 'yards'): 1 / 3,
        ('yards', 'feet'): 3,

        # Weight conversions
        ('grams', 'kilograms'): 0.001,
        ('kilograms', 'grams'): 1000,
        ('pounds', 'ounces'): 16,
        ('ounces', 'pounds'): 1 / 16,
        ('pounds', 'kilograms'): 0.453592,
        ('kilograms', 'pounds'): 1 / 0.453592,

        # Time conversions
        ('seconds', 'minutes'): 1 / 60,
        ('minutes', 'seconds'): 60,
        ('minutes', 'hours'): 1 / 60,
        ('hours', 'minutes'): 60,
        ('hours', 'days'): 1 / 24,
        ('days', 'hours'): 24,
    }

    if (from_unit, to_unit) in conversion_factors:
        factor = conversion_factors[(from_unit, to_unit)]
        return amount * factor

    # Temperature conversions
    if from_unit == 'celsius' and to_unit == 'fahrenheit':
        return (amount * 9 / 5) + 32
    elif from_unit == 'fahrenheit' and to_unit == 'celsius':
        return (amount - 32) * 5 / 9
    elif from_unit == 'celsius' and to_unit == 'kelvin':
        return amount + 273.15
    elif from_unit == 'kelvin' and to_unit == 'celsius':
        return amount - 273.15
    elif from_unit == 'fahrenheit' and to_unit == 'kelvin':
        return (amount - 32) * 5 / 9 + 273.15
    elif from_unit == 'kelvin' and to_unit == 'fahrenheit':
        return (amount - 273.15) * 9 / 5 + 32

    return None  # Unsupported conversion

def process_request(request):
    """Processes a conversion request."""
    amount = request.get('amount')
    from_unit = request.get('from_unit')
    to_unit = request.get('to_unit')

    if amount is None or not from_unit or not to_unit:
        return {
            'error': 'Invalid request. Please provide amount, from_unit, and to_unit.'
        }

    converted_value = convert_units(amount, from_unit, to_unit)

    if converted_value is None:
        return {
            'error': f"Conversion from {from_unit} to {to_unit} is not supported."
        }

    return {
        'converted_value': converted_value,
        'to_unit': to_unit
    }

def main():
    """Starts the ZeroMQ server to listen for requests."""
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5555")

    print("Listening for requests on tcp://*:5555...")
    print("Unit Converter Microservice is running and ready to process requests...")

    while True:
        # Wait for the next request from client
        request = socket.recv_json()

        # Process the request
        response = process_request(request)

        # Send the reply back to the client
        socket.send_json(response)

if __name__ == "__main__":
    main()
