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

#Lab Training

#Lab1:Python 基础语法
#Question1:字符串处理
astring = "Hello, World! I'm learning Python"
capitalize_astring = astring.upper()
lower_astring = astring.lower()
new_astring1 =astring.split(" ")
new_astring2 = astring.split("o") #分隔符会消失
print(capitalize_astring)
print(lower_astring)
print(new_astring1)
print(new_astring2)

#Question2:条件与循环结构
isContinue = True #用户循环输入 需要包含在循环里
while (isContinue):
    user_input = int(input("Please enter an integer:"))
    try: #try-except进行输入验证
        result = user_input % 3
        if result == 0:
            print("This number can be divided by 3")
        else:
            print("This number cannot be divided by 3")
        isContinue = False    
    except ValueError:
        print("Please enter again!")

for i in range(1,11):
    print(i)

#Lab2:数据处理与函数应用
#Question1:列表操作
alist = []
while (len(alist) < 5): #循环从0开始计算
    try:
        user_input = int(input("Please enter an integer:"))
        alist.append(user_input)
    except ValueError:
        print("Invalid value! Please enter again!")
new_list1 = sorted(alist)
new_list2 = alist.sort()
print(new_list1)
print(new_list2)

#Question2
def triangle_area(length,height):
    area = 0.5* length * height
    print(area)
triangle_area(5,8)

#Lab3: 函数模块调用与 Lambda 函数
#Question1:函数调用
import calendar
print(calendar.prmonth(2025,4,10,2)) #prmonth()最后两个调整宽度和行间距
# Question2:Lambda 函数应用
multiply = lambda x,y : x*y #变量名是函数名
print(multiply(5,7)) #调用lambda就要调用函数

#Lab4:面向对象编程基础
#Question1:类的定义与使用
class Car:
    def __init__(self,owner,model):
        self._owner = owner
        self._model = model
        self.speed  = 0
    def acclerate(self):
        self.speed += 10
    def brake(self):
        if self.speed >= 10:
            self.speed -= 10
        else:
            self.speed = 0
    def get_speed(self):
        print(self.speed)
Ferrari = Car("Elio","SUV")
Ferrari.acclerate()
Ferrari.acclerate()
Ferrari.brake()
Ferrari.get_speed()

#Lab5:面向对象编程进阶
#Question1: 类的封装与方法实现
class BankAccount:
    def __init__(self):
        self._balance = 0
        self._password = "123456"
    def deposit(self,money):
        self._balance += money
    def withdraw(self,money):
        user_input = input("Please enter your password:")
        if user_input == "123456" and self._balance >= money:
            self._balance -= money
        else:
            raise ValueError("Your password is worng!")
AKA = BankAccount()
AKA.deposit(100)
AKA.withdraw(90)

# Question2:继承与多态的理解与应用
class Person:
    def __init__(self,name,age):
        self._name = name
        self._age = age
    def display_info():
        pass
class Student(Person):
    def __init__(self,name,age,student_id):
        super().__init__(name,age)
        self._student_id = student_id
    def enroll_course(self):
        print(f"{self._name} has been enrolled this course.")
    def display_info(self):
        print(f"Name:{self._name}\nAge:{self._age}\nStudent ID:{self._student_id}")
Alice = Student("Alice","19","123456")
Alice.enroll_course()
Alice.display_info()
#Lab6:模块化编程
#Question1:模块函数的调用与理解
import math_operation
result = math_operation.add_numbers(3,5)
print(result)

#Lab 8: 递归与搜索算法
#Quetsion1:递归函数实现
def factorial(N):
    if N == 0 or N == 1:
        return 1
    return N * factorial(N-1)
result = factorial(5)
print(result)
#Question2:线性搜索应用
def linear_search(alist,target):
    if target in alist:
        return f"{target} is in the list"
    else:
        return -1
alist = [3, 7, 1, 9, 4, 6]
result = linear_search(alist,9)
print(result)

#Lab 9:搜索算法与可视化
#Question1:改进的线性搜索
def linear_search_modified(alist,target):
    if target in alist:
        return alist[target]
    else:
        return "Not Found"
    
alist = [10, 20, 30, 40, 50]
result = linear_search_modified(alist,35)
print(result)

#Question2:生成与搜索列表
import random
alist = []
for i in range(20): #range(20) 共计20个，0-19
    result = random.randint(0,100) #randint()生成随机数
    alist.append(result)
def linear_search(target,alist):
    if target in alist:
        return alist[target]
    else:
        return "Not Found"
outcome  = linear_search(50,alist)
print(outcome)

#Lab10:
#Question1:冒泡排序
def bubble_sort(alist):
    for i in range(len(alist)-1):
        swapped = False
        for j in range(len(alist)-1-i):
            if alist[j] > alist[j+1]:
                alist[j],alist[j+1] = alist[j+1],alist[j]
                swapped = True
        if not swapped:
                break
    return alist
alist = [6, 4, 8, 2, 9]
result = bubble_sort(alist)
print(result)
#Question2:选择排序
def selection_sort(alist):
    for i in range(0,len(alist)-1):
            min_index = i
            for j in range(i+1,len(alist)):  # 内层循环从 i + 1 开始
               if alist[j]< alist[min_index]:
                    min_index = j
            alist[i],alist[min_index] = alist[min_index],alist[i]
    return alist
alist = [5, 3, 7, 1, 4]
result = selection_sort(alist)
print(result)
#Question3:插入排序
def insertion_sort(alist):
    for i in range(1,len(alist)):
            key = alist[i]
            j = i-1
            while j>=0 and key < alist[j]:
               alist[j+1] = alist[j] #用alist[j]的值覆盖alist[j+1]来完成向后移动
               j-=1
            alist[j+1] = key
    return alist
alist = [40, 35, 60, 25, 70, 50, 80]
result = insertion_sort(alist)
print(result)

#Lab11:栈与队列
#Question1:栈操作实现
class MyStack():
    def __init__(self):
          self.stack = []
    def size(self):
            print(len(self.stack))
    def isEmpty(self):
        if self.size() == 0: #直接call函数 因为不是属性
            return True
        else:
            return False  
    def push(self,num):
            self.stack.append(num)
    def pop(self):
        if not self.isEmpty():
            self.stack.pop()
        else:
             raise ValueError("Attempt to pop an empty stack!")
    def print_stack(self):
        for i in range(len(self.stack)):
             print("Index:",i,"Value:",self.stack[i]) #无法直接获得值 所以要index
stack = MyStack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.pop()
stack.size()
stack.print_stack()
#Question2:栈操作实现
class  MyQueue():
    def __init__(self):
          self.queue = []
    def size(self):
        print(len(self.queue))
    def isEmpty(self):
        if self.size() == 0:
            return True
        else:
            return False
    def enqueue(self,num):
        self.queue.append(num)
    def dequeue(self):
        if not self.isEmpty():
            self.queue.pop()
        else:
            raise ValueError("Attempt to pop an empyu queue!")      
    def print_queue(self):
        for i in range(len(self.queue)):
            print("Index:",i,"Value:",self.queue[i])
queue = MyQueue()
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
queue.dequeue()
queue.size()
queue.print_queue()
#Question3:快速排序和归并排序

#Lab 12:链表与哈希表
#Question1:链表节点插入操作：基于文档中链表类的实现，创建一个链表对象。向链表头部插入数字5，向链表尾部插入数字10，然后使用printList方法打印链表，检查插入结果。
class Node:
    def __init__(self,data=None):
        self.data = data
        self.nextobj = None
node_1 = Node(12)
node_2 = Node(54)
node_3 = Node(72)
head = node_1
node_1.nextobj = node_2 
node_2.nextobj = node_3
class LinkedList:
    def __init__(self):
        self.head = None

#Question2:哈希函数应用：使用hash()函数计算字符串 “Python” 的哈希值，并打印结果。同时，解释为什么列表类型不能直接使用hash()函数进行哈希计算。