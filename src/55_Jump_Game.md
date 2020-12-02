# 55. Jump Game

> Given an array of non-negative integers, you are initially positioned at the first index of the array.
>
> Each element in the array represents your maximum jump length at that position.
>
> Determine if you are able to reach the last index.
>
> **Example 1:**
>
> ```
> Input: [2,3,1,1,4]
> Output: true
> Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
> ```
>
> **Example 2:**
>
> ```
> Input: [3,2,1,0,4]
> Output: false
> Explanation: You will always arrive at index 3 no matter what. Its maximum
>              jump length is 0, which makes it impossible to reach the last index.
> ```

1. Medium。

```cpp
class Solution {
public:
    bool canJump(vector<int>& nums) {
        // TLE。
        auto n = nums.size();
        // dp[i]表示从i出发能否到达最后一个位置。
        vector<bool> dp(n);
        dp[n-1] = true; // 边界。
        int i, j, end;
        for (i=n-2; i>=0; i--) {
            // 这里注意取小值，避免越界。
            end = n-1<i+nums[i]? n-1: i+nums[i];
            for (j=i+1; j<=end; j++) {
                if (dp[j]) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[0];
    }
};
```

```java
// 贪心，tricky。
public class Solution {
    public boolean canJump(int[] nums) {
        int lastPos = nums.length - 1;
        for (int i = nums.length - 2; i >= 0; i--) {
            if (i + nums[i] >= lastPos) {
                lastPos = i;
            }
        }
        return lastPos == 0;
    }
}
```

```cpp
// 贪心。
bool canJump(int A[], int n) {
    int i = 0;
    // I just iterate and update the maximal index that I can reach.
    for (int reach = 0; i < n && i <= reach; ++i)
        reach = max(i + A[i], reach);
    return i == n;
}
```

