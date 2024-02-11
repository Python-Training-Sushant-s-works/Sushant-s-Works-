import pytest
import mysql.connector

conn = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "Sushant@9546",
    database = "carconnect"
)

def authentication():
    cursor = conn.cursor()
    cursor.execute("select username,password from customer where customerid = 1")
    l = []
    for i in cursor:
        l.append(i)
    return l
    cursor.close()

def test_authentication():
     assert authentication() == [('johndoe123', 'password123')]

def updatinCustomer():
    cursor = conn.cursor()
    cursor.execute("update customer set firstname = 'johnny' where customerid = 1")
    conn.commit()
    cursor.close()
    return True

def test_updatingCustomer():
    assert updatinCustomer() == True


def adding():
    cursor = conn.cursor()
    cursor.execute("insert into vehicle(Model, Make, Year, Color, RegistrationNumber, Availability, DailyRate)"
                   "values(%s,%s,%s,%s,%s,%s,%s)",('Malibu', 'Chevrolet', 2019, 'Red', 'BCC84',1, 55.00))
    conn.commit()
    cursor.close()
    return True

def test_adding():
    assert adding() == True

def updatingVehicle():
    cursor = conn.cursor()
    cursor.execute("update vehicle set model = 'civi' where vehicleid = 1")
    conn.commit()
    cursor.close()
    return True

def test_updatingVehicle():
    assert updatingVehicle() == True


def gettingAvailableVehicle():
    cursor = conn.cursor()
    cursor.execute("select * from vehicle where availability = 1")
    result = cursor.fetchall()
    return len(result)


def test_gettingAvailableVehicle():
    assert gettingAvailableVehicle() >= 0


def gettingAllVehicle():
    cursor = conn.cursor()
    cursor.execute("select * from vehicle")
    result = cursor.fetchall()
    return len(result)

def test_gettingAllVehicle():
    assert gettingAllVehicle() == 13
