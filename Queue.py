import numpy as np
class Queue:
    
    def __init__(self, size):
        self.__data = np.empty((size,), dtype = np.uint16)
        self.__capacity = size
        self.__NOE = 0
        self.__front = -1
        self.__rear = -1

    def isFull(self):
        if (self.__NOE==self.__capacity):
            return True
        return False
    
    def isEmpty(self):
        if (self.__NOE == 0):
            return True
        return False
    
    def front(self):
        if(not self.isEmpty()):
            return self.__data[self.__front]
        else:
            return "Queue is empty"
        
    def rear(self):
        if(not self.isEmpty()):
            return self.__data[self.__rear]
        else:
            return "Queue is empty"
        
    def enqueue(self, element):
        if(self.isFull):
            self.__rear = self.__rear + 1
            self.__data[self.__rear] = element
            if(self.__front == -1):
                self.__front = 0
            self.__NOE = self.__NOE + 1
        else:
            return "Queue is Full"
    
    def dequeue(self):
        if(not self.isEmpty()):
            element = self.__data[self.__front]
            if (self.__front==self.__rear):
                self.__front = self.__rear = -1
            else:
                self.__front = self.__front + 1
            self.__NOE = self.__NOE - 1
            return element
        else:
            return "Queue is empty"
        



obj= Queue(5)
i = 3
while(not obj.isFull()):
    obj.enqueue(i)
    i = i + 1

while(not obj.isEmpty()):
    print(obj.front())
    obj.dequeue()
