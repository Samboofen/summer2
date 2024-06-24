def is_palindrome(input_string):
    cleaned_string = input_string.replace(" ", "").lower()
    return cleaned_string == cleaned_string[::-1]

if __name__ == "__main__":
    test_cases = [
        "madam",
        "racecar",
        "A man a plan a canal Panama",
        "hello",
        "Was it a car or a cat I saw?"
    ]
    
    for test_case in test_cases:
        if is_palindrome(test_case):
            print(f"'{test_case}' is a palindrome.")
        else:
            print(f"'{test_case}' is not a palindrome.")
