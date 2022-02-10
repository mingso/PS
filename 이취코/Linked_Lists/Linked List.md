## Singly Linked List

### Node 정의
```python
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
```

### Linked List 정의
```python
class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.count = 0
    
    def append(self, node):
        if self.head == None:
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node
        self.count += 1
    
    def getDataIndex(self, data):
        curNode = self.head
        idx = 0
        while curNode:
            if curNode.data == data:
                return idx
            curNode = curNode.next
            idx += 1
        return -1
    
    def insertNodeAtIndex(self, idx, node):
        curNode = self.head
        prevNode = None
        cur_i = 0
        
        if idx == 0:
            if self.head:
                nextNode = self.head
                self.head = node
                self.head.next = nextNode
            else:
                self.head = node
        else:
            while cur_i < idx:
                if curNode:
                    prevNode = curNode
                    curNode = curNode.next
                else:
                    break
                cur_i += 1

            if cur_i == idx:
                node.next = curNode
                prevNode.next = node
            else:
                return -1
        self.count += 1
    
    def deleteAtIndex(self, idx):
        curNode_i = 0
        curNode = self.head
        prevNode = None
        nextNode = self.head.next
        if idx == 0:
            self.head = nextNode
        else:
            while curNode_i < idx:
                if curNode.next:
                    prevNode = curNode
                    curNode = nextNode
                    nextNode = nextNode.next
                else:
                    break
                curNode_i += 1
            if curNode_i == idx:
                prevNode.next = nextNode
            else:
                return -1
    
        self.count -= 1
            
    def clear(self):
        self.head = None
        self.count += 0
        
    def print(self):
        curNode = self.head
        string = ""
        while curNode:
            string += str(curNode.data)
            if curNode.next:
                string += " "
            curNode = curNode.next
        print(string)
```

## Doubly Linked List

### Node 정의
```python
class Node(object):
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None
```

```python
class DoublyLinked_list(object):
    def __init__(self):
        self.head = None
 
    def append(self, node):
        if self.head:
            curn = self.head
            while curn.next:
                curn = curn.next
            curn.next = node
            node.prev = curn
        else:
            self.head = node
 
    def insertNodeAtIndex(self, idx, node):
        prevn = None
        nextn = None
 
        if idx == 0:
            if self.head:
                nextn = self.head
                self.head = node
                self.head.next = nextn
                nextn.prev = self.head
            else:
                self.head = node
 
        else:
            cur_i = 0
            curn = self.head
            while cur_i < idx:
                if curn:
                    prevn = curn
                    curn = curn.next
                else:
                    break
                cur_i += 1
            if cur_i == idx:
                node.prev = prevn
                node.next = curn
                prevn.next = node
                if curn:
                    curn.prev = node
            else:
                print(-1)
                return -1
 
    def getDataIndex(self, data):
        curn = self.head
        cur_i = 0
 
        while curn:
            if curn.data == data:
                return cur_i
            curn = curn.next
            cur_i += 1
        print(-1)
        return -1
 
    def insertNodeAtData(self, data, node):
        index = self.getDataIndex(data)
        if index >= 0:
            self.insertNodeAtIndex(index, node)
        else:
            return -1
 
    def deleteAtIndex(self, idx):
        nextn = None
        prevn = None
        cur_i = 0
 
        if idx == 0:
            if self.head:
                self.head = self.head.next
                self.head.prev = None
                return
            else:
                print(-1)
                return -1
        curn = self.head
 
        while cur_i < idx:
            if curn.next:
                prevn = curn
                curn = curn.next
                nextn = curn.next
            else:
                break
            cur_i += 1
        if cur_i == idx:
            if nextn:
                nextn.prev = prevn
            prevn.next = nextn
        else:
            print(-1)
            return -1
 
    def print(self):
        curn = self.head
        string = ''
        prevn = None
        while curn:
            string += str(curn.data)
            if curn.next and curn.prev == prevn:
                string += '<->'
            prevn = curn
            curn = curn.next
        print(string)
```
