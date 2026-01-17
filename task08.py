def calculate_stats(numbers: list) -> dict:
    if not numbers:
        return { "sum": None, "average": None}
    total = sum(numbers)
    average = total / len(numbers)
    return {
        "sum": total,
        "average": round(average, 2)
    }
print(calculate_stats([3, 7, 10, -5, -8, 15, 22]))



