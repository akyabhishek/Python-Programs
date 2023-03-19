from sympy import EX


class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_beg(self,data):
        node=Node(data,self.head)
        self.head=node

    def print(self):
        if self.head is None:
            print("Linked list is empty")
            return
        itr=self.head
        llstr = ''
        while itr:
            llstr += str(itr.data)+' --> ' if itr.next else str(itr.data)
            itr=itr.next
        print(llstr)

    def insert_at_end(self,data):
        if self.head is None:
            self.head=Node(data,None)
            return
        itr=self.head
        while itr.next:
            itr=itr.next
        itr.next=Node(data,None)

    def insert_values(self,datalist):
        self.head=None
        for data in datalist:
            self.insert_at_end(data)

    def get_len(self):
        count=0
        itr=self.head
        while itr:
            count+=1
            itr=itr.next
        return count
    
    def remove_at(self,index):
        if index<0 or index>=self.get_len():
            raise Exception("Invalid Index")
        if index==0:
            self.head=self.head.next
            return
        count=0
        itr=self.head

        while itr:
            if count==index-1:
                itr.next=itr.next.next
                break
            itr=itr.next
            count+=1

    def insert_at(self,index,data):
        if index<0 or index>=self.get_len():
            raise Exception("Invalid Index")
        if index==0:
            self.insert_at_beg(data)
            return
        count=0
        itr=self.head
        while itr:
            if count==index-1:
                node=Node(data,itr.next)
                itr.next=node
                break
            count+=1
            itr=itr.next  
    def insert_after_value(self,data_after,datanew):
        itr=self.head
        count=0
        valExi=False
        while itr:
            if itr.data == data_after:
                if count==self.get_len():
                    self.insert_at_end(datanew)
                else:
                    self.insert_at(count+1,datanew)
                valExi=True
                break
            itr=itr.next
            count+=1
        if not valExi:
            raise Exception("Value not fount")
    
ll = LinkedList()
ll.insert_values(["banana","mango","grapes","orange"])
ll.print()
ll.insert_after_value("mango","apple") # insert apple after mango
ll.print()