import mysql.connector
class DataConnector:
    def __init__(self, host, user, password, database):
        self.connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,

            database=database
        )
        self.cursor = self.connection.cursor()
    def create_tables(self):
        create_tables_queries = [
            """
            CREATE TABLE IF NOT EXISTS customers (
                CustomerID INT AUTO_INCREMENT PRIMARY KEY,
                FirstName VARCHAR(255),
                LastName VARCHAR(255),
                Email VARCHAR(255),
                PhoneNumber VARCHAR(15),
                Address VARCHAR(255),
                Username VARCHAR(255),
                Password VARCHAR(255),
                RegistrationDate DATE
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS vehicles (
                VehicleID INT AUTO_INCREMENT PRIMARY KEY,
                Model VARCHAR(255),
                Make VARCHAR(255),
                Year INT,
                Color VARCHAR(255),
                RegistrationNumber VARCHAR(255),
                Availability BOOLEAN,
                DailyRate FLOAT
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS reservations (
                ReservationID INT AUTO_INCREMENT PRIMARY KEY,
                CustomerID INT,
                VehicleID INT,
                StartDate DATE,
                EndDate DATE,
                TotalCost FLOAT,
                Status VARCHAR(255),
                FOREIGN KEY (CustomerID) REFERENCES customers(CustomerID),
                FOREIGN KEY (VehicleID) REFERENCES vehicles(VehicleID)
            );
            """,
            """
            CREATE TABLE IF NOT EXISTS admins (
                AdminID INT AUTO_INCREMENT PRIMARY KEY,
                FirstName VARCHAR(255),
                LastName VARCHAR(255),
                Email VARCHAR(255),
                PhoneNumber VARCHAR(15),
                Username VARCHAR(255),
                Password VARCHAR(255),
                Role VARCHAR(255),
                JoinDate DATE
            );
            """
        ]
        try:
            for query in create_tables_queries:
                self.cursor.execute(query)
            self.connection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def execute_query(self, query, values=None, fetch_one=False):
        try:
            if values:
                self.cursor.execute(query, values)
            else:
                self.cursor.execute(query)

            if fetch_one:
                return self.cursor.fetchone()
            else:
                self.connection.commit()
                return self.cursor.fetchall()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.cursor.execute("""
                INSERT INTO customers
                (FirstName, LastName, Email, PhoneNumber, Address, Username, Password, RegistrationDate)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, customer_data)


    def insert_user_input_data(self, customer_data, vehicle_data, reservation_data, admin_data):
        try:
            # Insert customer data
            self.cursor.execute("""
                INSERT INTO customers
                (FirstName, LastName, Email, PhoneNumber, Address, Username, Password, RegistrationDate)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, customer_data)
            self.cursor.execute("""
                INSERT INTO vehicles
                (Model, Make, Year, Color, RegistrationNumber, Availability, DailyRate)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, vehicle_data)
            self.cursor.execute("""
                INSERT INTO reservations
                (CustomerID, VehicleID, StartDate, EndDate, TotalCost, Status)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, reservation_data)
            self.cursor.execute("""
                INSERT INTO admins
                (FirstName, LastName, Email, PhoneNumber, Username, Password, Role, JoinDate)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """, admin_data)
            self.connection.commit()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
