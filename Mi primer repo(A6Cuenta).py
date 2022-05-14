#Actividad Nº6 - Modulo 2:
class Person:
    def __init__(self, name):
        self.name=name
        print(f"Hi Mr/Mrs {name}")
    
    class Account:
        def __init__(self,holder,amount):
            self.holder=holder
            self.amount=amount

        def show(self):
            #print(f"This is the Account of: {???})
            print(f"The total amount of your account is: {self.amount}")

        def deposit(self, deposit):
            self.amount+=deposit
            print(f"You just deposited: {deposit}")
            if deposit>0:
                print(f"Your total account is now: {self.amount}")
            
        def remove(self,remove):
            print(f"You just remove: {remove}")
            if remove>0:
                print(f"Your total account is now: {self.amount-remove}")
person1=Person("Pablo")
user1=Person.Account(person1, 20452)
user1.show()
user1.deposit(678)
user1.remove(444)
#¿Cómo coloco números con decimales?