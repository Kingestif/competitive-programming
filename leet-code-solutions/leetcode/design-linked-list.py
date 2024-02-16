class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class MyLinkedList:

    def __init__(self):
        self.head=None      #we always say self.head on other 

    def get(self, index: int) -> int:
        # currentNode=self.head
        # array=[]

        # while currentNode:
        #     array.append(currentNode.value)
        #     currentNode=currentNode.next
        # print(array)
        

        # ----------------
        if self.head==None:
            return -1
        counter=0
        currentNode=self.head
        while counter<index:
            counter+=1
            currentNode=currentNode.next
            if currentNode==None:   #given index is greater than amount
                print("index above amount")
                return -1
        print("indexed:",currentNode.value)
        return currentNode.value

    def addAtHead(self, val: int) -> None:
        newnode=Node(val)     #creating new node
        newnode.next=self.head
        self.head=newnode
        

    def addAtTail(self, val: int) -> None:
        newnode=Node(val)
        currentNode=self.head
        if self.head==None:
            self.head=newnode
            return 
        while currentNode.next:
            currentNode=currentNode.next
        currentNode.next=newnode
        

    def addAtIndex(self, index: int, val: int) -> None:
        if self.head==None and index!=0:
            return 
        if index==0:    #if empty use insertFront function
            newnode=Node(val)     #creating new node
            newnode.next=self.head
            self.head=newnode
            return
        value=val
        newnode=Node(value)
        counter=1   #start from 1 
        currentNode=self.head
        while counter < index:
            counter+=1
            currentNode=currentNode.next
            if currentNode==None:
                print("index out of range")
                return

        newnode.next=currentNode.next
        currentNode.next=newnode


        

        

    def deleteAtIndex(self, index: int) -> None:
        if index==0:    #deleting at front
            self.head=self.head.next
            return 
        

        counter=1
        currentNode=self.head
        while counter<index:
            counter+=1
            currentNode=currentNode.next
            if currentNode.next==None:
                print("index out of range")
                return -1
        if currentNode.next:
            currentNode.next=currentNode.next.next
        else:
            return -1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)