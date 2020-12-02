# 74. Search a 2D Matrix

> Write an efficient algorithm that searches for a value in an *m* x *n* matrix. This matrix has the following properties:
>
> - Integers in each row are sorted from left to right.
> - The first integer of each row is greater than the last integer of the previous row.
>
> **Example 1:**
>
> ```
> Input:
> matrix = [
>   [1,   3,  5,  7],
>   [10, 11, 16, 20],
>   [23, 30, 34, 50]
> ]
> target = 3
> Output: true
> ```
>
> **Example 2:**
>
> ```
> Input:
> matrix = [
>   [1,   3,  5,  7],
>   [10, 11, 16, 20],
>   [23, 30, 34, 50]
> ]
> target = 13
> Output: false
> ```

1. Medium。

```cpp
// 巧妙的问题转换，其实看似要在每一行/列进行二分查找，其实这就是一个分成几行排列的有序序列，直接在逻辑一维上进行二分查找即可。
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if (matrix.empty()) return false;
        auto m=matrix.size(), n=matrix[0].size();
        // [l, r)。
        int l=0, r=m*n, mid, elem;
        while (l < r) {
            mid = l + (r-l)/2;
            elem = matrix[mid/n][mid%n];
            if (elem == target)
                return true;
            else if (elem > target)
                r = mid;
            else
                l = mid+1;
        }
        return false;
    }
};
```

