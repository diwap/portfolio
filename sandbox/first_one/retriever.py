from employee_detail import DATA

retrieved_data = DATA

def student_paragrapher(data, name):
    if not data or not isinstance(data, dict):
        return "Data not found"

    student_detail = {}
    for d in data.get("student"):
        if d.get("name") == name:
            student_detail = d

    if not student_detail:
        return "Not found"

    hob = []
    for s in student_detail.get("hobby"):
        hob.append(
            s.lower()
        )

    join_my_list = ", ".join(hob[:-1])
    print(join_my_list)

    hobby = "%s and %s" % (
        join_my_list,
        hob[-1]
    )

    summary = "My name is %s. I am %d years old. I live in %s. I like %s. My level is %s" % (
        student_detail.get("name"),
        student_detail.get("age"),
        student_detail.get("address"),
        hobby,
        student_detail.get("level")
    )
    
    return summary

student_name = "Pema Dorje"

print(student_paragrapher(retrieved_data, student_name))