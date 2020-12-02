# 766. Toeplitz Matrix

> A matrix is *Toeplitz* if every diagonal from top-left to bottom-right has the same element.
>
> Now given an `M x N` matrix, return `True` if and only if the matrix is *Toeplitz*.
>  
>
> **Example 1:**
>
> ```
> Input:
> matrix = [
>   [1,2,3,4],
>   [5,1,2,3],
>   [9,5,1,2]
> ]
> Output: True
> Explanation:
> In the above grid, the diagonals are:
> "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", "[3, 3]", "[4]".
> In each diagonal all elements are the same, so the answer is True.
> ```
>
> **Example 2:**
>
> ```
> Input:
> matrix = [
>   [1,2],
>   [2,2]
> ]
> Output: False
> Explanation:
> The diagonal "[1, 2]" has different elements.
> ```
>
>
> **Note:**
>
> 1. `matrix` will be a 2D array of integers.
> 2. `matrix` will have a number of rows and columns in range `[1, 20]`.
> 3. `matrix[i][j]` will be integers in range `[0, 99]`.
>
>
> **Follow up:**
>
> 1. What if the matrix is stored on disk, and the memory is limited such that you can only load at most one row of the matrix into the memory at once?
>
>    用第二个实现。
>
> 2. What if the matrix is so large that you can only load up a partial row into the memory at once?

1. Easy。

```cpp
class Solution {
public:
    bool isToeplitzMatrix(vector<vector<int>>& matrix) {
        if (matrix.size() <= 1) return true;
        // 观察测试样例可知，若一行有n列，
        // 那么该行的后n-1个元素要与上一行的前n-1个元素一一对应相等。
        auto m=matrix.size(), n=matrix[0].size();
        int r, c;
        for (r=1; r<m; r++) {
            for (c=1; c<n; c++) {
                if (matrix[r-1][c-1] != matrix[r][c])
                    return false;
            }
        }
        return true;
    }
};
```

```cpp
// 按对角线分类，如果两个元素在同一对角线上，那么`r1-c1==r2-c2`。
class Solution {
public:
    bool isToeplitzMatrix(vector<vector<int>>& matrix) {
        if (matrix.size() <= 1) return true;
        auto m=matrix.size(), n=matrix[0].size();
        unordered_map<int, int> groups;
        int r, c;
        for (r=1; r<m; r++) {
            for (c=1; c<n; c++) {
                if (groups.find(r-c) == groups.end())
                    groups[r-c] = matrix[r][c];
                else if (groups[r-c] != matrix[r][c])
                    return false;
            }
        }
        return true;
    }
};
```

