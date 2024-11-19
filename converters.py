conversion_factors = {
    'length': {
        'meter': 1.0,
        'kilometer': 0.001,
        'mile': 0.000621371,
        'yard': 1.09361,
        'foot': 3.28084,
    },
    'weight': {
        'kilogram': 1.0,
        'gram': 1000.0,
        'pound': 2.20462,
        'ounce': 35.274,
    },
    'temperature': {},  # Special handling required
}

def convert_length(value, from_unit, to_unit):
    if from_unit not in conversion_factors['length'] or to_unit not in conversion_factors['length']:
        raise ValueError("Invalid units for length conversion.")
    base_value = value / conversion_factors['length'][from_unit]
    return base_value * conversion_factors['length'][to_unit]

def convert_weight(value, from_unit, to_unit):
    if from_unit not in conversion_factors['weight'] or to_unit not in conversion_factors['weight']:
        raise ValueError("Invalid units for weight conversion.")
    base_value = value / conversion_factors['weight'][from_unit]
    return base_value * conversion_factors['weight'][to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == 'celsius' and to_unit == 'fahrenheit':
        return (value * 9/5) + 32
    if from_unit == 'fahrenheit' and to_unit == 'celsius':
        return (value - 32) * 5/9
    if from_unit == 'celsius' and to_unit == 'kelvin':
        return value + 273.15
    if from_unit == 'kelvin' and to_unit == 'celsius':
        return value - 273.15
    raise ValueError("Invalid units for temperature conversion.")
