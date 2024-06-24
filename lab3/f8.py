def spy_game(nums):
    found_0 = False
    found_00 = False
    for num in nums:
        if num == 0 and not found_0:
            found_0 = True
        elif num == 0 and found_0 and not found_00:
            found_00 = True
        elif num == 7 and found_0 and found_00:
            return True
    
    return False

print(spy_game([1, 2, 4, 0, 0, 7, 5]))   
print(spy_game([1, 0, 2, 4, 0, 5, 7]))   
print(spy_game([1, 7, 2, 0, 4, 5, 0]))   
