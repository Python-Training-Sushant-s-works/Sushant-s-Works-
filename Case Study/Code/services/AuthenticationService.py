from AuthenticationException import AuthenticationException

class AuthenticationService:
    def authenticate(self, username, password):

        valid_username = "root"
        valid_password = "Sushant@9546"

        if username == valid_username and password == valid_password:
            return True
        else:
            raise AuthenticationException("Invalid username or password")
