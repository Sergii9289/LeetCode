# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# злиття двох зв'язних списків  та , які впорядковані за зростанням,
# у єдиний зв'язний список, також впорядкований за зростанням.
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # Створюється "фіктивний" вузол () зі значенням . Цей вузол
        # використовується як тимчасовий початок нового списку.
        final = new = ListNode(0)

        while list1 and list2:
            if list1.val < list2.val:
                new.next = list1
                list1 = list1.next
            else:
                new.next = list2
                list2 = list2.next
            new = new.next
        # Коли один зі списків вичерпався, залишки іншого додаються до кінця злитого списку
        new.next = list1 or list2
        # Метод повертає final.next, який є початком нового об'єднаного списку.
        return final.next

# Функція для створення зв'язного списку зі звичайного списку
def create_linked_list(arr):
    dummy = ListNode()
    current = dummy
    for value in arr:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

# Перетворення Python-списків у зв'язні списки
list1 = create_linked_list([1, 2, 4])
list2 = create_linked_list([1, 3, 4])

# Викликаємо метод для злиття
sol = Solution()
merged_list = sol.mergeTwoLists(list1, list2)

# Виведення результату
current = merged_list
while current:
    print(current.val, end=" ")  # Output: 1 1 2 3 4 4
    current = current.next
