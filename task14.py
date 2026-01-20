def find_pattern(items: list, pattern: str, match_type: str) -> list:
    if match_type == "starts":
        return [item for item in items if item.startswith(pattern)]
    elif match_type == "ends":
        return [item for item in items if item.endswith(pattern)]
    elif match_type == "contains":
        return [item for item in items if pattern in item]
    else:
        return []
print(find_pattern(["Ali", "Alisher", "Vali", "Aziz"], "V", "starts"))