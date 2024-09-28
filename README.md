
# Student Management System

A **Terminal-based Student Management System** built using **Python** and **MySQL**. This system allows you to efficiently manage student information with features such as adding, updating, deleting, and searching for student records.

## Features

- **Add New Student**: Add a new student's details to the system.
- **Update Student Record**: Update any field for an existing student.
- **Delete Student Record**: Safely delete a student record after verification.
- **Search Student Record**: Search for a student by their ID.
- **Display All Students**: View all student records in a neatly formatted table.

## Database Structure

The student data is stored in a MySQL database with the following fields:

- `student_id`: Unique identifier for each student.
- `name`: Student's name.
- `class_section`: Class and section of the student.
- `admission_no`: Admission number.
- `dob`: Date of birth (in `YYYY-MM-DD` format).
- `mother_name`: Student's mother's name.
- `father_name`: Student's father's name.
- `phone_no`: Parent's contact number.
- `address`: Home address.

## Prerequisites

To run the project on your local machine, you need to have the following installed:

1. **Python 3.x**
2. **MySQL** (Ensure MySQL server is running)

You'll also need to install the following Python packages:

```bash
pip install mysql-connector-python
```

## Setup

### 1. Clone the Repository
Clone this repository to your local machine:

```bash
git clone https://github.com/AnujYadav-Dev/student-management-system.git
cd student-management-system
```

### 2. Create the MySQL Database
Create a MySQL database and a `students` table:

```sql
CREATE DATABASE student_management;

USE student_management;

CREATE TABLE students (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100),
    class_section VARCHAR(10),
    admission_no VARCHAR(20),
    dob DATE,
    mother_name VARCHAR(100),
    father_name VARCHAR(100),
    phone_no VARCHAR(15),
    address VARCHAR(255)
);
```

### 3. Configure Database Connection
In the Python code, update the `connect_db` function with your MySQL connection details:

```python
def connect_db():
    return mysql.connector.connect(
        host='localhost',
        database='student_management',
        user='your_mysql_user',
        password='your_mysql_password'
    )
```

### 4. Run the Program
Execute the main Python script to start the terminal-based student management system:

```bash
python student_management.py
```

## How to Use

1. After running the script, you will be prompted with a menu to **add**, **update**, **delete**, **search**, or **display** student records.
2. Follow the on-screen instructions for each option.
3. The program handles exceptions such as invalid inputs and non-existent records.

### Example Operations:

#### Add a Student:

```bash
Enter student name: Anuj Yadav
Enter class & section: 5A
Enter admission number: 12345
Enter date of birth (YYYY-MM-DD): 2005-12-08
Enter mother's name: Jane Yadav
Enter father's name: Jack Yadav
Enter phone number: 1234567890
Enter address: 123 Main St
```

#### Update a Student Record:

```bash
Enter the Student ID to update: 3
Which field would you like to update?
1. Name
2. Class & Section
3. Admission No
4. Date of Birth (YYYY-MM-DD)
5. Mother's Name
6. Father's Name
7. Phone No.
8. Address
Enter the number corresponding to the field: 2
Enter new value for Class & Section: 6B
Class & Section updated successfully.
```

#### Delete a Student Record:

```bash
Enter the Student ID to delete: 5
No student found with Student ID 5.
```

## Exception Handling

- If an invalid Student ID is entered for update or deletion, a message will alert the user.
- Input validations are in place for various fields such as date and phone number.
  
## Future Improvements

- Add a graphical user interface (GUI) to improve the user experience.
- Implement user authentication for enhanced security.
- Add more search features (e.g., search by name, class, or phone number).

## Contributions

Contributions are welcome! Feel free to fork this repository, make improvements, and submit a pull request.

---

**Happy Coding!**
