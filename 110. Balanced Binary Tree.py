from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val: int, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(levels: List[Optional[int]]) -> Optional[TreeNode]:
    if not levels:
        return None

    root = TreeNode(levels[0])
    queue = deque([root])
    i = 1

    while queue and i < len(levels):
        node = queue.popleft()

        if i < len(levels) and levels[i] is not None:
            node.left = TreeNode(levels[i])
            queue.append(node.left)
        i += 1

        if i < len(levels) and levels[i] is not None:
            node.right = TreeNode(levels[i])
            queue.append(node.right)
        i += 1

    return root


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check(node: Optional[TreeNode]) -> int:
            if not node:
                return 0  # Висота порожнього дерева — 0

            left = check(node.left)
            if left == -1:
                return -1  # Ліве піддерево незбалансоване

            right = check(node.right)
            if right == -1:
                return -1  # Праве піддерево незбалансоване

            if abs(left - right) > 1:
                return -1  # Поточний вузол незбалансований

            return max(left, right) + 1  # Висота поточного вузла

        return check(root) != -1


tree = build_tree([3, 9, 20, None, None, 15, 7])
sol = Solution()
print(sol.isBalanced(tree))  # Виведе: True
