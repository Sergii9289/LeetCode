from typing import Optional, List
from collections import deque

from algorythms.Graphs.BFS_find_shortest_path import reconstruct_path


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree_from_list(values: List[Optional[int]]) -> Optional[TreeNode]:
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        current = queue.popleft()

        # Ліва дитина
        if i < len(values) and values[i] is not None:
            current.left = TreeNode(values[i])
            queue.append(current.left)
        i += 1

        # Права дитина
        if i < len(values) and values[i] is not None:
            current.right = TreeNode(values[i])
            queue.append(current.right)
        i += 1

    return root


def print_tree_pretty(node: Optional[TreeNode], prefix: str = "", is_left: bool = True):
    if node is not None:
        print_tree_pretty(node.right, prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(node.val))
        print_tree_pretty(node.left, prefix + ("    " if is_left else "│   "), True)


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            current_level = []

            for _ in range(level_size):
                node = queue.popleft()
                current_level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(current_level)

        return len(result)


values_list = [3, 9, 20, None, None, 15, 7]
tree = build_tree_from_list(values_list)
print_tree_pretty(tree)
sol = Solution()
print(sol.maxDepth(tree))

