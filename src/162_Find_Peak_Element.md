# 162. Find Peak Element

> A peak element is an element that is greater than its neighbors.
>
> Given an input array `nums`, where `nums[i] ≠ nums[i+1]`, find a peak element and return its index.
>
> The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.
>
> You may imagine that `nums[-1] = nums[n] = -∞`.
>
> **Example 1:**
>
> ```
> Input: nums = [1,2,3,1]
> Output: 2
> Explanation: 3 is a peak element and your function should return the index number 2.
> ```
>
> **Example 2:**
>
> ```
> Input: nums = [1,2,1,3,5,6,4]
> Output: 1 or 5 
> Explanation: Your function can return either index number 1 where the peak element is 2, 
>              or index number 5 where the peak element is 6.
> ```
>
> **Note:**
>
> Your solution should be in logarithmic complexity.

1. Medium。

![](https://leetcode.com/problems/find-peak-element/Figures/162/Find_Peak_Case1.PNG)

![](https://leetcode.com/problems/find-peak-element/Figures/162/Find_Peak_Case2.PNG)

![](https://leetcode.com/problems/find-peak-element/Figures/162/Find_Peak_Case3.PNG)

```cpp
// 很容易写出O(N)的实现。
class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        if (nums.empty()) return -1;
        auto n = nums.size();
        if (n==1 || nums[0]>nums[1]) return 0;
        if (nums[n-1] > nums[n-2]) return n-1;
        for (int i=1; i<n-1; i++) {
            if (nums[i]>nums[i-1] && nums[i]>nums[i+1])
                return i;
        }
        return -1;
    }
};
```

```cpp
// 提到搜索需要O(logN)时间复杂度，那肯定考虑二分查找。
class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        if (nums.empty()) return -1;
        auto n = nums.size();
        if (n==1 || nums[0]>nums[1]) return 0;
        if (nums[n-1] > nums[n-2]) return n-1;
        int l=0, r=n, mid;
        while (l < r) {
            mid = l+(r-l)/2;
            if (nums[mid]>nums[mid-1] && nums[mid]>nums[mid+1])
                return mid;
            else if (nums[mid]<nums[mid-1])
                r = mid;
            else
                l = mid+1;
        }
        return -1;
    }
};
```

```cpp
// 代码简化如下：
class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        for (int i=0; i<nums.size()-1; i++) {
            if (nums[i] > nums[i+1])
                return i;
        }
        return nums.size()-1;
    }
};
```

```cpp
class Solution {
public:
    int findPeakElement(vector<int>& nums) {
        int l=0, r=nums.size()-1, mid; // 区间是[l, r]，这有一个好处是自然地处理了nums.size()为1的情况。
        while (l < r) { // 不是`l <= r`，那么就在循环外返回，否则在循环中返回。
            mid = l + (r-l)/2;
            if (nums[mid] > nums[mid+1])
                r = mid; // 一边满足，固定r，然后向右找山峰，让l往r靠。
            else
                l = mid+1;
        }
        // l==r==mid。
        return l;
    }
};
```

