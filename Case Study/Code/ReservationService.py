from IReservationService import IReservationService
import mysql.connector

class ReservationService(IReservationService):
    def __init__(self, connector):
        self.connector = connector
    def get_reservation_by_id(self, reservation_id):
        try:
            query = "SELECT * FROM reservations WHERE ReservationID = %s"
            result = self.connector.execute_query(query, (reservation_id,), fetch_one=True)
            if result:
                reservation_data = result
                print(f"Reservation found with ID {reservation_id}: {reservation_data}")
            else:
                print(f"No reservation found with ID {reservation_id}")
        except Exception as e:
            print(f"Error: {e}")
    def get_reservations_by_customer_id(self, customer_id):
        try:
            query = "SELECT * FROM reservations WHERE CustomerID = %s"
            result = self.connector.execute_query(query, (customer_id,), fetch_one=False)
            if result:
                customer_reservations = result
                print(f"Reservations for Customer ID {customer_id}:")
                for reservation in customer_reservations:
                    print(reservation)
            else:
                print(f"No reservations found for Customer ID {customer_id}")
        except Exception as e:
            print(f"Error: {e}")


    def create_reservation(self, reservation_data):
        try:

            customer_id_exists = self.verify_customer_exists(reservation_data[1])

            if customer_id_exists:
                self.connector.execute_query("""
                    INSERT INTO reservations
                    (ReservationID, CustomerID, VehicleID, StartDate, EndDate, TotalCost, Status)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, reservation_data)
                print("Reservation created successfully!")
            else:
                print(f"Customer with ID {reservation_data[1]} does not exist.")
        except Exception as e:
            print(f"Error: {e}")

    def verify_customer_exists(self, customer_id):
        try:
            query = "SELECT CustomerID FROM customers WHERE CustomerID = %s"
            result = self.connector.execute_query(query, (customer_id,), fetch_one=True)
            return result is not None
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return False

    def update_reservation(self, reservation_id, reservation_data):
        try:
            query = """
                UPDATE reservations
                SET CustomerID = %s, VehicleID = %s, StartDate = %s, EndDate = %s,
                    TotalCost = %s, Status = %s
                WHERE ReservationID = %s
            """
            self.connector.execute_query(query, reservation_data[1:] + (reservation_id,))
            print(f"Reservation with ID {reservation_id} updated successfully.")
        except Exception as e:
            print(f"Error: {e}")
    def cancel_reservation(self, reservation_id):
        try:
            query = "DELETE FROM reservations WHERE ReservationID = %s"
            self.connector.execute_query(query, (reservation_id,))
            print(f"Reservation with ID {reservation_id} canceled successfully.")
        except Exception as e:
            print(f"Error: {e}")


