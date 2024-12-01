import json

def load_conversions():
    """Load conversion data from the JSON file."""
    with open('conversions.json', 'r') as f:
        return json.load(f)

def convert_units(amount, from_unit, to_unit):
    """
    Converts the given amount from one unit to another.
    Supports metric and imperial units for length, weight, and temperature.
    """
    conversions = load_conversions()
    
    # Normalize units to lowercase for comparison
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    # Handle length and weight conversions
    for category, rules in conversions.items():
        for key, value in rules.items():
            if key == f"{from_unit}_to_{to_unit}":
                # For numeric conversion factors
                if isinstance(value, (int, float)):
                    return amount * value
                
                # For temperature formulas
                if isinstance(value, str):
                    x = amount
                    return eval(value)
    
    raise ValueError(f"Conversion from {from_unit} to {to_unit} is not supported.")
