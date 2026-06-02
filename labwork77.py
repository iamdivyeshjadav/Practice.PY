start = 10
end = 30
prime_numbers = []

for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(num)

print("Prime numbers array:", prime_numbers)
'''
Output:
Prime numbers array: [11, 13, 17, 19, 23, 29]
'''