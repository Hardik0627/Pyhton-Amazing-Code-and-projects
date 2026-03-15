# College Roll Number Management System

students = {}

def add_student():
    roll = input("Enter Roll Number: ")
    name = input("Enter Student Name: ")

    if roll in students:
        print("⚠ Roll number already exists!")
    else:
        students[roll] = name
        print("✅ Student added successfully!")

def view_students():
    if not students:
        print("No records found.")
    else:
        print("\n--- Student Records ---")
        for roll, name in students.items():
            print(f"Roll No: {roll} | Name: {name}")

def search_student():
    roll = input("Enter Roll Number to search: ")
    if roll in students:
        print(f"✅ Found: {students[roll]}")
    else:
        print("❌ Student not found")

def update_student():
    roll = input("Enter Roll Number to update: ")
    if roll in students:
        new_name = input("Enter new name: ")
        students[roll] = new_name
        print("✅ Record updated")
    else:
        print("❌ Roll number not found")

def delete_student():
    roll = input("Enter Roll Number to delete: ")
    if roll in students:
        del students[roll]
        print("✅ Record deleted")
    else:
        print("❌ Roll number not found")

# Main Menu
while True:
    print("\n===== College Roll Management =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        print("Exiting program...")
        break
    else:
        print("Invalid choice!")