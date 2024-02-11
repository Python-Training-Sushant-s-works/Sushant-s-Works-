from IVehicleService import IVehicleService
class VehicleService(IVehicleService):
    def __init__(self, connector):
        self.connector = connector
    def get_vehicle_by_id(self, vehicle_id):
        try:
            query = "SELECT * FROM vehicles WHERE VehicleID = %s"
            result = self.connector.execute_query(query, (vehicle_id,), fetch_one=True)
            if result:
                vehicle_data = result
                print(f"Vehicle found with ID {vehicle_id}: {vehicle_data}")
            else:
                print(f"No vehicle found with ID {vehicle_id}")
        except Exception as e:
            print(f"Error: {e}")
    def get_available_vehicles(self):
        try:
            query = "SELECT * FROM vehicles WHERE Availability = 'Available'"
            result = self.connector.execute_query(query, fetch_one=False)
            if result:
                available_vehicles = result
                print("Available Vehicles:")
                for vehicle in available_vehicles:
                    print(vehicle)
            else:
                print("No available vehicles.")
        except Exception as e:
            print(f"Error: {e}")
    def add_vehicle(self, vehicle_data):
        try:
            self.connector.execute_query("""
                INSERT INTO vehicles
                (VehicleID, Model, Make, Year, Color, RegistrationNumber, Availability, DailyRate)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, vehicle_data)
            print("Vehicle data saved to database.")
        except Exception as e:
            print(f"Error: {e}")

    def update_vehicle(self, vehicle_id, updated_vehicle_data):
        print(updated_vehicle_data)
        try:
            query = """
                UPDATE vehicles
                SET Model = %s, Make = %s, Year = %s, Color = %s,
                    RegistrationNumber = %s, Availability = %s, DailyRate = %s
                WHERE VehicleID = %s
            """
            updated_values = updated_vehicle_data.get_data_for_database() + (vehicle_id,)
            self.connector.execute_query(query, updated_values)
            print(f"Vehicle with ID {vehicle_id} updated successfully.")
        except Exception as e:
            print(f"Error: {e}")

    def remove_vehicle(self, vehicle_id):
        try:
            reservations_query = "SELECT ReservationID FROM reservations WHERE VehicleID = %s"
            reservations = self.connector.execute_query(reservations_query, (vehicle_id,), fetch_one=False)

            if reservations:
                for reservation in reservations:
                    reservation_id = reservation['ReservationID']
                    self.connector.execute_query("DELETE FROM reservations WHERE ReservationID = %s", (reservation_id,))

            vehicle_removal_query = "DELETE FROM vehicles WHERE VehicleID = %s"
            self.connector.execute_query(vehicle_removal_query, (vehicle_id,))
            print(f"Vehicle with ID {vehicle_id} removed successfully.")
        except Exception as e:
            print(f"Error: {e}")
