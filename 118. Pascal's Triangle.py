from typing import List

def generate(numRows: int) -> List[List[int]]:
    i = 1
    res = [[0, 1, 0]]
    while i < numRows:
        t1 = res[-1]
        temp = [0] * (i + 3)
        for j in range(i + 1):
            temp[j + 1] = t1[j] + t1[j + 1]
        i += 1
        res.append(temp)
    cleaned = [row[1:-1] for row in res]
    return cleaned


print(generate(5))