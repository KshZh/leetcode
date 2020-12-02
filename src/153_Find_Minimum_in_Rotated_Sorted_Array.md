# 153. Find Minimum in Rotated Sorted Array

> Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
>
> (i.e.,  `[0,1,2,4,5,6,7]` might become  `[4,5,6,7,0,1,2]`).
>
> Find the minimum element.
>
> You may assume no duplicate exists in the array.
>
> **Example 1:**
>
> ```
> Input: [3,4,5,1,2] 
> Output: 1
> ```
>
> **Example 2:**
>
> ```
> Input: [4,5,6,7,0,1,2]
> Output: 0
> ```

1. Medium。

```cpp
// 基于index的二分查找。
class Solution {
public:
    int findMin(vector<int>& nums) {
        int l=0, r=nums.size()-1, mid;
        while (l < r) {
            // mid = (l+r)/2; // 加法可能溢出。
            mid = l + (r-l)/2;
            if (nums[mid] > nums[r]) // 不符合递增序列，那么起点一定在(mid, r]之间。
                l = mid+1;
            else
                r = mid;
        }
        // `l==r`.
        return nums[l];
    }
};
```

