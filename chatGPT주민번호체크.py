import re

def check_korean_resident_number(number):
    pattern = re.compile(r'^\d{6}-?[1-2]\d{6}$')
    return bool(pattern.match(number))

# Test cases
samples = [
    'YYMMDD-1#######',  # Replace YYMMDD with valid year, month, day
    'YYMMDD-2#######',  # Replace YYMMDD with valid year, month, day
    '930101-1123456',
    '8505061123456',
    '751212-2123456',
    '200304-1123456',
    '123456-1123456',  # Invalid length
    '990101-3123456',  # Invalid first digit of last 7 digits
    '030101-4123456',  # Invalid first digit of last 7 digits
    '921314-1123456',  # Invalid month (13)
]

for sample in samples:
    result = check_korean_resident_number(sample)
    print(f'{sample}: {"Valid" if result else "Invalid"}')
