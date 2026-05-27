from turtle import pd


students = [
    {"id": 101, "name": "Alice", "score": 85},
    {"id": 102, "name": "Bob", "score": 78},
    {"id": 103, "name": "Charlie", "score": 92}
]
print("--- Student Names ---")
for student in students:
    print(student["name"])
avg_score = sum(s["score"] for s in students) / len(students)
print(f"\nAverage Score: {avg_score:.2f}")
students.append({"id": 104, "name": "David", "score": 95})
for student in students:
    if student["id"] == 102:
        student["score"] = 88
students = [student for student in students if student["name"] != "Charlie"]
print("\n--- Students with Score > 80 ---")
for student in students:
    if student["score"] > 80:
        print(student["name"])
students.sort(key=lambda x: x["score"], reverse=True)
highest_student = max(students, key=lambda x: x["score"])
print(f"\nHighest Scorer: {highest_student['name']} ({highest_student['score']})")
print("\n--- Student Report ---")
grade_counts = {"A": 0, "B": 0, "C": 0}

for student in students:
    score = student["score"]
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    else:
        grade = "C"
    grade_counts[grade] += 1
    
    print(f"Name: {student['name']} | Score: {score} | Grade: {grade}")

print("\n--- Grade Counts ---")
for grade, count in grade_counts.items():
    print(f"Grade {grade}: {count}")
'''
Output:
--- Student Names ---
Alice
Bob
Charlie
Average Score: 85.00
--- Students with Score > 80 ---
Alice
David
Highest Scorer: David (95)
--- Student Report ---
Name: Alice | Score: 85 | Grade: B
Name: Bob | Score: 88 | Grade: B
Name: David | Score: 95 | Grade: A
--- Grade Counts ---
Grade A: 1
Grade B: 2
Grade C: 0
'''
