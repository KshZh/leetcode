# 300. Longest Increasing Subsequence

> Given an unsorted array of integers, find the length of longest increasing subsequence.
>
> **Example:**
>
> ```
> Input: [10,9,2,5,3,7,101,18]
> Output: 4 
> Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4. 
> ```
>
> **Note:**
>
> - There may be more than one LIS combination, it is only necessary for you to return the length.
> - Your algorithm should run in O(*n2*) complexity.
>
> **Follow up:** Could you improve it to O(*n* log *n*) time complexity?

1. Medium。
2. https://en.wikipedia.org/wiki/Longest_increasing_subsequence#Efficient_algorithm

![](https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/LISDemo.gif/600px-LISDemo.gif)

```cpp
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        auto n = nums.size();
        if (n == 0) return 0;
        // dp[i]表示以nums[i]结尾的最长上升子序列的长度。
        // 边界是`dp[i]=1`。
        vector<int> dp(n, 1);
        // max_初始值设置为INT_MAX不好，这样如果只有一个元素，那么就会返回INT_MIN，实际应该返回1。
        int i, j, max_=1;
        for (i=1; i<n; i++) {
            for (j=0; j<i; j++) {
                if (nums[j] < nums[i])
                    dp[i] = max(dp[i], dp[j]+1);
            }
            if (dp[i] > max_) max_=dp[i];
        }
        return max_;
    }
};
```

```cpp
class Solution {
public:
    int lengthOfLIS(vector<int>& nums) {
        auto n = nums.size();
        if (n == 0) return 0;
        vector<int> dp(n); // dp[i]表示多个长度为i+1的上升子序列中的含有最小后缀元素的那个上升子序列，这样最有利于扩展该上升子序列。
        int l, r, mid, maxLen=0;
        for (int num: nums) {
            // 找到第一个大于等于num的dp[i]。
            l=0, r=maxLen;
            while (l < r) {
                mid = l+(r-l)/2;
                if (dp[mid] >= num) r=mid; // 用r暂存，但缩小范围继续找，试图找到第一个。
                else l=mid+1;
            }
            dp[r] = num;
            if (r == maxLen) maxLen++;
        }
        return maxLen;
    }
};
```

