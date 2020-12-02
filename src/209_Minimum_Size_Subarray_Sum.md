# 209. Minimum Size Subarray Sum

> Given an array of **n** positive integers and a positive integer **s**, find the minimal length of a **contiguous** subarray of which the sum ≥ **s**. If there isn't one, return 0 instead.
>
> **Example:** 
>
> ```
> Input: s = 7, nums = [2,3,1,2,4,3]
> Output: 2
> Explanation: the subarray [4,3] has the minimal length under the problem constraint.
> ```
>
> **Follow up:**
>
> If you have figured out the *O*(*n*) solution, try coding another solution of which the time complexity is *O*(*n* log *n*). 

1. Medium。

```cpp
// 滑动窗口，任一时刻仅有一个端点在移动，右端点扩展窗口，左端点收缩窗口。
// 空间复杂度明显是O(1)，时间复杂度为O(N)，因为每个元素最多访问两次，为2*N，所以就是O(N)，不要以为嵌套循环就是O(N^2)。
class Solution {
public:
    int minSubArrayLen(int s, vector<int>& nums) {
        int min=INT_MAX, sum=0;
        auto n = nums.size();
        for (int begin=0, end=0; end<n; end++) {
            sum += nums[end];
            while (sum >= s) {
                min = std::min(min, end-begin+1);
                sum -= nums[begin++];
            }
        }
        return min==INT_MAX? 0: min;
    }
};
```

```cpp
// 原数组是无序的，前缀和数组是有序的（原数组只包含正数），然后将问题转换一下配合二分查找。
class Solution {
public:
    int minSubArrayLen(int s, vector<int>& nums)
    {
        int n = nums.size();
        if (n == 0)
            return 0;
        int ans = INT_MAX;
        vector<int> sums(n + 1, 0); //size = n+1 for easier calculations
        //sums[0]=0 : Meaning that it is the sum of first 0 elements
        //sums[1]=A[0] : Sum of first 1 elements
        //ans so on...
        for (int i = 1; i <= n; i++)
            sums[i] = sums[i - 1] + nums[i - 1];
        for (int i = 1; i <= n; i++) {
            int to_find = s + sums[i - 1];
            auto bound = lower_bound(sums.begin(), sums.end(), to_find);
            if (bound != sums.end()) {
                ans = min(ans, static_cast<int>(bound - (sums.begin() + i - 1)));
            }
        }
        return (ans != INT_MAX) ? ans : 0;
    }
};
```

