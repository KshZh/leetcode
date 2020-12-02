# 329. Longest Increasing Path in a Matrix

> Given an integer matrix, find the length of the longest increasing path.
>
> From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).
>
> **Example 1:**
>
> ```
> Input: nums = 
> [
>   [9,9,4],
>   [6,6,8],
>   [2,1,1]
> ] 
> Output: 4 
> Explanation: The longest increasing path is [1, 2, 6, 9].
> ```
>
> **Example 2:**
>
> ```
> Input: nums = 
> [
>   [3,4,5],
>   [3,2,6],
>   [2,2,1]
> ] 
> Output: 4 
> Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
> ```

1. Hard，DFS，拓扑排序，Memoization。

2. 思路一，从问题出发的DP，DFS+Memoization。（这道题初看DP的边界不明显，所以这时可以考虑一下从问题出发的DP）。

3. 思路二，从边界出发的DP，最大堆，因为从矩阵中最大的元素出发的上升序列的长度必定为1，这就是边界。

4. 思路三，拓扑排序。（看问题和分析问题的角度值得学习）

5. ```cpp
   if (p == last) {
       level++;
       if (!q.empty()) // XXX 注意这里必须先判断队列非空然后才可以用back()。
           last = q.back();
   }
   ```

```cpp
// 思路一。
// 时间和空间复杂度都为O(N*M)，N*M是矩阵大小。
class Solution {
    vector<vector<int>> cache; // 也可以称为dp数组。dp的从问题出发的方向很像记忆化搜索。
    size_t m, n;
    vector<pair<int, int>> dirs{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        m = matrix.size();
        if (m == 0) return 0;
        n = matrix[0].size();
        cache = vector(m, vector<int>(n, 0));
        int maxLen = INT_MIN;
        // 考察从每个cell出发的上升序列，取其中最长的那个序列。
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                maxLen = max(maxLen, dfs(matrix, i, j));
            }
        }
        return maxLen;
    }
    
    int dfs(vector<vector<int>>& matrix, int i, int j) {
        if (cache[i][j]) return cache[i][j]; // 有cache数组充当visited数组的作用。
        // 注意这里不能惯性地初始化为INT_MIN，应初始化为1，因为从该cell出发的上升序列最短为该cell本身。
        int x, y, maxLen=1;
        // 遍历四个方向。
        for (const auto& dir: dirs) {
            x = i+dir.first;
            y = j+dir.second;
            if (x<0 || x>=m || y<0 || y>=n || matrix[x][y]<=matrix[i][j])
                continue;
            maxLen = max(maxLen, dfs(matrix, x, y) + 1);
        }
        cache[i][j] = maxLen;
        return maxLen;
    }
};
```

```cpp
// 思路二。
auto cmp = [](const vector<int>& a, const vector<int>& b) {
    return a[2]<b[2];  
};

class Solution {
    size_t m, n;
    vector<pair<int, int>> dirs{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        m = matrix.size();
        if (m == 0) return 0;
        n = matrix[0].size();
        vector<vector<int>> dp(m, vector<int>(n, 0));
        priority_queue<vector<int>, vector<vector<int>>, decltype(cmp)> q(cmp);
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                q.push({i, j, matrix[i][j]});
            }
        }
        int maxLen = INT_MIN, x, y, i, j;
        vector<int> z;
        while (!q.empty()) {
            z = q.top();
            q.pop();
            i=z[0], j=z[1];
            dp[i][j] = 1;
            // 遍历四个方向。
            for (const auto& dir: dirs) {
                x = i+dir.first;
                y = j+dir.second;
                if (x<0 || x>=m || y<0 || y>=n || matrix[x][y]<=matrix[i][j])
                    continue;
                dp[i][j] = max(dp[i][j], dp[x][y]+1);
            }
            maxLen = max(maxLen, dp[i][j]);
        }
        return maxLen;
    }
};
```

```cpp
// 思路三。
class Solution {
    size_t m, n;
    vector<pair<int, int>> dirs{{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
public:
    int longestIncreasingPath(vector<vector<int>>& matrix) {
        m = matrix.size();
        if (m == 0) return 0;
        n = matrix[0].size();
        int x, y, i, j;
        vector<vector<int>> indegree(m, vector<int>(n, 0));
        for (i=0; i<m; i++) {
            for (j=0; j<n; j++) {
                for (const auto& dir: dirs) {
                    x = i+dir.first;
                    y = j+dir.second;
                    if (x>=0 && x<m && y>=0 && y<n && matrix[x][y]>matrix[i][j]) {
                        indegree[x][y]++;
                    } 
                }
            }
        }
        return topSort(indegree, matrix);
    }
    
    int topSort(vector<vector<int>>& indegree, vector<vector<int>>& matrix) {
        int i, j, x, y;
        pair<int, int> p;
        queue<pair<int, int>> q;
        for (i=0; i<m; i++) {
            for (j=0; j<n; j++) {
                if (indegree[i][j] == 0)
                    q.push({i, j});
            }
        }
        int level = 0;
        pair<int, int> last = q.back();
        while (!q.empty()) {
            p = q.front();
            q.pop();
            i=p.first, j=p.second;
            for (const auto& dir: dirs) {
                x = i+dir.first;
                y = j+dir.second;
                // 如果当前结点有边指向另一个结点，则删除这条边。
                if (x>=0 && x<m && y>=0 && y<n && matrix[x][y]>matrix[i][j]) {
                    if (--indegree[x][y] == 0)
                        q.push({x, y});
                }
            }
            if (p == last) {
                level++;
                if (!q.empty()) // XXX 注意这里必须先判断队列非空然后才可以用back()。
                    last = q.back();
            }
        }
        return level;
    }
};
```

