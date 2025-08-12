/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    const hashDict = {};
    for (const [index, v] of nums.entries()) {
        const value = target - v;
        if (value in hashDict) {
          return[hashDict[value], index];
        }
        hashDict[v] = index;
    }
    return []
};

const nums = [2, 7, 11, 15];
const target = 9;

const result = twoSum(nums, target);
console.log(result); // [0, 1]