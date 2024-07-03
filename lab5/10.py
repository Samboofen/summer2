import re

def camel_to_snake(text):
    result = re.sub(r'(?<=[a-z0-9])([A-Z])', r'_\1', text)
    result = result.lower()
    
    return result
test_strings = [
    "camelCase",
    "CamelCaseString",
    "simpleTestCase",
    "convertThisString",
    "anotherExampleForTesting"
]
for s in test_strings:
    print(f"Input: '{s}'")
    print(f"Snake case: '{camel_to_snake(s)}'")
    print()
