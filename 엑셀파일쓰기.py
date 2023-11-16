from openpyxl import Workbook
from random import randint

# Create a workbook and select the active worksheet
wb = Workbook()
ws = wb.active

# Add headers to the worksheet
ws.append(['Product ID', 'Product Name', 'Price', 'Quantity'])

# Sample product names and prices
product_names = [
    "Laptop", "Smartphone", "Tablet", "Headphones", "Smartwatch",
    "Camera", "Speaker", "Gaming Console", "External Hard Drive", "Monitor"
]

# Generating 100 sample data rows
for i in range(1, 101):
    product_id = i
    product_name = product_names[randint(0, len(product_names) - 1)]
    price = round(randint(500, 3000) + randint(0, 99) / 100, 2)  # Random price between 500 and 3000
    quantity = randint(1, 10)  # Random quantity between 1 and 10

    # Append the data to the worksheet
    ws.append([product_id, product_name, price, quantity])

# Save the workbook
wb.save('salex.xlsx')
