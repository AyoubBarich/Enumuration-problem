import heapq

class Node:
    """Node is a class that implementds a single node in our ourdred set"""
    def __init__(self,data:int):
        
        self.data = data
        self.next = None

    def getData(self):
        return self.data
    
    def __next__(self):
        return self.next
    
    def isEmpty(self):
        if self == None:
            return True
        return False
    def setNext(self, node):
        self.next = node

    def hasNext(self):
        return self.next is None

    
    def __str__(self) -> str: 
        return str(self.data)   


class OrderedSet():

    def __init__(self,sequence=[]) :
        self.size = 0
        self.head = None
        while sequence != []:
            self.add(sequence.pop(0))
            self.size += 1

    def add(self,item):
        """
        add allows us to add a given item to our ordred list
        and keep the ordre property of our Orderd list

        returns : void
        param : item that we want to add to our Orderd list
        """
        current = self.head
        previous = None 
        flag = False
        curr = None
        while current != None:
            val = current.getData()
            if val >= item:
                curr = val
                break
            else:
                previous = current
                current = current.__next__()

        if curr != item:
            temp = Node(item)
            if previous == None:
                temp.setNext(self.head)
                self.head = temp
            else:
                temp.setNext(current)
                previous.setNext(temp)

    def search(self,item):
        """
        Given an item we return if an item is in our ordred list or not
        returns : boolean
        param : item of generic type
        """

        current = self.head
        found = False
        stop = False

        while current != None and not found and not stop:
            if current.getData() == item:
                found = True
            else:
                if current.getData() > item:
                    stop = True
                else:
                    current = current.getNext() 
        return found
    
    def includesSequence(self ,sequence ):
        """
        given a generic sequence we look if this sequence is in our orderd list
        param : iterable sequence
    
        returns : boolean
        """

        flag = True
        for element in sequence :
            flag &= self.search(element)
        return flag

    
    def __str__(self) -> str:
        """overides the print function"""
        res="{"
        current = self.head
        while current != None:
            data = current.getData()
            res+=" "+str(data)+" "
            current = current.__next__()
        res += "}"
        return res
    def __lt__(self,other):
        """adds the the possibility of coparing two orderd sets"""
        
        current = self.head
        otherCurrent = other.head
        while current != None and otherCurrent != None :
            if current.getData() > otherCurrent.getData() :
                return False
            elif current.getData() < otherCurrent.getData() :
                return True
            current = current.__next__()
            otherCurrent = otherCurrent.__next__()
        return False
    def __repr__(self) -> str:
        return self.__str__()




        # for i in range(min(len(SetA),len(SetB))):
        #     if SetA[i]< SetB[i]:
        #         return SetA
        #     elif SetB[i] < SetA[i] :
        #         return SetB
            
        # return SetA
SetA = OrderedSet([5,3,7,6,6,9,5,4,7])
SetB = OrderedSet([5,9,8,5])
SetC = OrderedSet([5,9,8,2])
SetD = OrderedSet([5,9,8,5,1,3])

print("setA :"+OrderedSet.__str__(SetA))
print("setB :"+OrderedSet.__str__(SetB))
print(SetA < SetB)

l = [SetA,SetB,SetC,SetD]

print("l before :" ,l)
heapq.heapify(l)
print("l after :" , l )