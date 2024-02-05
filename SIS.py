from datetime import datetime
#from Enrollment import Enrollment
#from Student import Student
#from Teacher import Teacher
#from Payment import Payment
class SIS:
    def __init__(self):
        self.students = []
        self.courses = []
        self.teachers = []
    def enroll_student_in_course(self, student, course):
        student.enroll_in_course(course)
        enrollment = Enrollment(student.student_id, course.course_id, datetime.now())
        course.enrollments.append(enrollment)
    def assign_teacher_to_course(self, teacher, course):
        course.assign_teacher(teacher)
        teacher.assigned_courses.append(course)
    def record_payment(self, student, amount, payment_date):
        payment = Payment(student.student_id, amount, payment_date)
        student.payments.append(payment)
    def generate_enrollment_report(self, course):
        print(f"Enrollment Report for Course {course.course_name}")
        for enrollment in course.enrollments:
            print(f"Student ID: {enrollment.student_id}, Enrollment Date: {enrollment.enrollment_date}")
    def generate_payment_report(self, student):
        print(f"Payment Report for Student {student.first_name} {student.last_name}")
        for payment in student.payments:
            print(f"Payment ID: {payment.payment_id}, Amount: {payment.amount}, Payment Date: {payment.payment_date}")
    def calculate_course_statistics(self, course):
        enrollment_count = len(course.enrollments)
        total_payments = sum([payment.amount for payment in course.enrollments[0].payments])
        print(f"Statistics for Course {course.course_name}")
        print(f"Number of Enrollments: {enrollment_count}")
        print(f"Total Payments: {total_payments}")

# Example usage:
sis_system = SIS()

# Assume you have instances of Student, Course, and Teacher classes
student1 = Student(1, "John", "Doe")
course1 = Course(1, "Math", "M101")
teacher1 = Teacher(1, "Sarah", "Smith")

# Enrolling a student in a course
sis_system.enroll_student_in_course(student1, course1)

# Assigning a teacher to a course
sis_system.assign_teacher_to_course(teacher1, course1)

# Recording a payment for a student
sis_system.record_payment(student1, 500, datetime.now())

# Generating reports
sis_system.generate_enrollment_report(course1)
sis_system.generate_payment_report(student1)

# Calculating course statistics
sis_system.calculate_course_statistics(course1)
