student_name = input("Enter Student Name: ")
age = int(input("Enter Age: "))
city = input("Enter City: ")
course = input("Enter Course Name: ")

subject1 = float(input("Enter Marks in Subject 1: "))
subject2 = float(input("Enter Marks in Subject 2: "))
subject3 = float(input("Enter Marks in Subject 3: "))

total = subject1 + subject2 + subject3
percentage = total / 3

print("\nStudent Details")
print("Name:", student_name)
print("Age:", age)
print("City:", city)
print("Course:", course)
print("Percentage:", percentage)
