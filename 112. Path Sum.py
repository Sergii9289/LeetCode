from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def build_tree(arr: list) -> Optional[TreeNode]:
    if not arr: return None

    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1
    while queue:
        node = queue.popleft()
        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1
        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1
    return root

def hasPathSum(root: Optional[TreeNode], targetSum: int) -> bool:
    if not root:
        return False

    # Якщо це листок — перевіряємо, чи сума дорівнює targetSum
    if not root.left and not root.right:
        return root.value == targetSum

    # Рекурсивно перевіряємо ліве і праве піддерево
    return (
        hasPathSum(root.left, targetSum - root.value) or
        hasPathSum(root.right, targetSum - root.value)
    )


arr = [5,4,8,11,None,13,4,7,2,None,None,None,1]
targetSum = 22
tree = build_tree(arr)
print(hasPathSum(tree, 22))