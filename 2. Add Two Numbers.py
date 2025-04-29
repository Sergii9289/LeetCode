class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def addTwoNumbers(l1, l2):
    ll1 = create_linked_list(l1)
    ll2 = create_linked_list(l2)
    dummy_head = ListNode()  # Dummy node to simplify result list handling
    current = dummy_head
    carry = 0  # Initialize carry to 0

    while ll1 or ll2 or carry:  # Loop until there are nodes in l1, l2, or carry is not 0
        # Get values of the current nodes or 0 if the node is None
        val1 = ll1.value if ll1 else 0
        val2 = ll2.value if ll2 else 0

        # Calculate the sum and carry
        total = val1 + val2 + carry
        carry = total // 10  # Determine the carry for the next step
        current.next = ListNode(total % 10)  # Create a new node with the remainder
        current = current.next  # Move to the next node

        # Move to the next nodes in l1 and l2, if they exist
        ll1 = ll1.next if ll1 else None
        ll2 = ll2.next if ll2 else None

    return linked_list_to_list(dummy_head.next)  # Return the result list, excluding the dummy node


def create_linked_list(values):
    # Ініціалізація початкового вузла
    dummy_head = ListNode()  # Фіктивний головний вузол для спрощення роботи
    current = dummy_head

    # Створення вузлів зі значень у списку
    for value in values:
        current.next = ListNode(value)  # Додаємо новий вузол
        current = current.next  # Переходимо до наступного вузла

    return dummy_head.next  # Повертаємо голову створеного списку (без фіктивного вузла)


def linked_list_to_list(linked_list):
    result = []
    current = linked_list
    while current:
        result.append(current.value)  # Додаємо значення вузла до списку
        current = current.next  # Переходимо до наступного вузла
    return result


# Example usage:
l1 = [2, 4, 3]
l2 = [5, 6, 4]
result = addTwoNumbers(l1, l2)
print(result)
