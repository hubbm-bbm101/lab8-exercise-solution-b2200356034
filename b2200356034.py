import sys
students = {}
lines = []
with open("student.txt", "r") as f:
    for line in f:
        if line.endswith("\n"):
            line = line[:-1]
        lines.append(line)
    print(lines)
    for i in lines:
        line = i.split(":")
        students[line[0]] = line[1]
    print(students)
    for j in sys.argv[1:]:
        try:
            print("Name: {}, University: {}".format(j, students[j]))
            assert j in students
        except:
            print("No record of {} was found!".format(j))
