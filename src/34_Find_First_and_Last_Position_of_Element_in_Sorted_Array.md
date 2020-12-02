# 34. Find First and Last Position of Element in Sorted Array

> Given an array of integers `nums` sorted in ascending order, find the starting and ending position of a given `target` value.
>
> Your algorithm's runtime complexity must be in the order of *O*(log *n*).
>
> If the target is not found in the array, return `[-1, -1]`.
>
> **Example 1:**
>
> ```
> Input: nums = [5,7,7,8,8,10], target = 8
> Output: [3,4]
> ```
>
> **Example 2:**
>
> ```
> Input: nums = [5,7,7,8,8,10], target = 6
> Output: [-1,-1]
> ```

1. Medium，二分查找。

```cpp
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        if (nums.empty()) return {-1, -1};
        // 两次二分查找，
        // 第一次找最后一个小于target的元素，
        // 第二次找第一个大于target的元素。
        int l=0, r=nums.size(), mid;
        while (l < r) {
            mid = (l+r)/2;
            if (nums[mid] < target)
                // 也就是mid及其左边的元素都小于target，
                // 用l-1暂存这个目前可能是“最后一个”小于target的元素的位置，
                // 并往mid右边去找，看是否还有小于target的元素。
                l = mid+1;
            else
                r = mid;
        }
        // 结束后，l-1指向最后一个小于target的元素，
        // 则l指向等于target的元素才对。
        // 如果l不在数组范围内或l指向的元素不等于target，
        // 说明target不在数组中。
        if (l==nums.size() || nums[l] != target) return {-1, -1};
        int start = l;
        l=0, r=nums.size();
        while (l < r) {
            mid = (l+r)/2;
            if (nums[mid] > target)
                // 说明mid及其右边都大于target，
                // 往左边找，试图找到第一个大于target的元素，
                // 且此时先用r存放目前可能是“第一个”大于target的元素的位置。
                r = mid;
            else
                l = mid+1;
        }
        return {start, r-1};
    }
};
```

```cpp
// tricky.
class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        if (nums.empty()) return {-1, -1};
        // 两次二分查找，
        // 第一次找最后一个小于target的元素，
        // 第二次找第一个大于target的元素。
        int start = upper_bound(nums, target-0.5);
        if (start==nums.size() || nums[start]!=target) return {-1, -1};
        return {start, upper_bound(nums, target+0.5)-1};
    }
    
    // 找到第一个大于target的元素。
    int upper_bound(vector<int>& nums, float target) {
        int l=0, r=nums.size(), mid;
        while (l < r) {
            mid = (l+r)/2;
            if (nums[mid] > target)
                // 说明mid及其右边都大于target，
                // 往左边找，试图找到第一个大于target的元素，
                // 且此时先用r存放目前可能是“第一个”大于target的元素的位置。
                r = mid;
            else
                l = mid+1;
        }
        return r;
    }
};
```

