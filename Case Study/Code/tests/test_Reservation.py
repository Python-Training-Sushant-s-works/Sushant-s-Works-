import unittest
from DataConnector import DataConnector
from DataConnector import DataConnector
from ReservationService import ReservationService


class TestAddNewReservation(unittest.TestCase):
    def setUp(self):
        self.data_connector = DataConnector(host='localhost', user='root', password='Sushant@9546', database='carconnect1')
        self.data_connector.create_tables()
        self.reservation_service = ReservationService(self.data_connector)

    def tearDown(self):
        self.data_connector.connection.close()

    def test_add_new_reservation(self):
        new_reservation_data = {
            'ReservationID': 101,
            'CustomerID': 1,
            'VehicleID': 1,
            'StartDate': '2024-01-02',
            'EndDate': '2024-01-03',
            'TotalCost': 5642.00,
            'Status': 'Booked',
        }

        try:
            with self.reservation_service.create_reservation(new_reservation_data) as cursor:
                new_reservation_id = cursor.lastrowid

            added_reservation_result = self.reservation_service.get_reservation_by_id(new_reservation_id)
            added_reservation = Reservation(*added_reservation_result)

            self.assertIsNotNone(added_reservation)
            # ... (similar assertions as before)

        except Exception as e:
            self.fail(f"Exception raised: {e}")

if __name__ == '__main__':
    unittest.main()