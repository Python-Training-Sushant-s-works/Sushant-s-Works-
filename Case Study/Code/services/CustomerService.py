# CustomerService.py
from ICustomerService import ICustomerService
from InvalidInputException import InvalidInputException
from DatabaseConnectionException import DatabaseConnectionException

class CustomerService(ICustomerService):
    def __init__(self, connector):
        self.connector = connector

    def get_customer_by_id(self, customer_id):
        try:
            query = "SELECT * FROM customers WHERE CustomerID = %s"
            result = self.connector.execute_query(query, (customer_id,), fetch_one=True)
            if result:
                customer_data = result
                print(f"Customer found with ID {customer_id}: {customer_data}")
                return customer_data  # Return the customer data
            else:
                print(f"No customer found with ID {customer_id}")
                return None
        except Exception as e:
            print(f"Error: {e}")
            return None

    def get_customer_by_username(self, username):
        try:
            query = "SELECT * FROM customers WHERE Username = %s"
            result = self.connector.execute_query(query, (username,), fetch_one=True)
            if result:
                customer_data = result
                print(f"Customer found with username {username}: {customer_data}")
            else:
                print(f"No customer found with username {username}")
        except Exception as e:
            print(f"Error: {e}")

    def save_to_database(self, customer_data, connector):
        print(customer_data)
        try:
            self.connector.execute_query("""
                INSERT INTO customers
                (CustomerID,FirstName, LastName, Email, PhoneNumber, Address, Username, Password, RegistrationDate)
                VALUES (%s,%s, %s, %s, %s, %s, %s, %s, %s)
            """, [*customer_data])
            print("Customer data saved to database.")
        except Exception as e:
            print(f"Error: {e}")

    def update_customer(self, customer_id, updated_customer):
        try:


            query = """
                UPDATE customers
                SET FirstName=%s, LastName=%s, Email=%s, PhoneNumber=%s, Address=%s, Password=%s, RegistrationDate=%s
                WHERE CustomerID=%s
            """
            params = (
                updated_customer["FirstName"],
                updated_customer["LastName"],
                updated_customer["Email"],
                updated_customer["PhoneNumber"],
                updated_customer["Address"],
                updated_customer["Password"],
                updated_customer["RegistrationDate"],
                customer_id,
            )
            self.connector.execute_query(query, params)
            print(f"Customer with ID {customer_id} updated successfully.")

        except Exception as e:
            raise DatabaseConnectionException(str(e))

    def delete_customer(self, customer_id):
        try:
            reservations = self.connector.execute_query("SELECT * FROM reservations WHERE CustomerID = %s", (customer_id,), fetch_all=True)
            if reservations:
                for reservation in reservations:
                    reservation_id = reservation[0]
                    self.connector.execute_query("DELETE FROM reservations WHERE ReservationID = %s", (reservation_id,))
            self.connector.execute_query("DELETE FROM customers WHERE CustomerID = %s", (customer_id,))
            print(f"Customer with ID {customer_id} deleted successfully.")
        except Exception as e:
            print(f"Error: {e}")
