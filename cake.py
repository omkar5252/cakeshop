class Cake:
    def __init__(self,id,name,price,quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return str(self.id)+","+str(self.name)+","+str(self.price)+","+str(self.quantity)
        
