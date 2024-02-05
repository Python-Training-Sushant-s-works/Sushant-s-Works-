class InsufficientFundsException(Exception):
    def __init__(self, student_id):
        super().__init__(f"Insufficient funds for student with ID {student_id}.")
