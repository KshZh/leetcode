# 130. Surrounded Regions

> Given a 2D board containing `'X'` and `'O'` (**the letter O**), capture all regions surrounded by `'X'`.
>
> A region is captured by flipping all `'O'`s into `'X'`s in that surrounded region.
>
> **Example:**
>
> ```
> X X X X
> X O O X
> X X O X
> X O X X
> ```
>
> After running your function, the board should be:
>
> ```
> X X X X
> X X X X
> X X X X
> X O X X
> ```
>
> **Explanation:**
>
> Surrounded regions shouldn’t be on the border, which means that any `'O'` on the border of the board are not flipped to `'X'`. Any `'O'` that is not on the border and it is not connected to an `'O'` on the border will be flipped to `'X'`. Two cells are connected if they are adjacent cells connected horizontally or vertically.

1. Medium。
2. 一开始是想从内部的'O'出发，然后dfs，如果遇到了在边界的'O'，那就在回来的时候把路径上的'O'都变成'X'。但发现就是最后一部不好实现。
3. 换个角度，从边界上的'O'出发，dfs，把路径上的'O'都变成'1'，最后把没标记成'1'的'O'都变成'X'，把标记为'1'的'O'还原回来。
4. 另一个思路是使用并查集，把边界上的'O'加入一个集合A中（因为边界上的'O'可能不止一个且位置不固定，所以设置一个dummy头目，而不是在边界的'O'中选一个），然后相邻的'O'也连接起来，如果相邻的'O'中其中一个在集合A中，那么另一个连接后也会在集合A中。

```cpp
class Solution {
    size_t m, n;
    const int direction[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
public:
    void solve(vector<vector<char>>& board) {
        if (board.empty()) return;
        m=board.size(), n=board[0].size();
        int i, j;
        for (i=0; i<m; i++) {
            dfs(i, 0, board);
            if (n > 1) dfs(i, n-1, board);
        }
        for (j=1; j<n-1; j++) {
            dfs(0, j, board);
            if (m > 1) dfs(m-1, j, board);
        }
        for (i=0; i<m; i++) {
            for (j=0; j<n; j++) {
                if (board[i][j] == 'O') board[i][j] = 'X';
                if (board[i][j] == '1') board[i][j] = 'O';
            }
        }
    }
    
    void dfs(int i, int j, vector<vector<char>>& board) {
        if (board[i][j]=='X' || board[i][j]=='1') return;
        board[i][j] = '1';
        int x, y;
        for (int k=0; k<4; k++) {
            x = i+direction[k][0];
            y = j+direction[k][1];
            if (x>=0 && x<m && y>=0 && y<n) {
                dfs(x, y, board);
            }
        }
    }
};
```

```CPP
class Solution {
    struct UF {
        vector<int> parent;
        UF(int n): parent(n) {
            for (int i=0; i<n; i++)
                parent[i] = i;
        }
        
        // 找到集合中的头目。
        int find(int u) {
            if (parent[u] != u) {
                parent[u] = find(parent[u]);
            }
            return parent[u];
        }
        
        void union_(int u, int v) {
            int pu = find(u);
            int pv = find(v);
            if (pu > pv) {
                parent[pv] = pu;
            } else {
                parent[pu] = pv;
            }
        }
    };
    size_t m, n;
    const int direction[4][2] = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
public:
    void solve(vector<vector<char>>& board) {
        if (board.empty()) return;
        m=board.size(), n=board[0].size();
        UF uf(m*n+1);
        int dummy = m*n;
        int i, j, k, x, y;
        for (i=0; i<m; i++) {
            for (j=0; j<n; j++) {
                if (board[i][j] == 'X') continue;
                if (i==0 || i==m-1 || j==0 || j==n-1) {
                    uf.union_(i*n+j, dummy); // 注意别写成`i*m+j`了，可能内存访问越界。
                } else {
                    for (k=0; k<4; k++) {
                        x = i+direction[k][0];
                        y = j+direction[k][1];
                        if (board[x][y] == 'O') {
                            uf.union_(x*n+y, i*n+j);
                        }
                    }   
                }
            }
        }
        for (i=0; i<m; i++) {
            for (j=0; j<n; j++) {
                if (uf.find(i*n+j) != dummy) // 这里严格应该分别find然后比较头目是否相等。不过因为我们限制ID大的做头目，所以这里没有问题。
                    board[i][j] = 'X';
            }
        }
    }
};
```



