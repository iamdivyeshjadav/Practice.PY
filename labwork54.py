def sum_and_product(*args):
    total_sum = sum(args)
    total_product = 1 if args else 0
    for num in args:
        total_product *= num
    return total_sum, total_product

# Example usage
s, p = sum_and_product(2, 3, 4)
print(f"Sum: {s}, Product: {p}")