attendance = [
    ("EMP101", "Anish"),
    ("EMP102", "Rahul"),
    ("EMP103", "Priya"),
    ("EMP101", "Anish"),
    ("EMP104", "Kiran")
]

# To Find duplicate attendance records
print("Duplicate Records:")
seen = set()

for record in attendance:
    if record in seen:
        print(record)
    else:
        seen.add(record)

# To Print unique employees
print("\nUnique Employees:")
unique = set(attendance)

for emp in unique:
    print(emp)

# 3. Count total unique employees
print("\nTotal Unique Employees:", len(unique))

# 4. Display employee IDs in sorted order
print("\nSorted Employee IDs:")

emp_ids = []

for emp in unique:
    emp_ids.append(emp[0])

emp_ids.sort()

for emp_id in emp_ids:
    print(emp_id)