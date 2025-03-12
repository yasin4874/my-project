3###########
class Laptop:
    def __init__(self,brand, model, price):
        self.brand= brand 
        self.model= model
        self.price= price
        
    def show_info(self):
        print (f"The brand of the laptop is {self.brand}, it's model {self.model}, and it's price is ${self.price}")
        
laptop1= Laptop("Dell","XPS 15 (9530)",1799)  
laptop1.show_info()

##############
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance 
    
    def deposit(self, amount):
        if amount < 0:
            print("you cant take a lend!")
        else:            
            self.__balance += amount
    
    def withdraw(self,reception):
        if reception > self.__balance:
            print("efficient value!")
        else:
            self.__balance-= reception
        
    def get_balance(self):
        print(f"your balance is: ${self.__balance}")
        
account1 = BankAccount(500)
account1.deposit(200)
account1.get_balance()
account1.withdraw(400)
account1.get_balance() 

##################
class Product:
    def __init__(self,name, price):
        self.name= name
        self.price= price
        
    def __str__(self):
        return f"{self.name} {self.price}"
        
good = Product("mango",23)
print(good)