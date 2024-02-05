from Customers import Customers
from Products import Products
from Orders import Orders
from OrderDetails import OrderDetails
from Inventory import Inventory
from DatabaseConnector import DatabaseConnector

def update_customer_info():
    customer_id = int(input("Enter CustomerID: "))
    new_email = input("Enter new email: ")
    new_phone = input("Enter new phone: ")
    new_address = input("Enter new address: ")

    db_connector = DatabaseConnector()
    db_connector.open_connection()

    cursor = db_connector.connection.cursor()

    try:
        print(f"Updating Customer with ID: {customer_id} to Email: {new_email}, Phone: {new_phone}, Address: {new_address}")

        cursor.execute("""
            UPDATE Customers
            SET Email = %s, Phone = %s, Address = %s
            WHERE CustomerID = %s
        """, (new_email, new_phone, new_address, customer_id))

        db_connector.connection.commit()

        print("Customer information updated successfully.")
    except Exception as e:
        print(f"Error updating customer information: {e}")
        db_connector.connection.rollback()
    finally:
        cursor.close()
        db_connector.close_connection()

def update_product_info():
    product_id = int(input("Enter ProductID: "))
    new_price = float(input("Enter new price: "))
    new_description = input("Enter new description: ")

    db_connector = DatabaseConnector()
    db_connector.open_connection()

    cursor = db_connector.connection.cursor()

    try:
        print(f"Updating Product with ID: {product_id} to Price: {new_price}, Description: {new_description}")

        cursor.execute("""
            UPDATE Products
            SET Price = %s, Description = %s
            WHERE ProductID = %s
        """, (new_price, new_description, product_id))

        db_connector.connection.commit()

        print("Product information updated successfully.")
    except Exception as e:
        print(f"Error updating product information: {e}")
        db_connector.connection.rollback()
    finally:
        cursor.close()
        db_connector.close_connection()

def update_order_info():
    order_id = int(input("Enter OrderID: "))
    new_status = input("Enter new order status: ")

    db_connector = DatabaseConnector()
    db_connector.open_connection()

    cursor = db_connector.connection.cursor()

    try:
        print(f"Updating Order with ID: {order_id} to Status: {new_status}")

        cursor.execute("""
            UPDATE Orders
            SET OrderStatus = %s
            WHERE OrderID = %s
        """, (new_status, order_id))

        db_connector.connection.commit()

        print("Order information updated successfully.")
    except Exception as e:
        print(f"Error updating order information: {e}")
        db_connector.connection.rollback()
    finally:
        cursor.close()
        db_connector.close_connection()

def update_order_details_info():
    order_detail_id = int(input("Enter OrderDetailID: "))
    new_quantity = int(input("Enter new quantity: "))

    db_connector = DatabaseConnector()
    db_connector.open_connection()

    cursor = db_connector.connection.cursor()

    try:
        print(f"Updating OrderDetails with ID: {order_detail_id} to Quantity: {new_quantity}")

        cursor.execute("""
            UPDATE OrderDetails
            SET Quantity = %s
            WHERE OrderDetailID = %s
        """, (new_quantity, order_detail_id))

        db_connector.connection.commit()

        print("OrderDetails information updated successfully.")
    except Exception as e:
        print(f"Error updating OrderDetails information: {e}")
        db_connector.connection.rollback()
    finally:
        cursor.close()
        db_connector.close_connection()

def update_inventory_info():
    inventory_id = int(input("Enter InventoryID: "))
    new_quantity = int(input("Enter new quantity: "))

    db_connector = DatabaseConnector()
    db_connector.open_connection()

    cursor = db_connector.connection.cursor()

    try:
        print(f"Updating Inventory with ID: {inventory_id} to Quantity: {new_quantity}")

        cursor.execute("""
            UPDATE Inventory
            SET QuantityInStock = %s
            WHERE InventoryID = %s
        """, (new_quantity, inventory_id))

        db_connector.connection.commit()

        print("Inventory information updated successfully.")
    except Exception as e:
        print(f"Error updating Inventory information: {e}")
        db_connector.connection.rollback()
    finally:
        cursor.close()
        db_connector.close_connection()

if __name__ == "__main__":
    update_customer_info()
    update_product_info()
    update_order_info()
    update_order_details_info()
    update_inventory_info()
