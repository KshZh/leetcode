# 200. Number of Islands

> Given a 2d grid map of `'1'`s (land) and `'0'`s (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
>
> **Example 1:**
>
> ```
> Input:
> 11110
> 11010
> 11000
> 00000
> 
> Output: 1
> ```
>
> **Example 2:**
>
> ```
> Input:
> 11000
> 11000
> 00100
> 00011
> 
> Output: 3
> ```

1. Medium。
2. 求解连通分量的个数，可以考察dfs/bfs次数，也可以用并查集。

```cpp
class Solution {
    vector<int> direction{0, -1, 0, 1, 0};
    size_t m, n;
public:
    int numIslands(vector<vector<char>>& grid) {
        if (grid.empty()) return 0;
        m = grid.size();
        n = grid[0].size();
        int r, c, ans=0;
        for (r=0; r<m; r++) {
            for (c=0; c<n; c++) {
                if (grid[r][c] == '1') {
                    bfs(grid, r, c);
                    ans++;
                }
            }
        }
        return ans;
    }
    
    void dfs(vector<vector<char>>& grid, int r, int c) {
        grid[r][c] = '0';
        int i, j, k;
        for (k=0; k<4; k++) {
            i = r+direction[k];
            j = c+direction[k+1];
            if (i<0 || i>=m || j<0 || j>=n) continue;
            if (grid[i][j] == '1')
                dfs(grid, i, j);
        }
    }
    
    void bfs(vector<vector<char>>& grid, int r, int c) {
        queue<pair<int, int>> q;
        q.push({r, c});
        grid[r][c] = '0'; // 注意要在push时更新，否则可能push同一个元素多次。
        pair<int, int> x;
        int i, j, k;
        while (!q.empty()) {
            x = q.front();
            q.pop();
            for (k=0; k<4; k++) {
                i = x.first+direction[k];
                j = x.second+direction[k+1];
                if (i<0 || i>=m || j<0 || j>=n) continue;
                if (grid[i][j] == '1') {
                    q.push({i, j});
                    grid[i][j] = '0';
                }
            }
        }
    }
};
```

```cpp
class Solution {
    int direction[5] = {0, -1, 0, 1, 0};
    size_t m, n;
    vector<int> parent;
    vector<int> rank;
    
    int find(int u) {
        if (parent[u] != u)
            parent[u] = find(parent[u]);
        return parent[u];
    }
    
    void union_(int u, int v) {
        int pu = find(u);
        int pv = find(v);
        if (pu == pv) return;
        if (rank[pu] > rank[pv]) {
            // 注意别写成`parent[v] = u;`或`parent[v] = pu;`了。
            // 并是两个集合的头目成为上下级的操作。
            parent[pv] = pu;
        } else {
            parent[pu] = pv;
            if (rank[pu] == rank[pv])
                rank[pv]++;
        }
    }
public:
    int numIslands(vector<vector<char>>& grid) {
        if (grid.empty()) return 0;
        m = grid.size();
        n = grid[0].size();
        int i, j, k, x, y;
        parent = vector<int>(m*n, -1);
        rank = vector<int>(m*n);
        for (i=0; i<m; i++) {
            for (j=0; j<n; j++) {
                if (grid[i][j] == '1')
                    parent[i*n+j] = i*n+j; // 初始时，每个元素自成一个帮派。
            }
        }
        for (i=0; i<m; i++) {
            for (j=0; j<n; j++) {
                if (grid[i][j] != '1') continue;
                for (k=0; k<4; k++) {
                    x = i+direction[k];
                    y = j+direction[k+1];
                    if (x<0 || x>=m || y<0 || y>=n) continue;
                    if (grid[x][y] == '1') {
                        union_(i*n+j, x*n+y); // 注意别写成`i*m+j`了。
                    }
                }
            }
        }
        int cnt = 0;
        for (i=0; i<m*n; i++) {
            if (parent[i]!=-1 && parent[i]==i)
                cnt++;
        }
        return cnt;
    }
};
```

