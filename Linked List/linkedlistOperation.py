class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
class Linkedlist:
  def __init__(self):
    self.head=None
  def add(self,data):
    obj=Node(data)
    if self.head==None:
      self.head=obj
      return
    cn=self.head
    while cn.next is not None:
      cn=cn.next
    cn.next=obj
  def traverse(self):
    cn=self.head
    while cn.next is not None:
      print (cn.data,end="->")
      cn=cn.next
    print(cn.data)
  def delfirst(self):
    self.head=self.head.next
  def delLast(self):
    self.head.next.next=None      
ll=Linkedlist()
ll.add(10)
ll.add(20)
ll.add(30)
ll.add(40)
ll.traverse()
ll.delfirst()
ll.traverse()
ll.delLast()
ll.traverse()




class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
class Linkedlist:
  def __init__(self):
    self.head=None
  def add(self,data):
    obj=Node(data)
    if self.head==None:
      self.head=obj
      return
    cn=self.head
    while cn.next is not None:
      cn=cn.next
    cn.next=obj
  def traverse(self):
    cn=self.head
    while cn.next is not None:
      print (cn.data,end="->")
      cn=cn.next
    print(cn.data)
  def delfirst(self):
    self.head=self.head.next
  def delLast(self):
    self.head.next.next.next=None 
    cn=self.head
    # if cn.Next is None:
    #   cn=None
    # while cn.Next.Next is not None:
    #   cn=cn.Next
    # cn.Next=None     
ll=Linkedlist()
ll.add(10)
ll.add(20)
ll.add(30)
ll.add(40)
ll.add(50)
ll.traverse()
ll.delfirst()
ll.traverse()
ll.delLast()
ll.traverse()





class Node:
  def __init__(self, data):
      self.data = data
      self.next = None


class Linkedlist:
  def __init__(self):
      self.head = None

  def add(self, data):
      obj = Node(data)

      if self.head is None:
          self.head = obj
          return

      cn = self.head
      while cn.next is not None:
          cn = cn.next

      cn.next = obj

  def traverse(self):
      cn = self.head

      while cn.next is not None:
          print(cn.data, end="->")
          cn = cn.next

      print(cn.data)

  def delfirst(self):
      self.head = self.head.next

  def delLast(self):
      cn = self.head

      if cn.next is None:
          self.head = None
          return

      while cn.next.next is not None:
          cn = cn.next

      cn.next = None

  def len(self):
      count = 0
      cn = self.head

      while cn is not None:
          count += 1
          cn = cn.next

      return count

  def inSAt(self, data, position):
      if position < 0 or position > self.len():
          print("Invalid position")
          return

      newNode = Node(data)

      if position == 0:
          newNode.next = self.head
          self.head = newNode
          return

      cn = self.head

      for i in range(position - 1):
          cn = cn.next

      newNode.next = cn.next
      cn.next = newNode
      def inSAt(self, data, first):
        if first==n < 0 or first > self.len():
            print("Invalid first")
            return
  
        newNode = Node(data)
  
        if first == 0:
            newNode.next = self.head
            self.head = newNode
            return
  
        cn = self.head
  
        for i in range(first - 1):
            cn = cn.next
  
        newNode.next = cn.next
        cn.next = newNode

  def  delbyvalue(self,target):
    if self.head is None:
      return False
    if self.head.data==target:
      self.head=self.head.next
      return True
    current=self.head
    while current.next is not None:
      if current.next.data==target:
        current.next=current.next.next
        return True
      current=current.next
    return false
  def count(self,data):
    if self.head is None:
      return 0
    c=0
    cn=self.head
    while cn.next is not None:
      if cn .data==data:
        c+=1
      cn=cn.next
    if cn.data==data:
      c+=1
    return c
ll = Linkedlist()
ll.add(10)
ll.add(20)
ll.add(30)
ll.add(40)
ll.add(50)
ll.traverse()
ll.delfirst()
ll.traverse()
ll.delLast()
ll.traverse()
ll.inSAt(60, 2)
ll.traverse()
ll.inSAt(70 ,0)
ll.traverse()
ll.delbyvalue(70)
ll.traverse()
ll.delbyvalue(20)
ll.traverse()
ll.add(60)
print(ll.count(60))
