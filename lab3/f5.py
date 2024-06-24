from itertools import permutations

def print_permutations(input_string):
    perm = permutations(input_string)
    for p in perm:
        print(''.join(p))

if __name__ == "__main__":
    input_string = input()
    
    print()
    print_permutations(input_string)