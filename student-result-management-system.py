import json
import os

FILE_NAME = "students.json"

# Load data
def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

# Save data
def save_data(data):
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)

# Calculate grade
def calculate_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 75:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 50:
        return "C"
    else:
        return "Fail"

# Add student
def add_student():
    data = load_data()
    roll = input("Enter Roll Number: ")
    name = input("Enter Name: ")

    marks = []
    for i in range(3):
        mark = float(input(f"Enter marks for subject {i+1}: "))
        marks.append(mark)

    total = sum(marks)
    average = total / len(marks)
    grade = calculate_grade(average)

    student = {
        "roll": roll,
        "name": name,
        "marks": marks,
        "total": total,
        "average": average,
        "grade": grade
    }

    data.append(student)
    save_data(data)
    print("✅ Student added successfully!\n")

# View all students
def view_students():
    data = load_data()
    if not data:
        print("No records found.\n")
        return

    for student in data:
        print("\n----------------------------")
        print("Roll:", student["roll"])
        print("Name:", student["name"])
        print("Marks:", student["marks"])
        print("Total:", student["total"])
        print("Average:", student["average"])
        print("Grade:", student["grade"])
    print("----------------------------\n")

# Search student
def search_student():
    data = load_data()
    roll = input("Enter Roll Number to search: ")

    for student in data:
        if student["roll"] == roll:
            print("\nStudent Found!")
            print(student)
            return
    print("❌ Student not found.\n")

# Delete student
def delete_student():
    data = load_data()
    roll = input("Enter Roll Number to delete: ")

    new_data = [student for student in data if student["roll"] != roll]

    if len(new_data) == len(data):
        print("❌ Student not found.\n")
    else:
        save_data(new_data)
        print("✅ Student deleted successfully!\n")

# Main menu
def main():
    while True:
        print("===== Student Result Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice!\n")

if __name__ == "__main__":
    main()
