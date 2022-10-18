class Node:
    def __init__(self, data = None, next = None):
        self.data = data 
        self.next = next 

    
    #getters
    #методы полечения значений
    def get_data(self):
        return self.data 

    def get_next(self):
        return self.next 

    #setters 
    #методы присвоевания значений
    def set_data(self, data):
        self.data = data 

    def set_next(self, next):
        self.next = next


class CircularLinked:

    def __init__(self, head = None, end = None):
        self.head = head 
        self.end = end
    
    def append(self, data):

        #создаем новый узел
        new_node = Node(data)
        
        #проверяем пуста ли у нас список или нет
        if not self.head:
            self.head = new_node
            self.head.set_next(new_node)
            self.end = new_node
            return 

        #если список не пуст то выполняем
        if self.end != None:
            self.end.set_next(new_node)
            new_node.set_next(self.head)
            self.end = new_node 
            return 

    def show(self):
        cur_node = self.head 
        output = ""

        while cur_node:
            output += str(cur_node.get_data()) + ", "
            cur_node = cur_node.get_next()
            if cur_node == self.head:
                break
         
        print(output)

    def length(self):
        cur_node = self.head
        size = 0
        while cur_node:
            size += 1
            cur_node = cur_node.get_next()
            if cur_node == self.head:
                break 
        
        return f"The length is {size}"

    def push_front(self, data):
        
        new_node = Node(data)
        
        #проверяем пуста ли у нас список или нет
        if not self.head:
            self.head = new_node 
            self.head.set_next(new_node)
            self.end = new_node 
            return 


        #если список не пуст то выполняем

        if self.end != None:
            new_node.set_next(self.head)
            self.end.set_next(new_node)
            self.head = new_node


    def insert(self, data, index):
        new_node = Node(data)
        cur_node = self.head 
        index_count = 0

        #есои индекс равно нулю
        if index == 0:
            self.push_front(0)
            return
        
        #проходим по списку
        while cur_node:
            index_count += 1
            if index_count == index:
                new_node.set_next(cur_node.get_next())
                cur_node.set_next(new_node)
                return
            cur_node = cur_node.get_next()

            if cur_node == self.head:
                break 
        #если нужно добавить узел в конец
        if index_count + 1 == index:
            self.append(data)
            return 
        #если не одно из условий не выполнилось то выводис исключение
        print("The index is out of range")

        
    def check_value(self, value):
        cur_node = self.head 

        while cur_node:
            if cur_node.get_data() == value:
                return f"в списке есть элемент со значением {value} => {True}"
            cur_node = cur_node.get_next()
            if cur_node == self.head:
                break 

        return f"в списке нет элемента со значением {value} => {False}" 

    def remove_last(self):
        cur_node = self.head  

        while cur_node:
            if cur_node.get_next().get_next() == self.head:
                cur_node.set_next(self.head)
                break
            cur_node = cur_node.get_next()
        self.end = cur_node
        

        
    
             
    def remove_first(self):
        cur_node = self.head 

        while cur_node.get_next() != self.head:
            cur_node = cur_node.get_next()
        cur_node.set_next(self.head.get_next())
        self.head = cur_node.get_next() 

    def remove(self, index):
        cur_node = self.head 
        index_count = 0 
        if index == 0:
            self.remove_first()
            return
        elif self.length() == index + 1:
            self.remove_last()
            return

        
        while cur_node:
            index_count += 1
            if index_count == index:
                cur_node.set_next(cur_node.get_next().get_next())
                return 
            cur_node = cur_node.get_next()
            if cur_node == self.head:
                break

     
        
        print("The index is out of range")

    
  



lst = CircularLinked()

lst.append(1)
lst.append(2)
lst.push_front(500)
lst.insert(1000, 1)
for i in range(5):
    lst.push_front(i ** 2)

lst.show()

print("удаляем последний элемент")
lst.remove_last()
lst.show()
print("удаляем первый элемент")
lst.remove_first()
lst.show()
print("удаляем второй элемент")
lst.remove(1)
lst.show()

lst.insert(100000, 6)
lst.show()





