# 229. Majority Element II

> Given an integer array of size *n*, find all elements that appear more than `⌊ n/3 ⌋` times.
>
> **Note:** The algorithm should run in linear time and in O(1) space.
>
> **Example 1:**
>
> ```
> Input: [3,2,3]
> Output: [3]
> ```
>
> **Example 2:**
>
> ```
> Input: [1,1,1,3,3,2,2,2]
> Output: [1,2]
> ```

1. Medium。
2. https://leetcode.com/problems/majority-element-ii/discuss/63537/My-understanding-of-Boyer-Moore-Majority-Vote

```java
class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
        if not nums:
            return []
        count1, count2, candidate1, candidate2 = 0, 0, 0, 1
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            else:
                count1, count2 = count1 - 1, count2 - 1
        return [n for n in (candidate1, candidate2)
                        if nums.count(n) > len(nums) // 3]
```

