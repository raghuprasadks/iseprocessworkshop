class Product():
    code:int
    name:str
    supplier:str
    price:int

    """
    Constructor
    """
    def __init__(self,code,name,supplier,price):
        self.code = code
        self.name = name
        self.supplier = supplier
        self.price = price
        
    def information(self):
        return f"Code: {self.code}, Name: {self.name}, Supplier: {self.supplier}, Price: {self.price}"
"""
without constructor
prod1 = Product()
prod1.code =1
prod1.name = "Product1"
prod1.supplier = "Supplier1"
prod1.price = 100
info =prod1.information()
print("product information: ", info)    
"""
print("with constructor")
prod2 = Product(2,"Product2","Supplier2",200)
info =prod2.information()
print("product2 information: ", info)
prod3 = Product(3,"Product3","Supplier3",300)
info =prod3.information()
print("product3 information: ", info)

class ProductManagement():    
    def __init__(self):
        cart = []
    



    def addProduct(self,product):
        print("add Product")
        self.cart.append(product)
    def listProducts(self):
        print("list products")
        for prod in self.cart:
            info = prod.information()
            print(info)

pm =ProductManagement()
pm.addProduct(prod2)
pm.addProduct(prod3)
pm.listProducts()


