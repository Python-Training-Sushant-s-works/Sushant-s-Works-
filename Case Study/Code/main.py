# main.py

from Customer import Customer
from Vehicle import Vehicle
from Reservation import Reservation
from Admin import Admin
from CustomerService import CustomerService
from VehicleService import VehicleService
from ReservationService import ReservationService
from AdminService import AdminService
from DataConnector import DataConnector

def main():
    connector = DataConnector(host='localhost', user='root', password='Sushant@9546', database='carconnect1')

    customer_service = CustomerService(connector)
    vehicle_service = VehicleService(connector)
    reservation_service = ReservationService(connector)
    admin_service = AdminService(connector)

    connector.create_tables()

    while True:
        print("\nChoose an option:")
        print("1. Register Customer")
        print("2. Add Vehicle")
        print("3. Insert Reservation")
        print("4. Register Admin")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            while True:
                print("\nCustomer Options:")
                print("1. Register New Customer")
                print("2. Update Customer")
                print("3. Delete Customer")
                print("4. Go Back")

                customer_choice = input("Enter your choice (1-4): ")

                if customer_choice == '1':
                    new_customer = Customer()
                    new_customer.get_input_from_user()
                    customer_service.save_to_database(new_customer.get_data_for_database(), connector)
                    print("Customer registered successfully!")
                elif customer_choice == '2':
                    customer_id = input("Enter Customer ID to update: ")
                    updated_customer = Customer()
                    updated_customer.get_input_from_user()
                    customer_service.update_customer(customer_id, updated_customer.get_data_for_database())
                    print("Customer updated successfully!")
                elif customer_choice == '3':
                    customer_id = input("Enter Customer ID to delete: ")
                    customer_service.delete_customer(customer_id)
                    print("Customer deleted successfully!")
                elif customer_choice == '4':
                    break
                else:
                    print(" Please enter a number between 1 and 4.")

        elif choice == '2':
            while True:
                print("\nVehicle Options:")
                print("1. Add New Vehicle")
                print("2. Update Vehicle")
                print("3. Remove Vehicle")
                print("4. Go Back")

                vehicle_choice = input("Enter your choice (1-4): ")

                if vehicle_choice == '1':
                    new_vehicle = Vehicle()
                    new_vehicle.get_input_from_user()
                    vehicle_service.add_vehicle(new_vehicle.get_data_for_database())
                    print("Vehicle added successfully!")
                if vehicle_choice == '2':
                    vehicle_id = input("Enter Vehicle ID to update: ")
                    updated_vehicle = Vehicle()
                    updated_vehicle.get_input_from_user()
                    vehicle_service.update_vehicle(vehicle_id, updated_vehicle)
                    print("Vehicle updated successfully!")
                elif vehicle_choice == '3':
                    vehicle_id = input("Enter Vehicle ID to remove: ")
                    vehicle_service.remove_vehicle(vehicle_id)
                    print("Vehicle removed successfully!")
                elif vehicle_choice == '4':
                    break
                else:
                    print(" Please enter a number between 1 and 4.")

        elif choice == '3':
            while True:
                print("\nReservation Options:")
                print("1. Create New Reservation")
                print("2. Update Reservation")
                print("3. Cancel Reservation")
                print("4. Go Back")

                reservation_choice = input("Enter your choice (1-4): ")

                if reservation_choice == '1':
                    new_reservation = Reservation()
                    new_reservation.get_input_from_user()
                    reservation_service.create_reservation(new_reservation.get_data_for_database())
                    print("Reservation created successfully!")
                elif reservation_choice == '2':
                    reservation_id = input("Enter Reservation ID to update: ")
                    updated_reservation = Reservation()
                    updated_reservation.get_input_from_user()
                    reservation_service.update_reservation(reservation_id, updated_reservation.get_data_for_database())
                    print("Reservation updated successfully!")
                elif reservation_choice == '3':
                    reservation_id = input("Enter Reservation ID to cancel: ")
                    reservation_service.cancel_reservation(reservation_id)
                    print("Reservation canceled successfully!")
                elif reservation_choice == '4':
                    break
                else:
                    print(" Please enter a number between 1 and 4.")

        elif choice == '4':
            while True:
                print("\nAdmin Options:")
                print("1. Register New Admin")
                print("2. Update Admin")
                print("3. Delete Admin")
                print("4. Go Back")

                admin_choice = input("Enter your choice (1-4): ")

                if admin_choice == '1':
                    new_admin = Admin()
                    new_admin.get_input_from_user()
                    admin_service.register_admin(new_admin.get_data_for_database())
                    print("Admin registered successfully!")
                elif admin_choice == '2':
                    admin_id = input("Enter Admin ID to update: ")
                    updated_admin = Admin()
                    updated_admin.get_input_from_user()
                    admin_service.update_admin(admin_id, updated_admin.get_data_for_database())
                    print("Admin updated successfully!")
                elif admin_choice == '3':
                    admin_id = input("Enter Admin ID to delete: ")
                    admin_service.delete_admin(admin_id)
                    print("Admin deleted successfully!")
                elif admin_choice == '4':
                    break
                else:
                    print(" Please enter a number between 1 and 4.")

        elif choice == '5':
            break
        else:
            print(" Please enter a number between 1 and 5.")

    connector.close_connection()

if __name__ == "__main__":
    main()
