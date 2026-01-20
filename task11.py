def analyze_list(items: list) -> dict:
    result = {"total": 0, "unique": 0, "duplicatas": [], "mast_comman": None}

    result["total"] = len(items)
    result["unique"] = len(set(items))

    for item in items:
        if items.count(item) > 1 and item not in result["duplicatas"]:
            result["duplicatas"].append(item)
    
    result["mast_comman"] = max(items, key=lambda item: items.count(item),default=None)

    return result


items = ["Ali", "Vali", "Ali", 1, 2, 1]

print(analyze_list(items))