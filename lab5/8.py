import re

def split_at_uppercase(text):
    pattern = r'(?=[A-Z])'
    result = re.split(pattern, text)
    result = list(filter(None, result))
    
    return result
test_strings = [
    "HelloWorld",
    "PythonIsFun",
    "ThisIsATest",
    "UpperCaseLetters",
    "anotherExampleWithMixedCase"
]
for s in test_strings:
    print(f"Input: '{s}'")
    print(f"Split: {split_at_uppercase(s)}")
    print()
