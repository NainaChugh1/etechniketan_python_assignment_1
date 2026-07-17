subjects = ["Python", "SQL", "Excel", "Tableau"]

print("Complete List:", subjects)

print("First Subject:", subjects[0])
print("Last Subject:", subjects[-1])

subjects.insert(1, "Power BI")
print("\nAfter Adding a Subject:", subjects)

subjects.remove("Excel")
print("\nAfter Removing Excel:", subjects)

new_subjects = subjects.copy()

new_subjects.sort()
print("\nSorted List:", new_subjects)

if "Excel" in new_subjects:
    print("\nExcel is Present")
else:
    print("\nExcel is Not Present")
