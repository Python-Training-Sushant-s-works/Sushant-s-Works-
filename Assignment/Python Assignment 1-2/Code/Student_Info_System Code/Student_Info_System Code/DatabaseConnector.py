import mysql.connector
from datetime import datetime
from student import Student
from course import Course
from payment import Payment
def get_date_input():
    while True:
        date_str = input("Enter date (YYYY-MM-DD): ")
        try:
            return datetime.strptime(date_str, "%Y-%m-%d").strftime("%Y-%m-%d")
        except ValueError:
            print("Invalid date format. Please enter again.")
class DatabaseConnector:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.connection.cursor()

    def execute_query(self, query, values=None):
        try:
            self.cursor.execute(query, values)
            self.connection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.connection.rollback()

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

    def create_tables(self):
        def create_tables(self):
            student_table_query = """
            CREATE TABLE IF NOT EXISTS students (
                id INT AUTO_INCREMENT PRIMARY KEY,
                first_name VARCHAR(255) NOT NULL,
                last_name VARCHAR(255) NOT NULL,
                birth_date DATE NOT NULL,
                email VARCHAR(255) NOT NULL,
                phone VARCHAR(20) NOT NULL
            );
            """
            course_table_query = """
            CREATE TABLE IF NOT EXISTS courses (
                id INT AUTO_INCREMENT PRIMARY KEY,
                course_name VARCHAR(255) NOT NULL,
                course_code VARCHAR(20) NOT NULL,
                instructor VARCHAR(255) NOT NULL
            );
            """
            teacher_table_query = """
            CREATE TABLE IF NOT EXISTS teachers (
                id INT AUTO_INCREMENT PRIMARY KEY,
                first_name VARCHAR(255) NOT NULL,
                last_name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                assigned_courses Varchar(255) Not null
            );
            """
            payment_table_query = """
            CREATE TABLE IF NOT EXISTS payments (
                id INT AUTO_INCREMENT PRIMARY KEY,
                student_id INT NOT NULL,
                amount FLOAT NOT NULL,
                payment_date DATE NOT NULL,
                FOREIGN KEY (student_id) REFERENCES students(id)
            );
            """
            enrollment_table_query = """
            CREATE TABLE IF NOT EXISTS enrollments (
                id INT AUTO_INCREMENT PRIMARY KEY,
                student_id INT NOT NULL,
                course_id INT NOT NULL,
                enrollment_date DATE NOT NULL,
                FOREIGN KEY (student_id) REFERENCES students(id),
                FOREIGN KEY (course_id) REFERENCES courses(id)
            );
            """

    def insert_enrollment(self):
        student_id = input("Enter student ID for enrollment: ")

        check_student_query = "SELECT id FROM students WHERE id = %s"
        self.cursor.execute(check_student_query, (student_id,))
        result = self.cursor.fetchone()

        if result is None:
            print(f"Error: Student with ID {student_id} does not exist.")
            return

        course_id = input("Enter course ID for enrollment: ")

        check_course_query = "SELECT id FROM courses WHERE id = %s"
        self.cursor.execute(check_course_query, (course_id,))
        result = self.cursor.fetchone()

        if result is None:
            print(f"Error: Course with ID {course_id} does not exist.")
            return

        enrollment_date = get_date_input()

        query = """
        INSERT INTO enrollments (student_id, course_id, enrollment_date)
        VALUES (%s, %s, %s);
        """
        values = (student_id, course_id, enrollment_date)
        self.execute_query(query, values)
        print("Enrollment successful.")

    def assign_teacher_to_course(self):
        course_id = input("Enter course ID: ")
        teacher_id = input("Enter teacher ID: ")

        check_course_query = "SELECT id FROM courses WHERE id = %s"
        self.cursor.execute(check_course_query, (course_id,))
        result_course = self.cursor.fetchone()

        check_teacher_query = "SELECT id FROM teachers WHERE id = %s"
        self.cursor.execute(check_teacher_query, (teacher_id,))
        result_teacher = self.cursor.fetchone()

        if result_course is None:
            print(f"Error: Course with ID {course_id} does not exist.")
            return
        if result_teacher is None:
            print(f"Error: Teacher with ID {teacher_id} does not exist.")
            return
        update_course_query = "UPDATE courses SET instructor = %s WHERE id = %s"
        values = (teacher_id, course_id)
        self.execute_query(update_course_query, values)
        print("Teacher assigned to the course.")

    def insert_payment(self):
        student_id = input("Enter student ID for payment: ")
        amount = float(input("Enter payment amount: "))
        payment_date = get_date_input()
        check_student_query = "SELECT id FROM students WHERE id = %s"
        self.cursor.execute(check_student_query, (student_id,))
        result = self.cursor.fetchone()

        if result is None:
            print(f"Error: Student with ID {student_id} does not exist.")
            return
        query = """
        INSERT INTO payments (student_id, amount, payment_date)
        VALUES (%s, %s, %s);
        """
        values = (student_id, amount, payment_date)
        self.execute_query(query, values)
        print("Payment recorded successfully.")

    def get_student_info(self, student_id):

        check_student_query = "SELECT * FROM students WHERE id = %s"
        self.cursor.execute(check_student_query, (student_id,))
        result = self.cursor.fetchone()

        if result is None:
            print(f"Error: Student with ID {student_id} does not exist.")
            return None

        student_info = Student(result[0], result[1], result[2], result[3], result[4], result[5])
        return student_info
    def get_payment_history(self, student_id):

        query = """
            SELECT payments.id, payments.amount, payments.payment_date
            FROM payments
            WHERE payments.student_id = %s;
        """
        self.cursor.execute(query, (student_id,))
        payment_history_data = self.cursor.fetchall()

        payment_history = []
        for payment_data in payment_history_data:
            payment = Payment(*payment_data)
            payment_history.append(payment)

        return payment_history

    def get_enrolled_courses(self, student_id):

        query = """
            SELECT courses.course_id, courses.course_name, courses.course_code, courses.instructor_name
            FROM enrollments
            JOIN courses ON enrollments.course_id = courses.course_id
            WHERE enrollments.student_id = %s;
        """

        self.cursor.execute(query, (student_id,))
        enrolled_courses_data = self.cursor.fetchall()

        enrolled_courses = []
        for course_data in enrolled_courses_data:
            course = Course(*course_data)
            enrolled_courses.append(course)

        return enrolled_courses
    def insert_student(self, first_name, last_name, birth_date, email, phone):
        query = """
        INSERT INTO students (first_name, last_name, birth_date, email, phone)
        VALUES (%s, %s, %s, %s, %s);
        """
        values = (first_name, last_name, birth_date, email, phone)
        self.execute_query(query, values)
        print("Student added successfully.")
    def insert_teacher(self, first_name, last_name, email, assigned_courses):
        try:

            query = "INSERT INTO teachers (first_name, last_name, email, assigned_courses) VALUES (%s, %s, %s, %s)"
            values = (first_name, last_name, email, assigned_courses)
            self.cursor.execute(query, values)
            self.connection.commit()
        except Exception as e:
            print(f"Error inserting teacher: {e}")

