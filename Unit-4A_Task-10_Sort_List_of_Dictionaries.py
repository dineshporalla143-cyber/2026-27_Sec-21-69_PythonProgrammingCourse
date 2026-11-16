students = [
    {"name": "Dinesh", "marks": 85},
    {"name": "Dharma", "marks": 95},
    {"name": "Dhanush", "marks": 75}
]

students.sort(key=lambda x: x["marks"])

print("Sorted Student Records:")

for student in students:
    print(student)