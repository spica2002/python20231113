import re

# Regular expression pattern for validating email addresses
pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

# Sample email addresses for testing
emails = [
    'example@email.com',
    'user.name@email-domain.co.uk',
    'invalid.email@',
    'another_invalid.email@domain',
    'test@domain..com',
    'email@domain',
    'email@-domain.com',
    'email@domain-.com',
    'email@123.456.789.10',
    'email@[123.456.789.10]',
]

# Function to test email addresses against the pattern
def test_email(email):
    if re.search(pattern, email):
        print(f"{email} is a valid email address.")
    else:
        print(f"{email} is NOT a valid email address.")

# Test the sample email addresses
for email in emails:
    test_email(email)
