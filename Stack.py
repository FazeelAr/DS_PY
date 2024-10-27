import numpy as np
class Stack:
    def __init__(self,size):
        self.__capacity=size
        self.__data = np.empty((size,),dtype=np.uint)
        self.__top = -1
    def isEmpty(self):
        if self.__top==-1:
            return True
        return False
    def isFull(self):
        if self.__top==self.__capacity-1:
            return True
        return False
    def push(self,element):
        if not self.isFull():
            self.__top = self.__top + 1
            self.__data[self.__top]=element
        else:
            print("Stack is full")

    def pop(self):
        if not self.isEmpty():
            val = self.__data[self.__top]
            self.__top = self.__top - 1
            return val
        print("Stack is empty")
        return -1
    

def fibonacci(first, sec, N):
    if(N==0):
        return
    else:
        res=first+sec
        print(res,end=" ")
        fibonacci(sec,res,N-1)


def power(bas,exp):
    if exp==0:
        return 1
    else:
        return bas*power(bas,exp-1)
    
#print(power(2,5))
#fibonacci(0,1,5)


obj = Stack(5)
obj.push(23)
obj.push(33)
obj.push(44)
obj.push(55)
obj.push(66)
obj.push(77)
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())
print(obj.pop())


