# 334. Increasing Triplet Subsequence

> Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

1. 存在性问题，Medium。

```cpp
class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        // 因为只需要判断是否存在一个递增的三元组子序列，所以只需考虑最容易满足的情况，即
        // 遍历时维护已遍历序列中的一个最小元和一个次小元，如果在未遍历序列中遍历到一个元素大于这两个元，那就存在。
        int firstMin=INT_MAX, secondMin=INT_MAX;
        for (int x: nums) {
            if (x <= firstMin) firstMin = x;
            else if (x <= secondMin) secondMin = x;
            else return true;
        }
        return false;
    }
};
```

```cpp
// 时空都是O(N)。
// 前缀最小，后缀最大，枚举a<b<c中的b。
class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        auto n = nums.size();
        if (n < 3) return false;
        vector<int> min(n, INT_MAX), max(n, INT_MIN);
        min[0] = nums[0];
        for (int i=1; i<n; i++) {
            if (nums[i] < min[i-1])
                min[i] = nums[i];
            else
                min[i] = min[i-1];
        }
        max[n-1] = nums[n-1];
        for (int i=n-2; i>=0; i--) {
            if (nums[i] > max[i+1])
                max[i] = nums[i];
            else
                max[i] = max[i+1];
        }
        for (int i=1; i<n-1; i++) {
            if (nums[i]>min[i] && nums[i]<max[i])
                return true;
        }
        return false;
    }
};
```

