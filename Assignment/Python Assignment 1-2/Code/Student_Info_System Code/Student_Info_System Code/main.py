from datetime import datetime
from DatabaseConnector import DatabaseConnector
def get_date_input():
    while True:
        date_str = input("Enter of birth date (YYYY-MM-DD): ")
        try:
            return datetime.strptime(date_str, "%Y-%m-%d").strftime("%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please enter again.")
def perform_operations(db_connector):
    print("\n1. Add a New Student")
    print("2. Enroll Student in a Course")
    print("3. Assign Teacher to a Course")
    print("4. Make Payment")
    print("5. Display Student Information")
    print("6. Display Enrolled Courses")
    print("7. Add New Teacher")
    print("8. Display Payment History")
    print("9. Exit")

    choice = input("Enter your choice (1-10): ")

    if choice == '1':

        first_name = input("Enter student's first name: ")
        last_name = input("Enter student's last name: ")
        birth_date = get_date_input()
        email = input("Enter student's email: ")
        phone = input("Enter student's phone number: ")

        db_connector.insert_student(first_name, last_name, birth_date, email, phone)
        print("Student added successfully.")
    elif choice == '2':
        db_connector.insert_enrollment()
    elif choice == '3':
        db_connector.assign_teacher_to_course()
    elif choice == '4':
        db_connector.insert_payment()
    elif choice == '5':
        student_id = input("Enter student ID: ")
        student = db_connector.get_student_info(student_id)
        if student:
            student.display_student_info()
        else:
            print("Student not found.")
    elif choice == '6':
        student_id = input("Enter student ID: ")
        enrolled_courses = db_connector.get_enrolled_courses(student_id)
        print("\nEnrolled Courses:")
        for course in enrolled_courses:
            course.display_course_info()
    elif choice == '7':
        add_new_teacher(db_connector)
    elif choice == '8':
        student_id = input("Enter student ID: ")
        payment_history = db_connector.get_payment_history(student_id)
        print("\nPayment History:")
        for payment in payment_history:
            print(f"Payment ID: {payment.payment_id}, Amount: ${payment.get_payment_amount()}, Date: {payment.get_payment_date()}")

    elif choice == '9':
        print("Exiting the program.")
        db_connector.close_connection()
        exit()
    else:
        print("Invalid choice. Please enter a number between 1 and 10.")

def update_teacher_details(db_connector):
    teacher_id = input("Enter teacher ID to update details: ")

    check_teacher_query = "SELECT id FROM teachers WHERE id = %s"
    db_connector.cursor.execute(check_teacher_query, (teacher_id,))
    result = db_connector.cursor.fetchone()

    if result is None:
        print(f"Error: Teacher with ID {teacher_id} does not exist.")
        return

    new_name = input("Enter teacher's new name: ")
    new_email = input("Enter teacher's new email: ")
    new_assigned_courses = input("Enter teacher's assigned_courses: ")

    db_connector.update_teacher_info(teacher_id, new_name, new_email, new_assigned_courses)
    print("Teacher details updated successfully.")
def add_new_teacher(db_connector):

    first_name = input("Enter teacher's first name: ")
    last_name = input("Enter teacher's last name: ")
    email = input("Enter teacher's email: ")
    assigned_courses = input("Enter teacher's assigned_courses: ")

    db_connector.insert_teacher(first_name, last_name, email,assigned_courses)
    print("New teacher added successfully.")
def main():

    db_connector = DatabaseConnector(host='localhost', user='root', password='Sushant@95', database='SIS5')


    db_connector.create_tables()

    while True:
        perform_operations(db_connector)

if __name__ == "__main__":
    main()
