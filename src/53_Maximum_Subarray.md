# 53. Maximum Subarray

> Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
>
> **Example:**
>
> ```
> Input: [-2,1,-3,4,-1,2,1,-5,4],
> Output: 6
> Explanation: [4,-1,2,1] has the largest sum = 6.
> ```

1. Easy，DP。
2. [贪心，分治](https://github.com/KshZh/ZJU-data-structure/blob/master/01%20%E5%9F%BA%E6%9C%AC%E6%A6%82%E5%BF%B5/solution.md)。

```cpp
class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        vector<int> dp(nums.size()); // dp[i]表示以nums[i]结尾的连续子序列和。
        // 状态转移方程：dp[i] = max(nums[i], nums[i]+dp[i-1]);
        dp[0] = nums[0];
        int max_ = dp[0];
        for (int i=1; i<nums.size(); i++) {
            dp[i] = max_(nums[i], dp[i-1]+nums[i]);
            if (dp[i] > max_)
                max_ = dp[i];
        }
        return max_;
    }
};
```

