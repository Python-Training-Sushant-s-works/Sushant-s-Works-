# exception/DatabaseConnectionException.py

class DatabaseConnectionException(Exception):
    def __init__(self, message="Database connection issue"):
        self.message = message
        super().__init__(self.message)
