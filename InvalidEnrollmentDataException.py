class InvalidEnrollmentDataException(Exception):
    def __init__(self, message):
        super().__init__(message)