# 198. House Robber

> You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and **it will automatically contact the police if two adjacent houses were broken into on the same night**.
>
> Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight **without alerting the police**.
>
> **Example 2:**
>
> ```
> Input: [2,7,9,3,1]
> Output: 12
> Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
>              Total amount you can rob = 2 + 9 + 1 = 12.
> ```

1. Easy，DP。
2. 算法不行，可能就是边界没处理正确。

```cpp
class Solution {
public:
    int rob(vector<int>& nums) {
        if (nums.empty())
            return 0;
        if (nums.size() == 1)
            return nums[0];
        vector<int> dp(nums.size()); // dp[i]表示num[0, i]可以获取的最大收益。
        dp[0] = nums[0];
        dp[1] = max(nums[0], nums[1]); // XXX 注意这个边界的初始化，算法不行，可能就是边界没处理正确。
        for (int i=2; i<nums.size(); i++) {
            dp[i] = max(dp[i-1], dp[i-2]+nums[i]); // 不偷当前房子，或者偷当前房子。
            // 可以看到，一次循环只会用到前两个dp元素，那么为了节省空间，可以不维护dp数组，而只使用三个变量。
        }
        return dp[nums.size()-1];
    }
};
```

