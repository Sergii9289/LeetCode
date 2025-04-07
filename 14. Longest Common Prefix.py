strs = ["flower","flow","flight"]
min_lens = min([len(x) for x in strs])
res = ''
for i in range(min_lens):
    letter = strs[0][:i+1]
    # print(letter)
    for j in strs:
        if not j.startswith(letter):
            break
    else:
        res = letter
        continue
    break

print(res)