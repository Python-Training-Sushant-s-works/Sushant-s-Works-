class CourseNotFoundException(Exception):
    def __init__(self, course_id):
        super().__init__(f"Course with ID {course_id} not found.")