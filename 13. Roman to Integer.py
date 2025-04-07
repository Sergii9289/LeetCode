s = "MCMXCIV"
rome_dict = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
res = 0
curr = 0
for i in reversed(s):
    if rome_dict[i] >= curr:
        res += rome_dict[i]
    else:
        res -= rome_dict[i]
    curr = rome_dict[i]
print(res)