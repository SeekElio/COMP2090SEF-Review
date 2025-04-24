'''
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
# Question2.1:Lambda 函数应用
multiply = lambda x,y : x*y #变量名是函数名
print(multiply(5,7)) #调用lambda就要调用函数
#Question2.2:
alist = [1, 2, 3, 4, 5]
result_function = lambda alist : (x**2 for x in alist)
print(list(result_function(alist)))
#Question2.3：
alist = [10, 21, 30, 43, 55]
new_alist = list(filter(lambda x: x%2 == 0,alist,))
print(new_alist)
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
#Quetsion1.1:递归函数实现
def factorial(N):
    if N == 0 or N == 1:
        return 1
    return N * factorial(N-1)
result = factorial(5)
print(result)
#Question1.2:
def fib(N):
    if N == 0:
        return 0
    elif N == 1:
        return 1
    return fib(N - 1)+fib(N - 2)
result = fib(6)
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
#Question1:链表节点插入操作：创建一个链表对象。向链表头部插入数字5，向链表尾部插入数字10，然后使用printList方法打印链表，检查插入结果。
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
    def insert_begin(self,data):
        new_node = Node(data)
        new_node.nextobj = self.head
        self.head = new_node 
    def insert_end(self,data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            return
        temp = self.head
        while temp.nextobj != None:
            temp = temp.nextobj
        temp.nextobj = new_node
    def print(self):
        thenode = self.head
        while thenode.nextobj != None:
            print(thenode.data)
            thenode = thenode.nextobj
       
myLinkedList = LinkedList()
myLinkedList.head = node_1
myLinkedList.insert_begin(5)
myLinkedList.insert_end(10)
myLinkedList.print()
#Question2:
class SimpleHashTable:
    def __init__(self,capacity):
        self.capacity =capacity
        self.load = 0
        self.buckets = [None] * capacity
    def hash_function(self,key):
        hashed_value = hash(key)%self.capacity
        return hashed_value
    def insert(self,key,value):
        index = self.hash_function(key)
        while self.buckets[index] != None:
            index += 1
        self.buckets[index] = {'key:':key,"value":value}
        self.load += 1
    def search(self, key):
        index = self.hash_function(key)
        while self.buckets[index] is not None and self.buckets[index]['key'] != key:
            index += 1
        if self.buckets[index] is None:
            return None
        else:
            return self.buckets[index]['value']
    def remove(self, key):
        index = self.hash_function(key)
        while self.buckets[index] is not None and self.buckets[index]['key']!=key:
            index +=1
        if self.buckets[index] is None:
            return None
        else:
            self.buckets[index] = None
            self.load -= 1
            return "Delete it!"
'''
#Exam Practice
#1. Call by Reference（按引用调用）
# 编写一个 Python 函数swap，该函数接收两个整数的引用，并交换它们的值。
# 使用列表来传递这两个整数，函数应直接修改列表中的值，而不是返回新的列表。
def swap(num_list):
    # 在这里编写交换逻辑
    num1 = num_list[0]
    num2 = num_list[1]
    num_list = [num2,num1]

nums = [3, 5]
swap(nums)
print(nums)

#2. Lambda function(匿名函数)
#使用 lambda 函数和sorted函数对一个包含字典的列表进行排序。
# 列表中的每个字典都有name（字符串类型）和age（整数类型）两个键。按照age对列表进行升序排序。
students = [
    {'name': 'Alice', 'age': 20},
    {'name': 'Bob', 'age': 18},
    {'name': 'Charlie', 'age': 22}
]
result_func = lambda alist: (alist.sort(key="age") for _ in alist)
result = result_func(students)

#3. Filter function(过滤函数)
#给定一个整数列表，使用filter函数和 lambda 表达式过滤出所有的偶数。
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x%2==0,numbers))
print(even_numbers)

#4. Define a Class
# 定义一个名为Circle的类，它有一个构造函数用于接收圆的半径radius。
# 类中包含两个方法：
# calculate_area用于计算圆的面积，
# calculate_circumference用于计算圆的周长。
# PI的值取3.14。

class Circle:
    def __init__(self,radius):
        self.raduis = radius
    def calculate_area(self):
        Area = 3.14*self.radius**2
        return Area
    def calculate_circumference(self):
        circumference = 3.14*2*self.radius
        return circumference
    
circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_circumference())

#5. Inheritance(继承)
# #定义一个基类Vehicle，包含属性brand（品牌）和color（颜色），以及方法display_info用于显示车辆的品牌和颜色信息。
# 再定义一个子类Car继承自Vehicle，新增属性seats（座位数），并重写display_info方法，使其除了显示品牌和颜色，还显示座位数信息。
class Vehicle:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color
    def display_info(self):
        print(f"Brand:{self.brand},Color:{self.color}")
class Car(Vehicle):
    def __init__(self,brand,color,seats):
        super().__init__(brand,color)
        self.seats = seats
    def display_info(self):
        print(f"Brand:{self.brand},Color:{self.color},Seats:{self.seats}")
#6.Searching algorithms（搜索算法）
#实现线性搜索（Linear Search）函数，在数组中查找目标值，找到返回索引，否则返回 - 1
def linear_search(arr, target):
    # 请补全代码
    for i in range(len(arr)):
        if arr[i] == target:
            return i
        return -1
#实现二分搜索函数，在数组中查找目标值，找到返回索引，否则返回 - 1
def binary_search(x,arr,left,right):
    if right > left:
        mid = (right+left)//2
    if arr[mid] == x:
        return mid
    elif arr[mid] > x:
        return binary_search(x,arr,left,mid-1)
    elif arr[mid]<x:
        return binary_search(x,arr,mid+1,right)
    else:
        return -1

#现冒泡排序（Bubble Sort），对数组进行升序排序。
def selection_sort(alist):
    for i in range(len(alist)-1):
        min_index = i
        for j in range(i+1,len(alist)):
            if alist[j] < alist[min_index]:
                min_index = j
        alist[i],alist[min_index] = alist[min_index],alist[i]

def bubble_sort(alist):
    for i in range(len(alist)-1,0,-1):
        swapped = False
        for j in range(i):
            if j[1+1] > j[1]:
                swapped = True
                alist[j],alist[j+1] = alist[j+1],alist[j]
        if not swapped:
            return
    return alist

def insertion_sort(alist):
    for i in range(1,len(alist)):
        current = alist[i]
        j = i -1
        while (j >=0 and alist[j] > current):
            alist[j+1] = alist[j]
            j-=1
        alist[j+1] = current
def insertion_sort_reverse(alist):
    for i in range(1,len(alist)):
        for j in range(i,0,-1):
            if alist[j] < alist[j-1]:
                alist[j],alist[j-1] = alist[j-1],alist[j]
#五、Recursion（递归）
#用递归实现计算数组元素之和
arr =  [1, 2, 3, 4]
def sum(arr):
    if len(arr) == 0:
        return 0
    return arr[0]+arr[1:]
#六、Linked Lists（链表）
#实现链表的 头插法 插入节点，并编写 print_list 方法打印链表所有节点的值。
class Node:
    def __init__(self,data):
        self.data = data
        self.nextobj = None

class LinkedList:
    def __init__(self):
        self.head = None
    def inser_begin(self,data):
        new_node = Node(data)
        new_node.nextobj = self.head
        self.head =  new_node
    def print_list(self):
        thenode = self.head
        while thenode!=None:
            print(thenode)
            thenode = thenode.nextobj
#七、Stack and Queues（栈和队列）
#题目 1：栈操作
#实现栈的 push 和 pop 方法，并模拟栈的进出过程。
#要求：用列表模拟栈，push 向栈顶添加元素，pop 移除并返回栈顶元素，空栈时抛出异常。
class Stack:
    def __init__(self):
        self.stack = []
    def size(self):
        size = len(self.stack)
        return size
    def isEmpty(self):
        if self.size() == 0:
            return True
        else:
            return False
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        if not self.isEmpty():
            self.stack.pop()
        else:
            raise ValueError("Attempt to pop an empty stack!")
#八、Hash Tables（哈希表）
#实现哈希表的 insert 和 search 方法，使用开放寻址法（线性探测）处理冲突。
#要求：哈希函数用 key % capacity，存储结构为列表，每个元素存储键值对（如字典）。
class HashTable:
    def __init__(self,capacity):
        self.capacity = capacity
        self.load = 0
        self.buckets = [None] * capacity
    def insert(self,key,value):
        index = self.hash_function(key)
        while self.buckets[index]!=None:
            index+=1
        self.buckets[index] = {'key':key,'value':value}
        self.load +=1
    def search(self,key):
        index = self.hash_function(key)
        while self.bucktes[index]!=None and self.buckets['key']!=key:
            index+=1
        if self.buckets[index]==None:
            return None
        else:
            return self.buckets[index]['value']
        
