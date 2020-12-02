# 207. Course Schedule

> There are a total of *n* courses you have to take, labeled from `0` to `n-1`.
>
> Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: `[0,1]`
>
> Given the total number of courses and a list of prerequisite **pairs**, is it possible for you to finish all courses?

1. Medium。

```cpp
class Solution {
    unordered_map<int, int> indegree;
    unordered_map<int, vector<int>> graph; // key是课程编号，value是该课程出边指向的结点。
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        if (numCourses <= 1 || prerequisites.empty()) return true;
        for (const auto& p: prerequisites) {
            indegree[p[1]]++;
            graph[p[0]].push_back(p[1]);
        }
        return bfs(numCourses);
    }
    
    bool bfs(int numCourses) {
        queue<int> q;
        int x;
        for (int i=0; i<numCourses; i++) {
            if (indegree[i] == 0) // 入度为0，入队。
                q.push(i);
        }
        while (!q.empty()) {
            x = q.front(); // 每次删掉入度为0的结点及其出边。
            q.pop();
            // n++;
            numCourses--;
            for (auto& v: graph[x]) {
                indegree[v]--;
                if (indegree[v] == 0)
                    q.push(v);
            }
        }
        // return n == numCourses;
        return numCourses == 0;
    }
};
```

```cpp
// 因为课程编号固定从0到N-1，所以可以直接用数组而不是哈希表，以空间换时间，获得更好的空间局部性，减少cache miss。
class Solution {
public:
    bool canFinish(int n, vector<vector<int>>& pre) {
        vector<vector<int>> adj(n, vector<int>());
        vector<int> degree(n, 0);
        for (auto &p: pre) {
            adj[p[0]].push_back(p[1]);
            degree[p[1]]++;
        }
        queue<int> q;
        for (int i = 0; i < n; i++)
            if (degree[i] == 0) q.push(i);
        while (!q.empty()) {
            int curr = q.front(); q.pop(); n--;
            for (int next: adj[curr])
                if (--degree[next] == 0) q.push(next);
        }
        return n == 0;
    }
};
```

```cpp
class Solution {
    vector<int> res;
    vector<vector<int>> adj;
    vector<int> indegree;
public:
    vector<int> findOrder(int n, vector<vector<int>>& pre) {
        adj = vector<vector<int>>(n, vector<int>());
        indegree = vector<int>(n, 0);
        for (const auto& p: pre) {
            adj[p[1]].push_back(p[0]);
            indegree[p[0]]++;
        }
        for (int i=0; i<n; i++) {
            if (indegree[i] == 0) {
                indegree[i]--; // 防止对同一个入度为0的结点多次调用dfs。
                dfs(i);
            }
        }
        if (res.size() == n)
            return res;
        return vector<int>();
    }
    
    void dfs(int x) {
        res.push_back(x);
        for (int v: adj[x]) {
            if (--indegree[v] == 0) {
                indegree[v]--;
                dfs(v);
            }
        }
    }
};
```

