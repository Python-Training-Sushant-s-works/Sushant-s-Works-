class OrderDetails:
    def __init__(self, OrderDetailID, OrderID, ProductID, Quantity):
        self.OrderDetailID = OrderDetailID
        self.OrderID = OrderID
        self.ProductID = ProductID
        self.Quantity = Quantity

    def GetOrderDetailInfo(self):
        print(f'OrderDetailID: {self.OrderDetailID}, OrderID: {self.OrderID}, ProductID: {self.ProductID}, Quantity: {self.Quantity}')

    def UpdateQuantity(self, quantity):
        self.Quantity = quantity
