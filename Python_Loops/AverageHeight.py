print("\n***Welcome to the Average Height***\n")

student_heights = input("Input a list of student heights. ").split()

for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

total_heights = 0
total_students = 0

for height in student_heights:
    total_heights += height
    total_students += 1

avg_height = round(total_heights / total_students, 2)

print(f"\nAverage height is {avg_height}\n")
