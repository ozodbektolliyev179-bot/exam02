def analyze_grades(students: dict) -> dict:

    jami_baho = 0
    for baho in students.values():
        jami_baho += baho

    ortacha = jami_baho / len(students)


    yuqori_baholar = []
    for ism, baho in students.items():
        if baho > ortacha:
            yuqori_baholar.append(ism)

    return {
        "average": round(ortacha, 2),
        "above_average": yuqori_baholar
    }
print(analyze_grades({"Ali": 5, "Vali": 4, "Hasan": 5, "Husan": 3}))