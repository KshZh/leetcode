# 279. Perfect Squares

> Given a positive integer *n*, find the least number of perfect square numbers (for example, `1, 4, 9, 16, ...`) which sum to *n*.
>
> **Example 1:**
>
> ```
> Input: n = 12
> Output: 3 
> Explanation: 12 = 4 + 4 + 4.
> ```
>
> **Example 2:**
>
> ```
> Input: n = 13
> Output: 2
> Explanation: 13 = 4 + 9.
> ```

1. Medium，dp，bfs，math。
2. 不需要先建树/图，只需把起点加入队列，之后把逻辑上邻接的结点也加入队列，这就实现了搜索。

```cpp
class Solution {
public:
    int numSquares(int n) {
        if (n == 0) return 0;
        // dp[i]表示数字i是至少dp[i]个完美平方数的和。
        vector<int> dp(n+1, INT_MAX);
        dp[0] = 0; // 边界。
        for (int i=1; i<=n; i++) {
            for (int j=1; j*j<=i; j++) {
                dp[i] = min(dp[i], dp[i-j*j]+1);
            }
        }
        return dp[n];
    }
};
```

```cpp
// 比如n为14，bfs的过程是：（!()表示比n大，不考虑）
// 1 4 9
// 2 5 10 8 13 !(18)
// 3 6 11 12 !(17) 14 [...]
// 这个bfs过程并不需要先建树/图，只需要把逻辑上是起点的结点压入queue中即可，之后逻辑上邻接的结点也压入queue即可实现搜索。
// 而且这个bfs有个特点就是，下一层是在搜索时实时由当前层计算出来并入队的。
class Solution {
public:
    int numSquares(int n) {
        if (n == 0) return 0;
        vector<int> perfectSquares;
        for (int i=1; i*i<=n; i++)
            perfectSquares.push_back(i*i);
        if (perfectSquares.back() == n)
            return 1;
        queue<int> q;
        vector<bool> visited(n);
        for (int x: perfectSquares) {
            q.push(x);
            visited[x] = true;
        }
        int level = 2, x;
        int last = q.back();
        while (!q.empty()) {
            x = q.front();
            q.pop();
            for (int y: perfectSquares) {
                if (x+y == n)
                    return level;
                if (x+y > n) break; // 因为perfectSquares是递增序列，所以满足该条件时，y后面的元素也都满足，所以可以提前结束循环。
                if (x+y<n && !visited[x+y]) {
                    q.push(x+y);
                    visited[x+y] = true;
                }
            }
            if (x == last) {
                if (!q.empty())
                    last = q.back();
                level++;
            }
        }
        return -1;
    }
};
```

