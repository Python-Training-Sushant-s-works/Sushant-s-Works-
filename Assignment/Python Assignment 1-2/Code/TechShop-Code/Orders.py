class Orders:
    def __init__(self, OrderID, CustomerID, OrderDate, TotalAmount):
        self.OrderID = OrderID
        self.CustomerID = CustomerID
        self.OrderDate = OrderDate
        self.TotalAmount = TotalAmount

    def GetOrderDetails(self):
        print(f'OrderID: {self.OrderID}, CustomerID: {self.CustomerID}, OrderDate: {self.OrderDate}, TotalAmount: {self.TotalAmount}')

    def UpdateOrderStatus(self, status):

        pass

    def CancelOrder(self):

        pass
