def mult_list(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product

list = [1, 5, 8, 12]
result = mult_list(list)
print(result)