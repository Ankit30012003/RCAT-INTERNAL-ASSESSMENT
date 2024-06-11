def square_of_evens(numbers):
    return [num ** 2 for num in numbers if num % 2 == 0]


original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list = square_of_evens(original_list)
print(new_list)

"""
output:- [4, 16, 36, 64, 100]
"""
