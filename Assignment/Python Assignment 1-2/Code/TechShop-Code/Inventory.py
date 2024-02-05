class Inventory:
    def __init__(self, InventoryID, ProductID, QuantityInStock, LastStockUpdate):
        self.InventoryID = InventoryID
        self.ProductID = ProductID
        self.QuantityInStock = QuantityInStock
        self.LastStockUpdate = LastStockUpdate

    def GetInventoryDetails(self):
        print(f'InventoryID: {self.InventoryID}, ProductID: {self.ProductID}, QuantityInStock: {self.QuantityInStock}, LastStockUpdate: {self.LastStockUpdate}')

    def UpdateStockQuantity(self, new_quantity):
        self.QuantityInStock = new_quantity
