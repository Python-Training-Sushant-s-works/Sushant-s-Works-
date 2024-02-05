from datetime import datetime
class Teacher:
    def __init__(self, teacher_id, first_name, last_name, email):
        self.teacher_id = teacher_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.assigned_courses = []

    def update_teacher_info(self, name, email, expertise):
        self.first_name = name
        self.email = email
        print(f"Teacher information updated for {self.first_name} {self.last_name}.")

    def display_teacher_info(self):
        print(f"Teacher ID: {self.teacher_id}")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Email: {self.email}")

    def get_assigned_courses(self):
        self.assigned_courses
        print(f"assigned_courses{self.assigned_courses}.")
