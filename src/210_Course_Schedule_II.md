# 210. Course Schedule II

> There are a total of *n* courses you have to take, labeled from `0` to `n-1`.
>
> Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: `[0,1]`
>
> Given the total number of courses and a list of prerequisite **pairs**, return the ordering of courses you should take to finish all courses.
>
> There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

1. Medium。

```cpp
class Solution {
public:
    vector<int> findOrder(int n, vector<vector<int>>& pre) {
        vector<vector<int>> adj(n, vector<int>());
        vector<int> indegree(n, 0);
        vector<int> res;
        for (const auto& p: pre) {
            adj[p[1]].push_back(p[0]);
            indegree[p[0]]++;
        }
        queue<int> q;
        for (int i = 0; i < n; i++)
            if (indegree[i] == 0) q.push(i);
        while (!q.empty()) {
            int curr = q.front(); q.pop(); n--;
            res.push_back(curr);
            for (int next: adj[curr])
                if (--indegree[next] == 0) q.push(next);
        }
        if (n == 0)
            return res;
        return vector<int>();
    }
};
```



