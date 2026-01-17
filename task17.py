def filter_positive(numbers: list) -> list:
    return list(filter(lambda x: x['value'] > 0, numbers))
print = filter_positive([{'value': -5}, {'value': 10}, {'value': -1}, {'value': 7}])

# [{'value': 10}, {'value': 7}] 
