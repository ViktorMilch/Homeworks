def make_squeres_dict(numbers = (1, 2, 3)):
    new_squeres_dict = {}
    for values in numbers:
        new_squeres_dict[values ** 2] = values
    return new_squeres_dict
print(make_squeres_dict())
print(make_squeres_dict(numbers=(-10, 0, 20)))
    
# numbers = {1:1, 2:4, 3:9}
# sq_numbers = {values: key for key, values in numbers.items()}
# print(sq_numbers)