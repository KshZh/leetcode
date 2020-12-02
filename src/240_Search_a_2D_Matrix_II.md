# 240. Search a 2D Matrix II

> Write an efficient algorithm that searches for a value in an *m* x *n* matrix. This matrix has the following properties:
>
> - Integers in each row are sorted in ascending from left to right.
> - Integers in each column are sorted in ascending from top to bottom.
>
> **Example:**
>
> Consider the following matrix:
>
> ```
> [
>   [1,   4,  7, 11, 15],
>   [2,   5,  8, 12, 19],
>   [3,   6,  9, 16, 22],
>   [10, 13, 14, 17, 24],
>   [18, 21, 23, 26, 30]
> ]
> ```
>
> Given target = `5`, return `true`.
>
> Given target = `20`, return `false`.

1. Medium。

```cpp
// 也可以在每一行/列应用二分查找，时间复杂度是O(MlogN)。
// 下面这个实现巧妙利用了矩阵的性质，从右上角开始查找。
class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        if (matrix.empty()) return false;
        auto m=matrix.size(), n=matrix[0].size(), half=m*n/2;
        int r=0, c=n-1;
        while (r<m && c>=0) {
            if (matrix[r][c] == target)
                return true;
            else if (matrix[r][c] > target)
                c--;
            else
                r++;
        }
        return false;
    }
};
```

