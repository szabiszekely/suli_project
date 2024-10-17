class Dog:
    def __init__ (self,nev,kor):
        self.nev = nev
        self.kor = kor
    
    def display_info(self):
        return f"{self.nev} ({self.kor})"
    
kutya = Dog("Max",8)
        
print(kutya.display_info())

class BankAccount:
    def __init__ (self,balance):
        self.balance = balance
    
    def deposit(self,amount):
        self.balance += amount
        
    def withdraw(self,amount):
        self.balance -= amount
        
    def get_balance(self):
        return f"\n {self.balance} \n"
balance = 100
sda = BankAccount(balance)
igaz = True
while igaz:
    print(f"deposit | withdraw | balance | exit")
    beker = input("Mit szeretnél? ")
    

    if beker == "deposit":
        menyiseg = int(input("Mennyi penzt szeretnél be tenni "))
        sda.deposit(menyiseg)
    elif beker == "withdraw":
        menyiseg = int(input("Mennyi penzt szeretnél be tenni "))
        
        sda.withdraw(menyiseg)
    elif beker == "balance":
    
        print(sda.get_balance())
    elif beker == "exit":
        igaz = False
    else:
        print("\n nem értelmezhető \n")

class Student:
    def __init__(self,nev,osztalyzat):
        self.nev = nev
        self.osztalyzat = osztalyzat
    def add_grade(self,grade):
        self.osztalyzat.append(grade)
        return self.osztalyzat
    def get_average(self):
        ossz = 0
        for i in self.osztalyzat:
            ossz += i
        eredmeny = ossz / len(self.osztalyzat)
        return f"{self.nev} átlaga: {eredmeny}"

diak = Student("Péter",[2,5,1,5,3])
print(diak.get_average())
print(diak.add_grade(2))
print(diak.add_grade(3))
print(diak.add_grade(1))
print(diak.add_grade(5))
print(diak.add_grade(4))
print(diak.get_average())
