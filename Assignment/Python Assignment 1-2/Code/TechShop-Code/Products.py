class Products:
    def __init__(self, ProductID, ProductName, Description, Price):
        self.ProductID = ProductID
        self.ProductName = ProductName
        self.Description = Description
        self.Price = Price

    def GetProductDetails(self):
        print(f'ProductID: {self.ProductID}, ProductName: {self.ProductName}, Description: {self.Description}, Price: {self.Price}')

    def UpdateProductInfo(self, Price=None, Description=None):
        if Price is not None:
            self.Price = Price
        if Description is not None:
            self.Description = Description
