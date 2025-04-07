class Node(object):  # основа LinkedList
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, data): # додавання елемента до списку
        new_node = Node(data)
        current_node = self.head
        if not current_node:  # if current_node == None
            self.head = new_node
            return
        while current_node.next: # ітерація до кінця списку
            current_node = current_node.next
        current_node.next = new_node  # присвоєння значення новому вузлу

    def show(self): # ітерація по списку
        current_node = self.head
        output = ''
        while current_node:
            output += str(current_node.data) + '->'
            current_node = current_node.next
        print(output)

    def lenght(self):  # метод рахує кількість елементів
        current_node = self.head
        count = 0
        while current_node:
            count += 1
            current_node = current_node.next
        print(count)

    def add_in_front(self, data): # додавання елементу в початок списку
        new_node = Node(data)  #  створюємо Node з вхідними даними
        new_node.next = self.head  #  робимо перший елемент для нього наступним
        self.head = new_node  #  змінюємо значення першого елементу

    def remove_last_element(self):
        current_node = self.head
        while current_node.next.next: # перевірка чи є у наступного елементу наступний (next)
            current_node = current_node.next
        # якщо item.next.next = None, то item.next = None (видаляємо посилання і об'єкт)
        current_node.next = None

    def remove_first(self): # видалення першого елементу
        self.head = self.head.next # просто забуваємо про існування першого елементу

    def item_by_index(self, index):  # повертає значення як у list. За індексом(якого не існує)
        current_node = self.head
        count = 0
        while current_node: # current_node != None
            if count == index: # коли count == index, повертаємо значення
                return current_node.data
            count += 1
            current_node = current_node.next
        else: return 'Not valid index'

    def insert_by_index(self, index, data): # заміна елементу
        current_node = self.head
        count = 0
        while current_node:
            if count + 1 == index:
                new_inst = Node(data=data, next=current_node.next.next)
                current_node.next = new_inst
                return f'Inserted new item [{index}]: {new_inst.data}'
            count += 1
            current_node = current_node.next
        else:
            return 'Not valid index'


    def remove_by_index(self, index): # видалення елементу
        current_node = self.head
        count = 0
        while current_node:
            if count + 1 == index:
                current_node.next = current_node.next.next
                return f'Deleted item [{index}]: {current_node.data}'
            count += 1
            current_node = current_node.next
        else:
            return 'Not valid index'


my_list = LinkedList()
print('Add items 2,4,6,8')
my_list.append(2)
my_list.append(4)
my_list.append(6)
my_list.append(8)
print('Add 111 in front')
my_list.add_in_front(111)
my_list.show()
print('Retrieve lenght of list')
my_list.lenght()
my_list.show()
print('Remove last element')
my_list.remove_last_element()
my_list.show()
print('Remove first element')
my_list.remove_first()
my_list.show()
print('Retrieve item by index')
print(my_list.item_by_index(2))
print('Insert item in list')
my_list.insert_by_index(1, 'new')
my_list.show()
print('Delete by index')
my_list.remove_by_index(1)
my_list.show()

