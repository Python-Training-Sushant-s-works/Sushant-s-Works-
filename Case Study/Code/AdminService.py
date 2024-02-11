from IAdminService import IAdminService
class AdminService(IAdminService):
    def __init__(self, connector):
        self.connector = connector
    def get_admin_by_id(self, admin_id):
        try:
            query = "SELECT * FROM admins WHERE AdminID = %s"
            result = self.connector.execute_query(query, (admin_id,), fetch_one=True)
            if result:
                admin_data = result
                print(f"Admin found with ID {admin_id}: {admin_data}")
            else:
                print(f"No admin found with ID {admin_id}")
        except Exception as e:
            print(f"Error: {e}")
    def get_admin_by_username(self, username):
        try:
            query = "SELECT * FROM admins WHERE Username = %s"
            result = self.connector.execute_query(query, (username,), fetch_one=True)
            if result:
                admin_data = result
                print(f"Admin found with username {username}: {admin_data}")
            else:
                print(f"No admin found with username {username}")
        except Exception as e:
            print(f"Error: {e}")
    def register_admin(self, admin_data):
        try:
            self.connector.execute_query("""
                INSERT INTO admins
                (AdminID, FirstName, LastName, Email, PhoneNumber, Username, Password, Role, JoinDate)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, admin_data)
            print("Admin data saved to database.")
        except Exception as e:
            print(f"Error: {e}")
    def update_admin(self, admin_data):
        try:
            query = """
                UPDATE admins
                SET FirstName = %s, LastName = %s, Email = %s, PhoneNumber = %s,
                    Username = %s, Password = %s, Role = %s, JoinDate = %s
                WHERE AdminID = %s
            """
            self.connector.execute_query(query, admin_data[1:] + (admin_data[0],))
            print(f"Admin with ID {admin_data[0]} updated successfully.")
        except Exception as e:
            print(f"Error: {e}")
    def delete_admin(self, admin_id):
        try:
            query = "DELETE FROM admins WHERE AdminID = %s"
            self.connector.execute_query(query, (admin_id,))
            print(f"Admin with ID {admin_id} deleted successfully.")
        except Exception as e:
            print(f"Error: {e}")
