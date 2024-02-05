from datetime import datetime
from enrollment import Enrollment
from payment import Payment
from DuplicateEnrollmentException import DuplicateEnrollmentException


class Student:
    def __init__(self, student_id, first_name, last_name, date_of_birth, email, phone_number):
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.email = email
        self.phone_number = phone_number
        self.enrollments = []     # List to store Enrollment objects
        self.payments = []

    def enroll_in_course(self, course):
        if self.is_student_already_enrolled(course):
            raise DuplicateEnrollmentException(self.student_id, course.course_id)

        enrollment_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        enrollment = Enrollment(len(self.enrollments) + 1, self, course, enrollment_date)
        self.enrollments.append(enrollment)
        course.enrollments.append(enrollment)
        print(f"{self.first_name} {self.last_name} enrolled in {course.course_name}.")

    # def update_student_info(self, first_name, last_name, date_of_birth, email, phone_number):

    def update_student_info(self, first_name, last_name, date_of_birth, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.email = email
        self.phone_number = phone_number
        print(f"Student information updated for {self.first_name} {self.last_name}.")
    def make_payment(self, amount, payment_date):
        payment = Payment(len(self.payments) + 1, self, amount, payment_date)
        self.payments.append(payment)
        print(f"Payment of ${amount} made by {self.first_name} {self.last_name} on {payment_date}.")
    def display_student_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Date of Birth: {self.date_of_birth}")
        print(f"Email: {self.email}")
        print(f"Phone Number: {self.phone_number}")

    def get_enrolled_courses(self):
        return [enrollment.course for enrollment in self.enrollments]

    def get_payment_history(self):
        return self.payments
