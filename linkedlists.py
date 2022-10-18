class LindkedList:
    def __init__(self):
        self.head = None

    def append(self, data):


        new_node = Node(data)

        if not self.head:
            self.head = new_node
            return

        cur_node = self.head
        while cur_node.get_next() != None:
            cur_node = cur_node.get_next()
        cur_node.set_next(new_node)

    def show(self):
        cur_node = self.head
        output = ""
        while cur_node != None:
            output += str(cur_node.get_data()) + ", "
            cur_node = cur_node.get_next()
        
        print(output)

    def length(self):
        size = 0
        cur_node = self.head 
        while cur_node:
            size += 1
            cur_node = cur_node.get_next()

        return size
    def push_front(self, data):
        new_node = Node(data)

        new_node.set_next(self.head)
        self.head = new_node

    def remove_last(self):
        cur_node = self.head
        while cur_node.get_next().get_next():
            cur_node = cur_node.get_next()
        else:
            cur_node.set_next(None)

    def remove_first(self):
        self.head = self.head.get_next()

    def insert(self, data, index):
        new_node = Node(data)
        cur_node = self.head 
        index_count = 0
        if index == 0:
            self.push_front(data)
            return 
        
        elif self.length() == index:
            self.append(data)
            return
        
        while cur_node.get_next():
            index_count += 1
            if index_count == index:
                new_node.set_next(cur_node.get_next())
                cur_node.set_next(new_node)
                return 

            cur_node = cur_node.get_next()
        
        
        print("The index is out of range")
    

    def value_check(self, data):
        cur_node = self.head 

        while cur_node.get_next():
            if cur_node.get_data() == data:
                return True 
            cur_node = cur_node.get_next()
        return False 



    def remove(self, index):
        cur_node = self.head 
        index_count = 0
        while cur_node.get_next():
            index_count += 1
            if index_count == index:
                cur_node.set_next(cur_node.get_next().get_next())
                return
            cur_node = cur_node.get_next()
        if self.length() == index - 1:
               self.remove_last()
               return
        if index == 0:
            self.remove_first()
            return

        print("The index is out of range")      


        


        

class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

    #getters

    def get_data(self ):
        return self.data 

    def get_next(self):
        return self.next

    #setters

    def set_data(self, data):
        self.data = data

    def set_next(self, next):
        self.next = next 

lst = LindkedList()

lst.append(2)
lst.append(4)
lst.append(4)
lst.append(10)
lst.append(12)
lst.append(21)
lst.push_front(100)
lst.remove_last()
lst.remove_first()
#lst.show()
lst.insert(19999, 5)
#lst.show()

#lst.insert(20000, 0)
#lst.show()

#lst.remove(6)
#lst.remove(0)
#lst.insert(100000, 4)
lst.show()

print(lst.length())
print(lst.value_check(10))
