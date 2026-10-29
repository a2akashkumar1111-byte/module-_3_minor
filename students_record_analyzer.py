subject = ("Python", "Maths", "DBMS")
print(subject)
student_number = int(input("How many students? "))
details = {}
student_id = []
count = 0

for i in range(student_number):
    ids = int(input("student id "))
    student_id.append(ids)

    name = input("name: ")
    marks =[]
    count += 1

    for j in range(len(subject)):
        m = int(input(f"{subject[j]} marks: "))
        marks.append(m)

    details[ids] =  {"name" : name , "marks" : marks}
print(details)

total_list = []
print("____STUDENT REPORT_____")
for ids in details:
    name = details[ids]['name']
    marks = details[ids]['marks']

    total = 0
    for m in marks:
        total = total + m
    
    average = total / len(marks)
    total_list.append(average)
    if average >= 75:
        result = "Distinction"
    elif average >= 40:
        result = "Pass"
    else:
        result = "Fail"
    
    details[ids]['total'] = total
    details[ids]['average'] = average
    details[ids]['result'] = result
    
    print(f"\n{ids} | {name}")
    print(f"{subject[0]}: {marks[0]}, {subject[1]}: {marks[1]}, {subject[2]}: {marks[2]}")
    print(f"Total: {total} | Average: {average:.2f} | Result: {result}")

ids = int(input("\ninput searching student id: "))

if ids in details:
    print(f"\n{ids} | {details[ids]}")
else:
    print("no record found.")

print("first two student ids: ",student_id[:2])

print("total number of student recorded: ",count)
