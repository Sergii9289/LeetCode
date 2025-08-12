from typing import List, Optional
import networkx as nx
import matplotlib.pyplot as plt

# Визначення вузла дерева
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left: Optional[TreeNode] = left
        self.right: Optional[TreeNode] = right

# Основний клас
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None

        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        return root

    # Рекурсивна побудова позицій для візуалізації
    def draw_tree(self, root, pos=None, x=0, y=0, dx=1.0):
        if pos is None:
            pos = {}
        if root:
            pos[root.val] = (x, y)
            if root.left:
                pos.update(self.draw_tree(root.left, pos, x - dx, y - 1, dx / 2))
            if root.right:
                pos.update(self.draw_tree(root.right, pos, x + dx, y - 1, dx / 2))
        return pos

    # Побудова графу для візуалізації
    def plot_tree(self, root):
        G = nx.DiGraph()
        pos = self.draw_tree(root)

        def add_edges(node):
            if node.left:
                G.add_edge(node.val, node.left.val)
                add_edges(node.left)
            if node.right:
                G.add_edge(node.val, node.right.val)
                add_edges(node.right)

        add_edges(root)

        plt.figure(figsize=(10, 6))
        nx.draw(G, pos, with_labels=True, node_color="lightgreen", node_size=2000, font_size=12)
        plt.title("Binary Search Tree from Sorted Array")
        plt.show()

# Виклик
nums = [-10, -3, 0, 5, 9]
sol = Solution()
tree_root = sol.sortedArrayToBST(nums)
sol.plot_tree(tree_root)