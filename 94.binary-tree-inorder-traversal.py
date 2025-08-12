class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root):
        result = []

        def traverse(node):
            if not node:
                return
            traverse(node.left)  # 1. Обходимо ліву гілку
            result.append(node.val)  # 2. Додаємо значення вузла
            traverse(node.right)  # 3. Обходимо праву гілку

        traverse(root)
        return result

tree = TreeNode(val=1, left=None, right=TreeNode(2, TreeNode(3), None))

sol = Solution()
print(sol.inorderTraversal(tree))