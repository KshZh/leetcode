# 120. Triangle

> Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
>
> For example, given the following triangle
>
> ```
> [
>      [2],
>     [3,4],
>    [6,5,7],
>   [4,1,8,3]
> ]
> ```
>
> The minimum path sum from top to bottom is `11` (i.e., **2** + **3** + **5** + **1** = 11).
>
> **Note:**
>
> Bonus point if you are able to do this using only *O*(*n*) extra space, where *n* is the total number of rows in the triangle.

1. Medium。

```cpp
// 记忆化dfs。
class Solution {
    unordered_map<int, unordered_map<int, int>> cache;
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        return dfs(triangle, 0, 0);
    }
    
    // XXX 明确递归函数的输入输出，输入一个起点，输出从该起点出发的多条路径中最小的路径和。
    int dfs(const vector<vector<int>>& triangle, int row, int col) {
        if (row == triangle.size()-1) return triangle[row][col];
        if (cache.find(row)!=cache.end() && cache[row].find(col)!=cache[row].end())
            return cache[row][col];
        int x1 = dfs(triangle, row+1, col);
        int x2 = dfs(triangle, row+1, col+1);
        // 这里不需要检查col+1是否溢出，因为根据杨辉三角的特点，当前行的最后一个元素，对应于同一列的下一行的最后第二个元素。所以只需要检查行不要溢出就行了。
        cache[row][col] = min(x1, x2)+triangle[row][col];
        return min(x1, x2)+triangle[row][col];
    }
};
```

```cpp
// 从边界出发的dp。
class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        // 滚动数组。
        // dp[j]表示从第i行第i列出发的多条路径中最小的路径和。
        vector<int> dp(triangle.back());
        for (int i=triangle.size()-2; i>=0; i--) {
            // 从第0行开始，第i行有i+1个元素，最后一个元素的下标是i。
            for (int j=0; j<=i; j++) { // 注意要顺序处理，这样才不会覆盖下一层未被使用的旧值。
                dp[j] = min(dp[j], dp[j+1])+triangle[i][j];
            }
        }
        return dp[0];
    }
};
```

