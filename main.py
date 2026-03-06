"""
Student Management System
Author: Karnan
Description: A CLI-based application to manage student records with CRUD operations
using file handling for persistent storage.
"""

import json
import os

DATA_FILE = "students.json"


def load_students():
    """Load student data from file."""
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)


def save_students(students):
    """Save student data to file."""
    with open(DATA_FILE, "w") as file:
        json.dump(students, file, indent=4)


def add_student(students):
    """Add a new student record."""
    student_id = input("Enter Student ID: ")
    name = input("Enter Student Name: ")
    age = input("Enter Age: ")
    grade = input("Enter Grade: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "grade": grade
    }

    students.append(student)
    save_students(students)
    print("Student added successfully.\n")


def view_students(students):
    """Display all student records."""
    if not students:
        print("No student records found.\n")
        return

    print("\nStudent Records:")
    for student in students:
        print(f"ID: {student['id']} | Name: {student['name']} | Age: {student['age']} | Grade: {student['grade']}")
    print()


def search_student(students):
    """Search for a student by ID."""
    student_id = input("Enter Student ID to search: ")
    for student in students:
        if student["id"] == student_id:
            print("Student Found:")
            print(student)
            return
    print("Student not found.\n")


def update_student(students):
    """Update an existing student record."""
    student_id = input("Enter Student ID to update: ")

    for student in students:
        if student["id"] == student_id:
            student["name"] = input("Enter new name: ")
            student["age"] = input("Enter new age: ")
            student["grade"] = input("Enter new grade: ")
            save_students(students)
            print("Student record updated.\n")
            return

    print("Student not found.\n")


def delete_student(students):
    """Delete a student record."""
    student_id = input("Enter Student ID to delete: ")

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            save_students(students)
            print("Student record deleted.\n")
            return

    print("Student not found.\n")


def main_menu():
    """Display the main menu."""
    students = load_students()

    while True:
        print("===== Student Management System =====")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            update_student(students)
        elif choice == "5":
            delete_student(students)
        elif choice == "6":
            print("Exiting system...")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main_menu()
