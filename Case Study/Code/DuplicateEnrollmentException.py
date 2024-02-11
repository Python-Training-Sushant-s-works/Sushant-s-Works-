class DuplicateEnrollmentException(Exception):
    def __init__(self, student_id, course_id):
        super().__init__(f"Student with ID {student_id} is already enrolled in course with ID {course_id}.")
