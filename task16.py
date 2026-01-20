def count_by_grade(grades: dict, target_grade: int) -> dict:
    count = 0
    students_with_target_grade = []

    for name, grade in grades.items():
        if grade == target_grade:
            count += 1
            students_with_target_grade.append(name)

    return {
        "count": count,
        "students": students_with_target_grade
    }
print(count_by_grade({"Ali": 5, "Vali": 4, "Hasan": 3, "Husan": 5}, 5))

print(count_by_grade({"Aziz": 4, "Bobur": 4, "Diyor": 3}, 4))
# {"count": 2, "students": ["Aziz", "Bobur"]})
# ["Bobur", "Jasur"]