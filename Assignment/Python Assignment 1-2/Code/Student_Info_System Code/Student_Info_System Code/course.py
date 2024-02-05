class Course:
    def __init__(self, course_id, course_name, course_code, instructor_name):
        self.course_id = course_id
        self.course_name = course_name
        self.course_code = course_code
        self.instructor_name = instructor_name
        self.teacher = None
        self.enrollments = []           # List to store Enrollment objects
    def assign_teacher(self, teacher):
        self.teacher = teacher
        teacher.assigned_courses.append(self)
        print(f"{teacher.first_name} {teacher.last_name} assigned to teach {self.course_name}.")
    def update_course_info(self, course_code, course_name, instructor):
        self.course_code = course_code
        self.course_name = course_name
        self.instructor_name = instructor
        print(f"Course information updated for {self.course_name}.")
    def display_course_info(self):
        print(f"Course ID: {self.course_id}")
        print(f"Course Name: {self.course_name}")
        print(f"Course Code: {self.course_code}")
        print(f"Instructor: {self.instructor_name}")
    def get_enrollments(self):
        return self.enrollments
    def get_teacher(self):
        return self.teacher
