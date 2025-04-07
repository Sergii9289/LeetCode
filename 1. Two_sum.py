from zoneinfo import reset_tzpath

nums = [1, 2, 5, 7, 11, 15, 16, 8, 4, 21, 22, 5]
target = 9
# if nums.count(target / 2) >= 2:
#     element = target / 2
#     res = sorted([nums.index(element)] + [len(nums) - 1 - nums[::-1].index(element)])
# else:
#     n_list = list({x for x in nums if target - x in nums})
#     res = sorted([nums.index(n_list[0]), nums.index(n_list[-1])])
# print(res)


hash_dict = {}
for index, num in enumerate(nums):
    value = target - num
    if value in hash_dict:
        res = [hash_dict[value], index]
    hash_dict[num] = index
print(res)