def calculate_total_cost(**kwargs):
    price = kwargs.get('price', 0)
    quantity = kwargs.get('quantity', 0)
    name = kwargs.get('name', 'Product')
    total = price * quantity
    return f"The total cost for {quantity} x '{name}' is: ${total:.2f}"
print(calculate_total_cost(name="Laptop", price=999.99, quantity=2))
"""
output:
The total cost for 2 x 'Laptop' is: $1999.98
"""
