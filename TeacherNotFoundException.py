class TeacherNotFoundException(Exception):
    def __init__(self, teacher_id):
        super().__init__(f"Teacher with ID {teacher_id} not found.")