# exception/InvalidInputException.py

class InvalidInputException(Exception):
    def __init__(self, message="Invalid input data"):
        self.message = message
        super().__init__(self.message)
