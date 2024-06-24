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

def filter_prime(numbers):
    return list(filter(lambda x: is_prime(x), numbers))
if __name__ == "__main__":
    numbers = list(map(int, input().split()))
    prime_numbers = filter_prime(numbers)
    print( prime_numbers)
