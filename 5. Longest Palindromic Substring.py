
def find_palindromes(s):
    palindromes = set()

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            palindromes.add(s[left:right+1])
            left -= 1
            right += 1

    for i in range(len(s)):
        expand_around_center(i, i)       # Паліндроми непарної довжини
        expand_around_center(i, i + 1)   # Паліндроми парної довжини

    return list(palindromes)

s = "babad"
res = find_palindromes(s)
print(res)