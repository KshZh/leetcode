# 33. Search in Rotated Sorted Array

> Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
>
> (i.e., `[0,1,2,4,5,6,7]` might become `[4,5,6,7,0,1,2]`).
>
> You are given a target value to search. If found in the array return its index, otherwise return `-1`.
>
> You may assume no duplicate exists in the array.
>
> Your algorithm's runtime complexity must be in the order of *O*(log *n*).
>
> **Example 1:**
>
> ```
> Input: nums = [4,5,6,7,0,1,2], target = 0
> Output: 4
> ```
>
> **Example 2:**
>
> ```
> Input: nums = [4,5,6,7,0,1,2], target = 3
> Output: -1
> ```

1. Medium，广义二分查找。

```cpp
class Solution {
public:
    int search(vector<int>& nums, int target) {
        auto n = nums.size();
        int l=0, r=n-1, mid, realMid;
        while (l < r) {
            mid = (l+r)/2;
            if (nums[mid] > nums[r]) l=mid+1; // 违反了单调递增，所以最小的元素一定在mid和r之间。
            else r=mid;
        }
        int offset = l; // 最终`l==r`，指向最小元，即上升序列的起点。
        l=0, r=n;
        while (l < r) {
            mid = (l+r)/2;
            realMid = (mid+offset)%n;
            if (nums[realMid] == target) return realMid;
            else if (nums[realMid] < target) l = mid+1; // 要增大realMid，就要增大l，而不是减小r。
            else r = mid;
        }
        return -1;
    }
};
```

