import math
from itertools import permutations

def sphere_volume(radius):
    volume = (4/3) * math.pi * radius**3
    return volume

def print_permutations(input_string):
    perm = permutations(input_string)
    for p in perm:
        print(''.join(p))

def is_palindrome(input_string):
    cleaned_string = input_string.replace(" ", "").lower()
    return cleaned_string == cleaned_string[::-1]

if __name__ == "__main__":
    radius = 5
    volume = sphere_volume(radius)
    print(f"Volume of the sphere with radius {radius} units is: {volume:.2f} cubic units")
    
    input_string = "abc"
    print("Permutations of the string:")
    print_permutations(input_string)
    
    test_phrase = "A man a plan a canal Panama"
    if is_palindrome(test_phrase):
        print(f"'{test_phrase}' is a palindrome.")
    else:
        print(f"'{test_phrase}' is not a palindrome.")
