class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):  # Усуваємо проблему ділення на нуль
            return s

        nums_in_zig = 2 * numRows - 2
        n_zig, str_ost = divmod(len(s), nums_in_zig)
        cols = (nums_in_zig // 2) * n_zig + (0 if str_ost == 0 else 1 if str_ost <= numRows else 1 + (str_ost % numRows))

        two_l_list = [['' for _ in range(numRows)] for _ in range(cols)]
        row, col, direction = 0, 0, 1

        for char in s:
            two_l_list[col][row] = char
            if row == 0:
                direction = 1  # Йдемо вниз
            elif row == numRows - 1:
                direction = -1  # Йдемо вгору
            row += direction
            if direction == -1 or row == 0:
                col += 1

        return ''.join([''.join(row) for row in zip(*two_l_list)])

s = "P"
numRows = 1
a = Solution()
print(a.convert(s, numRows))  # Виведе "P"