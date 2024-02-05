import mysql.connector
class DatabaseConnector:
    def __init__(self):
        self.connection = None
    def open_connection(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Sushant@9546",
            database="techshopdbb"
        )
        self.create_database()
        self.create_tables()
    def close_connection(self):
        if self.connection:
            self.connection.close()
    def create_database(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute("CREATE DATABASE IF NOT EXISTS techshopdb")
            self.connection.database = "techshopdb"
        except Exception as e:
            print(f"Error creating database: {e}")
        finally:
            cursor.close()

    def create_tables(self):
        cursor = self.connection.cursor()
        try:
            # Create Customers table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Customers (
                    CustomerID INT AUTO_INCREMENT PRIMARY KEY,
                    FirstName VARCHAR(255),
                    LastName VARCHAR(255),
                    Email VARCHAR(255) UNIQUE,
                    Phone VARCHAR(20),
                    Address VARCHAR(255)
                )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Products (
                    ProductID INT AUTO_INCREMENT PRIMARY KEY,
                    ProductName VARCHAR(255),
                    Description TEXT,
                    Price DECIMAL(10, 2)
                )
            """)


            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Orders (
                    OrderID INT AUTO_INCREMENT PRIMARY KEY,
                    CustomerID INT,
                    OrderDate DATE,
                    TotalAmount DECIMAL(10, 2),
                    OrderStatus VARCHAR(255),
                    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
                )
            """)


            cursor.execute("""
                CREATE TABLE IF NOT EXISTS OrderDetails (
                    OrderDetailID INT AUTO_INCREMENT PRIMARY KEY,
                    OrderID INT,
                    ProductID INT,
                    Quantity INT,
                    FOREIGN KEY (OrderID) REFERENCES Orders(OrderID),
                    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
                )
            """)

            cursor.execute("""
                CREATE TABLE IF NOT EXISTS Inventory (
                    InventoryID INT AUTO_INCREMENT PRIMARY KEY,
                    ProductID INT,
                    QuantityInStock INT,
                    LastStockUpdate DATE,
                    FOREIGN KEY (ProductID) REFERENCES Products(ProductID)
                )
            """)
        except Exception as e:
            print(f"Error creating tables: {e}")
        finally:
            cursor.close()

    def insert_customer(self, first_name, last_name, email, phone, address):
        cursor = self.connection.cursor()
        try:
            query = "INSERT INTO Customers (FirstName, LastName, Email, Phone, Address) VALUES (%s, %s, %s, %s, %s)"
            values = (first_name, last_name, email, phone, address)
            cursor.execute(query, values)
            self.connection.commit()
            print("Customer inserted successfully.")
        except Exception as e:
            print(f"Error inserting customer: {e}")
        finally:
            cursor.close()

    def insert_product(self, product_name, description, price):
        cursor = self.connection.cursor()
        try:
            query = "INSERT INTO Products (ProductName, Description, Price) VALUES (%s, %s, %s)"
            values = (product_name, description, price)
            cursor.execute(query, values)
            self.connection.commit()
            print("Product inserted successfully.")
        except Exception as e:
            print(f"Error inserting product: {e}")
        finally:
            cursor.close()

    def insert_order(self, customer_id, order_date, total_amount, order_status):
        cursor = self.connection.cursor()
        try:
            query = "INSERT INTO Orders (CustomerID, OrderDate, TotalAmount, OrderStatus) VALUES (%s, %s, %s, %s)"
            values = (customer_id, order_date, total_amount, order_status)
            cursor.execute(query, values)
            self.connection.commit()
            print("Order inserted successfully.")
        except Exception as e:
            print(f"Error inserting order: {e}")
        finally:
            cursor.close()

    def insert_order_detail(self, order_id, product_id, quantity):
        cursor = self.connection.cursor()
        try:
            query = "INSERT INTO OrderDetails (OrderID, ProductID, Quantity) VALUES (%s, %s, %s)"
            values = (order_id, product_id, quantity)
            cursor.execute(query, values)
            self.connection.commit()
            print("Order detail inserted successfully.")
        except Exception as e:
            print(f"Error inserting order detail: {e}")
        finally:
            cursor.close()

    def insert_inventory(self, product_id, quantity_in_stock, last_stock_update):
        cursor = self.connection.cursor()
        try:
            query = "INSERT INTO Inventory (ProductID, QuantityInStock, LastStockUpdate) VALUES (%s, %s, %s)"
            values = (product_id, quantity_in_stock, last_stock_update)
            cursor.execute(query, values)
            self.connection.commit()
            print("Inventory inserted successfully.")
        except Exception as e:
            print(f"Error inserting inventory: {e}")
        finally:
            cursor.close()

db_connector = DatabaseConnector()
db_connector.open_connection()

db_connector.close_connection()
