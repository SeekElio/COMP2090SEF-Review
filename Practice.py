#Question1
class Vechicle:
    def __init__(self,brand,color):
        self._brand = brand
        self._color = color
    def display_info(self):
        print(f"Brand:{self._brand}, Color:{self._color}")

class Car(Vechicle):
    def __init__(self,brand,color,seats):
        super().__init__(brand,color)
        self._seats = seats
    def display_info(self):
        print(f"Brand:{self._brand}, Color:{self._color},Seats:{self._seats}")

Lamborghini = Car("Lamborghini", "white",8)
Lamborghini.display_info()

#Question2 
class BankAccount:
    def __init__(self,balance):
        self._balance = balance
    def deposit(self,money):
        self._balance += money
    def withdraw(self,money):
        if money > self._balance:
            print("Your balance is not enough!")
        else:
            self._balance -= money
    def check_balance(self):
        print(f"Your balance is {self._balance}.")

Alex = BankAccount(100)
Alex.deposit(100) 
Alex.withdraw(200)
Alex.check_balance()

#Question3
def binarySearch(alist,target,left,right):
    if right > left:
        mid = (left+right)//2
        if alist[mid] == target:
            return mid
        elif alist[mid] > target:
            return binarySearch(alist,target,left,mid-1)
        else:
            return binarySearch(alist,target,mid+1,right)
    else:
        return -1
    
alist = [2, 4, 6, 8, 10]
print(binarySearch(alist,6,0,4))
print(binarySearch(alist,7,0,4))


#Question4
def fib(N):
    if N == 0 or N == 1:
        return 1
    return fib(N-1)+fib(N-2)
print(fib(9))

#Question5
thelist = [1, 3, 4, 6, 8, 9]
result = list(filter(lambda x: x%2 == 1,thelist))
print(result)

#Question6
def modify_dict(thedict):
    thedict.setdefault("new_key","new_value")
my_dict = {"key1": "value1"}
modify_dict(my_dict)
print(my_dict)