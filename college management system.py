# College Management System

students = []

# Add Student
def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")
    course = input("Enter Course: ")
    marks = input("Enter Marks: ")

    student = {
        "Roll": roll,
        "Name": name,
        "Course": course,
        "Marks": marks
    }

    students.append(student)
    print("✅ Student Added Successfully!\n")


# View Students
def view_students():
    if not students:
        print("No student records found.\n")
        return

    print("\n--- Student List ---")
    for s in students:
        print(s)
    print()


# Search Student
def search_student():
    roll = input("Enter Roll Number to Search: ")
    for s in students:
        if s["Roll"] == roll:
            print("Student Found:", s)
            return
    print("❌ Student Not Found\n")


# Delete Student
def delete_student():
    roll = input("Enter Roll Number to Delete: ")
    for s in students:
        if s["Roll"] == roll:
            students.remove(s)
            print("🗑 Student Deleted Successfully\n")
            return
    print("Student Not Found\n")


# Main Menu
while True:
    print("====== College Management System ======")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        print("Exiting Program...")
        break
    else:
        print("Invalid Choice\n")