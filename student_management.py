import mysql.connector
from mysql.connector import Error

# Connect to MySQL Database
def connect_db():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='student_management',
            user='root',  # Replace with your MySQL username
            password='Alpha01'  # Replace with your MySQL password
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print("Error while connecting to MySQL", e)

# Adding a new student record
def add_student():
    try:
        connection = connect_db()
        cursor = connection.cursor()

        name = input("Enter Name: ")
        class_section = input("Enter Class & Section: ")
        admission_no = input("Enter Admission No: ")
        dob = input("Enter Date of Birth (YYYY-MM-DD): ")
        mother_name = input("Enter Mother's Name: ")
        father_name = input("Enter Father's Name: ")
        phone_no = input("Enter Phone No.: ")
        address = input("Enter Address: ")

        query = """INSERT INTO students 
                   (name, class_section, admission_no, dob, mother_name, father_name, phone_no, address) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        values = (name, class_section, admission_no, dob, mother_name, father_name, phone_no, address)

        cursor.execute(query, values)
        connection.commit()

        print("Student added successfully.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Display all student records
def display_students():
    try:
        connection = connect_db()
        cursor = connection.cursor()

        query = "SELECT * FROM students"
        cursor.execute(query)
        result = cursor.fetchall()

        print("\n{:<10} {:<20} {:<10} {:<15} {:<15} {:<20} {:<20} {:<15} {:<30}".format(
            'ID', 'Name', 'Class', 'Admission No', 'DOB', 'Mother\'s Name', 'Father\'s Name', 'Phone', 'Address'))

        for row in result:
            # Convert the date to a string in YYYY-MM-DD format
            dob = row[4].strftime('%Y-%m-%d') if row[4] else 'N/A'

            # Ensure the column width for DOB is wide enough to display the date
            print("{:<10} {:<20} {:<10} {:<15} {:<15} {:<20} {:<20} {:<15} {:<30}".format(
                row[0], row[1], row[2], row[3], dob, row[5], row[6], row[7], row[8]))

    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


# Update student record
def update_student():
    try:
        connection = connect_db()
        cursor = connection.cursor()

        student_id = input("Enter the Student ID to update: ")

        # Check if the student exists in the database
        check_query = "SELECT * FROM students WHERE student_id = %s"
        cursor.execute(check_query, (student_id,))
        record = cursor.fetchone()

        if record is None:
            print(f"No student found with Student ID {student_id}.")
            return

        # If the record exists, proceed with asking which field to update
        print("\nWhich field would you like to update?")
        print("1. Name")
        print("2. Class & Section")
        print("3. Admission No")
        print("4. Date of Birth (YYYY-MM-DD)")
        print("5. Mother's Name")
        print("6. Father's Name")
        print("7. Phone No.")
        print("8. Address")
        choice = input("Enter the number corresponding to the field: ")

        field_map = {
            '1': 'name',
            '2': 'class_section',
            '3': 'admission_no',
            '4': 'dob',
            '5': 'mother_name',
            '6': 'father_name',
            '7': 'phone_no',
            '8': 'address'
        }

        if choice not in field_map:
            print("Invalid choice. Please try again.")
            return

        # Ask for the new value for the chosen field
        new_value = input(f"Enter new value for {field_map[choice].replace('_', ' ').title()}: ")

        # Prepare the update query
        query = f"UPDATE students SET {field_map[choice]} = %s WHERE student_id = %s"
        values = (new_value, student_id)

        cursor.execute(query, values)
        connection.commit()

        print(f"{field_map[choice].replace('_', ' ').title()} updated successfully.")

    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()


# Delete student record
def delete_student():
    try:
        connection = connect_db()
        cursor = connection.cursor()

        student_id = input("Enter the Student ID to delete: ")

        # Check if the student exists in the database
        check_query = "SELECT * FROM students WHERE student_id = %s"
        cursor.execute(check_query, (student_id,))
        record = cursor.fetchone()

        if record is None:
            print(f"No student found with Student ID {student_id}.")
            return

        # If the record exists, proceed with deletion
        confirmation = input(f"Are you sure you want to delete the record of {record[1]} (Y/N)? ").lower()
        if confirmation == 'y':
            delete_query = "DELETE FROM students WHERE student_id = %s"
            cursor.execute(delete_query, (student_id,))
            connection.commit()
            print("Student record deleted successfully.")
        else:
            print("Deletion canceled.")

    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Search student by admission number
def search_student():
    try:
        connection = connect_db()
        cursor = connection.cursor()

        admission_no = input("Enter the Admission Number to search: ")

        query = "SELECT * FROM students WHERE admission_no = %s"
        cursor.execute(query, (admission_no,))
        result = cursor.fetchall()

        if result:
            print("\n{:<10} {:<20} {:<10} {:<15} {:<12} {:<20} {:<20} {:<15} {:<30}".format(
                'ID', 'Name', 'Class', 'Admission No', 'DOB', 'Mother\'s Name', 'Father\'s Name', 'Phone', 'Address'))

            for row in result:
                print("{:<10} {:<20} {:<10} {:<15} {:<12} {:<20} {:<20} {:<15} {:<30}".format(
                    row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))
        else:
            print("No student found with this Admission Number.")
    except Error as e:
        print(f"Error: {e}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Main menu
def menu():
    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. Display Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Search Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            display_students()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            search_student()
        elif choice == '6':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

# Start the program
if __name__ == "__main__":
    menu()
