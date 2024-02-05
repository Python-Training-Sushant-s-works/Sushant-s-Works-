class Customers:
    def __init__(self, CustomerID, FirstName, LastName, Email, Phone, Address):
        self.CustomerID = CustomerID
        self.FirstName = FirstName
        self.LastName = LastName
        self.Email = Email
        self.Phone = Phone
        self.Address = Address

    def GetCustomerDetails(self):
        print(f'CustomerID: {self.CustomerID}, FirstName: {self.FirstName}, LastName: {self.LastName}, Email: {self.Email},'
              f' Phone: {self.Phone}, Address: {self.Address}')
