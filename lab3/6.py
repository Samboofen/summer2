def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True 
    if num % 2 == 0:
        return False  
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True
numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 30, 31, 32, 40]
prime_numbers = list(filter(lambda x: is_prime(x), numbers))
print("Prime numbers in the list:", prime_numbers)