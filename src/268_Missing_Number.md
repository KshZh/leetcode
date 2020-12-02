# 268. Missing Number

> Given an array containing *n* distinct numbers taken from `0, 1, 2, ..., n`, find the one that is missing from the array.
>
> **Example 1:**
>
> ```
> Input: [3,0,1]
> Output: 2
> ```
>
> **Example 2:**
>
> ```
> Input: [9,6,4,2,3,5,7,0,1]
> Output: 8
> ```
>
> **Note**:
> Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

1. Easy。

```cpp
// 使用排序，需要O(NlogN)时间复杂度，O(1)或O(N)空间复杂度，如果不能修改参数的话。
// 使用哈希表，需要O(N)空间复杂度。
// 对于[0, 1, 3, 4]，missing=4∧(0∧0)∧(1∧1)∧(2∧3)∧(3∧4)=(4∧4)∧(0∧0)∧(1∧1)∧(3∧3)∧2=0∧0∧0∧0∧2=2
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int missing = nums.size();
        for (int i=0; i<nums.size(); i++) {
            missing ^= i^nums[i];
        }
        return missing;
    }
};
```

```cpp
// 先求出[1, n]的和，然后减去nums数组所有元素的和，就得到缺失的元素了。
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int expectedSum = nums.size()*(nums.size()+1)/2; // 等差数列和=(首项+尾项)*项数/2。
        int actualSum = 0;
        for (int num: nums) actualSum += num;
        return expectedSum-actualSum;
    }
};
```

