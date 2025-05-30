class Solution:
    def isValid(self, s: str) -> bool:
        # Dictionary to store valid matching pairs of brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            if char in bracket_map:
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack


solution = Solution()
result = solution.isValid('()')
print(result)