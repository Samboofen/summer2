import re

def insert_spaces(text):
    # Define the pattern: look for uppercase letters preceded by a lowercase letter or another uppercase letter
    pattern = r'(?<!^)(?=[A-Z])'
    
    # Use re.sub to insert spaces where the pattern matches
    result = re.sub(pattern, ' ', text)
    
    return result

# Test cases
test_strings = [
    "HelloWorld",
    "PythonIsFun",
    "ThisIsATest",
    "UpperCaseLetters",
    "anotherExampleWithMixedCase"
]

# Apply the insert_spaces function to each test string and print the results
for s in test_strings:
    print(f"Input: '{s}'")
    print(f"With spaces: '{insert_spaces(s)}'")
    print()
