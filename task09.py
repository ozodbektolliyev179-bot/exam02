def find_min_max(numbers: list) -> dict:
        if not numbers:
            return {"min": None, "max": None}
        minimum = min(numbers)
        maximum = max(numbers)  
        return {
            "min": minimum,
            "max": maximum
        }
print(find_min_max([3, 1, 4, 1, 5, 9, 2, 6, 5]))

