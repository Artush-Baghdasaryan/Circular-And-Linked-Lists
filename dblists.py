class DbList:
    def __init__(self):
        self.head = None 
    
    def push_back(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node 
            return

        cur_node = self.head

        while cur_node.get_next():
            cur_node = cur_node.get_next()

        cur_node.set_next(new_node)
        new_node.set_prev(cur_node)

    def push_front(self, data):

        new_node = Node(data)

        if not self.head:
            self.head = new_node 
            return

        new_node.set_next(self.head)
        new_node.set_prev(None)

        
        self.head.set_prev(new_node)  
        self.head = new_node 

    def insert(self, data, index):
        new_node = Node(data)
        cur_node = self.head
        index_count = 0
        if index == 0:
            self.push_front(data)
            return 
        elif self.length() == index:
            self.push_back(data)
            return
        

        while cur_node:
            index_count += 1
            if index_count == index:
                #setting next nodes
                temp_node = cur_node.get_next()
                cur_node.set_next(new_node)
                new_node.set_next(temp_node)

                #setting prev nodes
                temp_node.set_prev(new_node)
                new_node.set_prev(cur_node)
                return
            cur_node = cur_node.get_next()

        print("the index is out of range")
        
    
    def show_left(self):
        cur_node = self.head 
        output = ""
        while cur_node != None:
            output += str(cur_node.get_data()) + ", "
            cur_node = cur_node.get_next()

        print(output)

    def show_right(self):
        cur_node = self.head 
        output = ""
        while cur_node.get_next():
            cur_node = cur_node.get_next()
        
        while cur_node:
            output += str(cur_node.get_data()) + ", "
            cur_node = cur_node.get_prev()
        
        print(output)

    def length(self):
        cur_node = self.head 
        index_count = 0

        while cur_node:
            index_count += 1
            cur_node = cur_node.get_next()

        return index_count


    def value_check(self, data):
        cur_node = self.head 

        while cur_node.get_next():
            if cur_node.get_data() == data:
                return True 
            cur_node = cur_node.get_next()
        return False  

    def remove_last(self):
        cur_node = self.head 

        while cur_node.get_next().get_next():
            cur_node = cur_node.get_next()

        cur_node.set_next(None)

    def remove_first(self):
        cur_node = self.head.get_next()
        cur_node.set_prev(None)
        self.head = cur_node 

    def remove(self, index):
        cur_node = self.head 
        index_count = 0 

        if index == 0:
            self.remove_first()
            return 
        
        if self.length() == index:
            self.remove_last()
            return 

        while cur_node.get_next():
            index_count += 1
            if index_count == index:
                cur_node.set_next(cur_node.get_next().get_next())
                cur_node.get_next().set_prev(cur_node)
                return 
            cur_node = cur_node.get_next()
        
        print("The index is out of range")



        


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


lst = DbList()
lst.push_back(1)
lst.push_front(2)
lst.push_front(10)
lst.push_back(19)
lst.show_left()

lst.insert(100, 3)
lst.show_left()
lst.show_right()
lst.length()
print(lst.value_check(10))

lst.remove_last()
lst.show_left()
lst.show_right()


lst.remove_first()
lst.show_left()
lst.show_right()

lst.insert(15, 2)
lst.show_left()

lst.remove(2)
lst.show_left()
lst.show_right()
