def student():
    student_list, temp = [], []
    for _ in range(3):
        for _ in range(5):
            temp.append(input())
        student_list.append(temp)
        temp = []
    search, select, sx = input(), [], ""
    for i in student_list:
        if search in i:
            select = i
    if select == []:
        print("Student not found")
    else:
        sx = "Mr" if "Male" in select else "Miss"
        name = select[0]
        age = select[2]
        id_ = select[3]
        gpa = float(select[4])
        print(f"{sx} {name} ({age}) ID: {id_} GPA {gpa:.2f}")
student()
