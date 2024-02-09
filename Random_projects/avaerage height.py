student_heights = input().split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total = 0
for x in student_heights:
    total = total + x
print(f"total height = {total}")

num_stu = len(student_heights)
print(f"number of students = {num_stu}")

average_heights = int(round(total / num_stu))
print(f"average height = {average_heights}")
