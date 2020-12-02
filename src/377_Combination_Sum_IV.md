# 377. Combination Sum IV

> Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.
>
> **Example:**
>
> ```
> nums = [1, 2, 3]
> target = 4
> 
> The possible combination ways are:
> (1, 1, 1, 1)
> (1, 1, 2)
> (1, 2, 1)
> (1, 3)
> (2, 1, 1)
> (2, 2)
> (3, 1)
> 
> Note that different sequences are counted as different combinations.
> 
> Therefore the output is 7.
> ```
>
> **Follow up:**
> What if negative numbers are allowed in the given array?
> How does it change the problem?
> What limitation we need to add to the question to allow negative numbers?
>
> **Credits:**
> Special thanks to [@pbrother](https://leetcode.com/pbrother/) for adding this problem and creating all test cases.

1. Medium。
2. 典型背包问题是组合问题，这道题类似背包问题，但是排列问题。
3. 类似题目[518. Coin Change 2](./src/518_Coin_Change_2.md)，但是组合问题。

```cpp
class Solution {
    unordered_map<int, int> book;
public:
    int combinationSum4(vector<int>& nums, int target) {
        return dfs(nums, target);
    }
    
    int dfs(vector<int>& nums, int target) {
        if (target < 0) return 0;
        if (target == 0) return 1;
        if (book.find(target) != book.end()) return book[target];
        int cnt = 0;
        for (int num: nums) {
            cnt += dfs(nums, target-num);
        }
        book[target] = cnt;
        return cnt;
    }
};
```

```cpp
class Solution {
public:
    int combinationSum4(vector<int>& nums, int target) {
        vector<unsigned int> dp(target+1);
        dp[0] = 1;
        // 排列问题，双层循环不能反过来，这样dp[i][j]用到的就是dp[nums.size()-1][j-num]了，也就是在所有num上的排列个数，而不是在部分num上的排列个数，即不是dp[i][j-num]。
        for (int j=1; j<=target; j++) {
            for (int num: nums) { // 对于每一个num，用或不用。
                if (j>=num)
                    dp[j] += dp[j-num];
            }
        }
        return dp[target];
    }
};
```

