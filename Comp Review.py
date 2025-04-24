import time
#Recursive 递归

#阶乘问题
def fact(N):
    if N == 0:
        return 1 # math definition fact(0) is 1
    if N == 1:
        return 1 # simple case fact(1) is 1 (1)
    return fact(N-1) * N

if __name__ == "__main__":
    result = fact(10)
    print(result)  # factorial of 10
    result = fact(50)
    print(result)  # factorial of 50

#斐波那契数列
def fib(N):
    if N == 0:
        return 1 
    if N == 1:
        return 1 
    return fib(N-1) + fib(N-2)

if __name__ == "__main__":
    result = fib(10)
    print(result)  # fibonacci of 89


#Sort a List 排列数组

#list.sort()
alist = [3, 1, 2, 0, 7, 6, 8]
alist.sort()
print(alist)  
# [0, 1, 2, 3, 6, 7, 8]

#sorted(list)
alist = [3, 1, 2, 0, 7, 6, 8]
alist_sorted_reverse = sorted(alist, reverse=True)
print(alist_sorted_reverse)  
# [[8, 7, 6, 3, 2, 1, 0]

#字典 Dictionaries
list_of_dict = []
for i in range(10):
    adict = {}
    adict['value_1'] = i
    adict['value_2'] = 9-i
    list_of_dict.append(adict)
def get_value2(adict):
    return adict['value_2']

# sort based on key "value_2"
list_of_dict.sort(key = get_value2)
print(list_of_dict)

#lambda
sorted(list_of_dict, key=lambda adict: adict['value_1'])

#Result:
[{'value_1': 9, 'value_2': 0}, 
{'value_1': 8, 'value_2': 1}, 
{'value_1': 7, 'value_2': 2}, 
{'value_1': 6, 'value_2': 3}, 
{'value_1': 5, 'value_2': 4}, 
{'value_1': 4, 'value_2': 5}, 
{'value_1': 3, 'value_2': 6}, 
{'value_1': 2, 'value_2': 7}, 
{'value_1': 1, 'value_2': 8}, 
{'value_1': 0, 'value_2': 9}]

#对象 Objects

#搜索算法 Searching - locating information

#线性搜索 Linear Search
def linearSearch(a, x):
    for i in range(len(a)):
        if a[i] == x:
            return i
        return -1

#二分搜索 Binary Search
def binarySearch(a, left, right, x):
    if right >= left: # Check base case
        mid = (left + right) // 2
        # If element is present at the middle
        if a[mid] == x:
            return mid
        
        # If element is smaller than mid, it can only present in left sub-list
        elif a[mid] > x:
            return binarySearch(a, left, mid - 1, x)
        
        # Else the element can only present in right sub-list
        else:
            return binarySearch(a, mid + 1, right, x)
    else:
        return -1 #Element is not present in the list
start = time.time()
binarySearch(a, 0, len(a), -1)
end = time.time()
print("The time spent is: ")
print(end - start)



#Sorting 排序算法 - some well-defined order 
alist = [64, 34, 25, 12, 22, 11, 90]
#选择排序 Selection Sort 
def selectionSort(alist):
    for idx in range(len(alist) - 1): #从0到n-2
        min_index = idx
    for j in range(idx + 1, len(alist)):
    # select the minimum element in every iteration
        if alist[j] < alist[min_index]:
            min_index = j
    # swapping the elements to sort the list
    alist[idx], alist[min_index] = alist[min_index], alist[idx]
selectionSort(alist)


#冒泡排序 Bubble Sort
alist = [64, 34, 25, 12, 22, 11, 90]
#正序排序：
def bubble_sort(alist):
    for i in range(len(alist)-1): #从0到n-2
        swapped = False
        for j in range(len(alist)-1-i):
            if alist[j] > alist[j+1]:
                alist[j],alist[j+1] = alist[j+1],alist[j]
                swapped = True
        if not swapped:
            break
    return alist
#倒叙排序：
def bubble_sort_reverse(alist): #从1到n-1
    for i in range(len(alist)-1,0,-1):
        swapped = False
        for j in range(i):
            if alist[j] > alist[j+1]:
                swapped = True
                alist[j],alist[j+1] = alist[j+1],alist[j]
        if not swapped:
            return
    return alist
bubble_sort_reverse(alist)

#插入排序 Insertion Sort

#正序排序
def insertion_sort(alist):
    for i in range(1,len(alist)):
        current = alist[i]
        j = i -1
        while (j >=0 and alist[j] > current):
            alist[j+1] = alist[j]
            j-=1
        alist[j+1] = current
#倒叙排序
def insertionSort(alist):
   # traverse through 1 to len(alist)
   for idx in range(1, len(alist)): #从1到n-1 因为第一个已经排序好了
      # move elements of alist[0 .. idx-1], that are greater than 
      # the previous value, to one position ahead of their current 
      # position
      for j in range(idx, 0, -1):
         if alist[j] < alist[j - 1]:
            # swapping the elements if they are not ordered
            alist[j], alist[j - 1] = alist[j - 1], alist[j]
         # we can stop if alist[j] >= alist[j-1]
         # note that alist[0, ..., idx-1] is sorted
         # this is where we can stop earlier.
         else:
            break
         
insertionSort(thelist)


#快速排序 Quick Sort
# Function to find the partition (noun) position and partition (verb) the list
def partition(thelist, low, high):
    # Choose the rightmost element as pivot
    pivot = thelist[high]
    # Pointer for greater element
    i = low - 1
    # Traverse through all elements, compare each element with pivot
    for j in range(low, high):
        if thelist[j] <= pivot:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1
            # Swapping element at i with element at j
            (thelist[i], thelist[j]) = (thelist[j], thelist[i])
        # Swap the pivot element with
        # the greater element specified by i
        (thelist[i + 1], thelist[high]) = (thelist[high], thelist[i + 1])
        # Return the position from where partition is done
        return i + 1
# Function to perform quicksort
def quick_sort(thelist, low, high):
    if low < high:
    # Find pivot element such that
    # element smaller than pivot are on the left
    # element greater than pivot are on the right
        pi = partition(thelist, low, high)
        # Recursive call on the left of pivot
        quick_sort(thelist, low, pi - 1)
        # Recursive call on the right of pivot
        quick_sort(thelist, pi + 1, high)

#归并排序 Merge Sort
def mergeSort(arr):
 if len(arr) > 1:
    # Finding the mid of the array
    mid = len(arr)//2
    # Dividing the array elements
    L = arr[:mid]
    # into 2 halves
    R = arr[mid:]
    # Sorting the first half
    mergeSort(L)
    # Sorting the second half
    mergeSort(R)
    i = j = k = 0
     # Copy data to temp arrays L[] and R[]
 while i < len(L) and j < len(R):
    if L[i] <= R[j]:
        arr[k] = L[i]
        i += 1
    else:
        arr[k] = R[j]
        j += 1
        k += 1
    # Checking if any element was left
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1



#数据结构

#Stack 栈
class Stack:
    def __init__(self):
        self.stack = []
    def size(self):
        return len(self.stack)
    def isEmpty(self):
        if self.size() == 0:
            return True
        else:
            return False
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if not self.isEmpty():
            self.stack.pop()
        else:
            raise IndexError("Attempt to pop an empty stack")
    def print_stack(self):
        for i in range(len(self.stack)):
            print('index:', i, 'Value:', self.stack[i])

#Queue 队列
class Queue:
    def __init__(self):
        self.queue = []
    def size(self):
        return len(self.queue)
    def isEmpty(self):
        if self.size() == 0:
            return True
        else:
            return False
    def enQueue(self, value):
        self.queue.append(value)
    def deQueue(self):
        if not self.isEmpty():
            self.queue.pop(0)
        else:
            raise IndexError("Attempt to dequeue an empty stack")
    def print_queue(self):
        for i in range(len(self.queue)):
            print('index:', i, 'Value:', self.queue[i])


#Linked List 链表
class Node:
    def __init__(self, data=None):
        self.data = data
        self.nextobj = None
node_1 = Node(12)
node_2 = Node(99)
node_3 = Node(37)
node_1.nextobj = node_2
node_2.nextobj = node_3

class LinkedList:
    def __init__(self):
        self.head = None
    def insertEnd(self, data):
        # insert new data at the end
        if self.head == None:            # 如果火车没有车头
            # if the link has no node
            self.head = Node(data)       # 新车厢直接成为车头
            return
        temp = self.head      #如果有车头
        # traverse to the last node
        while temp.nextobj != None:   #只要还没有到达车尾,逐个车厢检查
            temp = temp.nextobj     #让 temp 指针移动到下一个节点
        temp.nextobj = Node(data)   #将车尾的挂钩指向新车厢，完成尾插。
    def insertBegin(self, data):
        # insert new data at the beginning
        new_node = Node(data)
        new_node.nextobj = self.head
        self.head = new_node
    def insertBetween(self, mid_node, data):
        # insert new data in between
        # mid_node and mid_node.nextobj
        new_node = Node(data)
        new_node.nextobj = mid_node.nextobj
        mid_node.nextobj = new_node
    def printList(self):
        thenode = self.head
        while thenode.nextobj != None:
            print(thenode.data)
            thenode = thenode.nextobj
    def deleteNode(self, target_data):
        thenode = self.head 
        if thenode.data == target_data:   
            self.head = thenode.nextobj   #让新车头变为原车头的下一节车厢
            return
        while thenode.nextobj != None: #当问题车厢不在车头时，遍历寻找问题车厢
            if thenode.data == target_data:
                break
            prevnode = thenode # 记录当前车厢的前一节车厢
            thenode = thenode.nextobj # 移动到下一节车厢
        prevnode.nextobj = thenode.nextobj #让前一节车厢的挂钩，跳过问题车厢，直接连接下一节车厢
#哈希表
class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.load = 0
        self.buckets = [None] * self.capacity
    def hash_function(self, key):
        hashed_value = key % self.capacity 
        return hashed_value # return the key
    def insert(self, key, value):
        index = self.hash_function(key)
        # open addressing resolves collision
        while self.buckets[index] != None:
            index += 1
        self.buckets[index] = {'key': key, 'value': value}
        self.load += 1 # update the load number
    def search(self, key):
        index = self.hash_function(key)
        while self.buckets[index] is not None and self.buckets[index]['key'] != key:
            index += 1
        if self.buckets[index] is None:
            return None # Not found
        else:
            return self.buckets[index]['value'] # return the value
    def remove(self, key):
        index = self.hash_function(key)
        while self.buckets[index] is not None and self.buckets[index]['key'] != key:
            index += 1
            if self.buckets[index] is None:
                return None # Not found
            else:
                self.buckets[index] = None # Remove the key-value pair
                self.load -= 1 # update the load number
                return 