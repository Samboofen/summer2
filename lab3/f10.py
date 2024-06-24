
def unique_elements(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    
    return unique_list

if __name__ == "__main__":
    test_list = [1, 2, 2, 3, 4, 4, 5]
    result = unique_elements(test_list)
    print("Original List:", test_list)
    print("List with Unique Elements:", result)