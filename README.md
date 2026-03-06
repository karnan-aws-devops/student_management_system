# Student Management System (Python)

## Overview

The **Student Management System** is a command-line based Python application designed to manage student records efficiently.
It allows users to perform essential operations such as adding, viewing, searching, updating, and deleting student information.
The system uses **JSON file handling** to store student data, ensuring that records are preserved even after the program is closed.

## Features

* Add new student records
* View all stored student records
* Search student details using Student ID
* Update existing student information
* Delete student records
* Persistent data storage using JSON
* Simple and user-friendly command-line interface

## Technologies Used

* Python
* JSON (for data storage)
* File Handling
* Command Line Interface (CLI)

## Project Structure

student-management-system
│
├── main.py
├── students.json
└── README.md

## How the Application Works

1. When the program starts, it loads existing student data from the **students.json** file.
2. The user interacts with a menu-driven interface to perform various operations.
3. Any changes made to student records are automatically saved to the JSON file.
4. This ensures the data remains available for future program executions.

## Installation and Usage

### Step 1: Clone the repository

git clone https://github.com/yourusername/student-management-system.git

### Step 2: Navigate to the project directory

cd student-management-system

### Step 3: Run the program

python main.py

## Example Menu

===== Student Management System =====

1. Add Student
2. View Students
3. Search Student
4. Update Student
5. Delete Student
6. Exit

## Learning Outcomes

This project helped strengthen knowledge in:

* Python programming fundamentals
* CRUD operations
* File handling and JSON data storage
* Data structures such as lists and dictionaries
* Writing modular and structured Python programs

## Author

Karnan
