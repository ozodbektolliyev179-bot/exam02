def square_values(numbers: list) -> list:
    return list(map(lambda x:{'value': x['value']**2}, numbers))




print(square_values([{'value': 2}, {'value': 3}, {'value': 4}]))
# [{'value': 4}, {'value': 9}, {'value': 16}]

print(square_values([{'value': -2}, {'value': 5}]))
# [{'value': 4}, {'value': 25}]