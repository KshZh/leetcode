# 213. House Robber II

> You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are **arranged in a circle.** That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have security system connected and **it will automatically contact the police if two adjacent houses were broken into on the same night**.
>
> Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight **without alerting the police**.
>
> **Example 1:**
>
> ```
> Input: [2,3,2]
> Output: 3
> Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2),
>              because they are adjacent houses.
> ```
>
> **Example 2:**
>
> ```
> Input: [1,2,3,1]
> Output: 4
> Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
>              Total amount you can rob = 1 + 3 = 4.
> ```

1. Medium。

```java
class Solution {
    public int rob(int[] nums) {
        if (nums.length == 1) return nums[0];
        return Math.max(rob(nums, 0, nums.length-1), rob(nums, 1, nums.length));
    }
    
    // [lo, hi).
    private int rob(int[] nums, int lo, int hi) {
        // 因为dp[i]只有dp[i-1]和dp[i-2]确定，
        // 所以可以不用一维数组，而用两个变量。
        int include = 0, exclude = 0;
        for (int j = lo; j < hi; j++) {
            int i = include, e = exclude;
            include = e + nums[j];
            exclude = Math.max(e, i);
        }
        return Math.max(include, exclude);
    }
}
```

