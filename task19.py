def find_longest_name(names: list) -> str:
    max_name = names[0]
    for name in names:
        if len(name) > len(max_name):
            max_name = name
    return max_name

print(find_longest_name(['Ali', 'Diyor', 'Jasurbek', 'Muhammad']))
