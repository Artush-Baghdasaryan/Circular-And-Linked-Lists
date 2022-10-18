class Node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data 
        self.next = next 
        self.prev = prev  

    #getters
    def get_next(self):
        return self.next 

    def get_prev(self):
        return self.prev 
    
    def get_data(self):
        return self.data 

    #setters 

    def set_next(self, next):
        self.next = next 

    def set_prev(self, prev):
        self.prev = prev
    
    def set_data(self, data):
        self.data = data 


class Circlular_doubly:
    def __init__(self, head = None, tail = None):
        self.head = head 
        self.tail = tail 

    def length(self):
        cur_node = self.head 
        index_count = 0 

        while cur_node:
            index_count += 1
            cur_node = cur_node.get_next()
            if cur_node == self.head:
                break 
        return index_count 
    def push_back(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node 
            self.tail = new_node
            
            self.head.set_next(new_node)
            self.head.set_prev(self.tail)
            self.tail.set_next(self.head)
            self.tail.set_prev(new_node)
            return       

        self.tail.set_next(new_node)
        new_node.set_prev(self.tail)

        new_node.set_next(self.head)
        self.head.set_prev(new_node)
        self.tail = new_node 
    
    def push_front(self, data):

        new_node = Node(data)

        if not self.head:
            self.head = new_node 
            self.tail = new_node
            
            self.head.set_next(new_node)
            self.head.set_prev(self.tail)
            self.tail.set_next(self.head)
            self.tail.set_prev(new_node)
            return

        new_node.set_next(self.head)
        new_node.set_prev(self.tail)
        self.head.set_prev(new_node)
        self.head = new_node 

        self.tail.set_next(self.head)

    def insert(self, data, index):
        new_node = Node(data)
        index_count = 0
        cur_node = self.head 

        if index == 0:
            self.push_front(data)
            return

        if self.length() == index:
            self.push_back(data)
            return 

        while cur_node:
            index_count += 1
            if index_count == index:
                temp_node = cur_node.get_next()
                new_node.set_next(temp_node)
                new_node.set_prev(cur_node)
                temp_node.set_prev(new_node)
                cur_node.set_next(new_node)
                return
            cur_node = cur_node.get_next()
            if cur_node == self.head:
                break
            
        print("The index is out of range")

    def show_left(self):
        cur_node = self.head 
        output = ""
        while cur_node:
            output += str(cur_node.get_data()) + ", "
            cur_node = cur_node.get_next()
            if cur_node == self.head:
                break 

        print(output)

    def show_right(self):
        cur_node = self.tail
        output = ""
        while cur_node:
            output += str(cur_node.get_data()) + ", "
            cur_node = cur_node.get_prev()
            if cur_node == self.tail:
                break 


        print(output)

    def remove_last(self):
        cur_node = self.tail.get_prev()
        cur_node.set_next(self.head)
        self.head.set_prev(cur_node)
        self.tail = cur_node 

    def remove_first(self):
        self.tail.set_next(self.head.get_next())
        self.head.get_next().set_prev(self.tail)
        self.head = self.head.get_next()

    def remove(self, index):
        index_count = 0
        if index == 0:
            self.remove_first()
            return 
        if self.length() == index:
            self.remove_last()
            return 

        cur_node = self.head
        while cur_node.get_next():
            index_count += 1
            cur_node = cur_node.get_next()
            if index_count == index:
                temp_node = cur_node.get_prev()
                temp_node.set_next(cur_node.get_next())
                cur_node.get_next().set_prev(temp_node)
                return
            if cur_node == self.head:
                break

        print("The index is out of range")

    def value_check(self, value):
        cur_node = self.head
        while cur_node:
            if(cur_node.get_data() == value):
                return f"Элемент со значением {value} существует => {True} "
            cur_node = cur_node.get_next()
            if cur_node == self.head:
                break 
        return f"Элемент со значением {value} не существует => {False} "
    

lst = Circlular_doubly()

lst.push_back(10)
lst.push_front(1)
lst.push_back("HEllO")
lst.push_back(True)
lst.insert("NewElement", 7)
lst.show_left()