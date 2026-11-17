
# https://github.com/MaryamKhorsandi/student-grade-analyzer.git

import csv

students = []

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for student in reader:
        student["score"] = float(student["score"])
        students.append(student)

# Calculate average
total = 0

for student in students:
    total += student["score"]

average = total / len(students)

print("Average Score:", round(average, 2))

# Find highest and lowest
highest = students[0]
lowest = students[0]

for student in students:
    if student["score"] > highest["score"]:
        highest = student

    if student["score"] < lowest["score"]:
        lowest = student

print("Highest Score:", highest["name"], highest["score"])
print("Lowest Score:", lowest["name"], lowest["score"])

# Find failed students
failed_students = []

for student in students:
    if student["score"] < 12:
        failed_students.append(student)

print("Failed Students:")

for student in failed_students:
    print(student["name"], student["score"])

# Save failed students
with open("failed_students.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "score"])

    writer.writeheader()
    writer.writerows(failed_students)

# Find top students
top_students = []

for student in students:
    if student["score"] > 17:
        top_students.append(student)

print("Top Students:")

for student in top_students:
    print(student["name"], student["score"])

# Save top students
with open("top_students.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "score"])

    writer.writeheader()
    writer.writerows(top_students)

# Sort students by score
sorted_students = sorted(students, key=lambda student: student["score"], reverse=True)

with open("sorted_students.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "score"])

    writer.writeheader()
    writer.writerows(sorted_students)

# Final Report
print("\n========== Class Report ==========")

print("Total Students:", len(students))
print("Average Score:", round(average, 2))
print("Highest Score:", highest["name"], highest["score"])
print("Lowest Score:", lowest["name"], lowest["score"])
print("Number of Failed Students:", len(failed_students))
print("Number of Top Students:", len(top_students))
