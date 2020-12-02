# 1203. Sort Items by Groups Respecting Dependencies

> There are `n` items each belonging to zero or one of `m` groups where `group[i]` is the group that the `i`-th item belongs to and it's equal to `-1` if the `i`-th item belongs to no group. The items and the groups are zero indexed. A group can have no item belonging to it.
>
> Return a sorted list of the items such that:
>
> - The items that belong to the same group are next to each other in the sorted list.
> - There are some relations between these items where `beforeItems[i]` is a list containing all the items that should come before the `i`-th item in the sorted array (to the left of the `i`-th item).
>
> Return any solution if there is more than one solution and return an **empty list** if there is no solution.
>
> **Example 1:**
>
> **![img](https://assets.leetcode.com/uploads/2019/09/11/1359_ex1.png)**
>
> ```
> Input: n = 8, m = 2, group = [-1,-1,1,0,0,1,0,-1], beforeItems = [[],[6],[5],[6],[3,6],[],[],[]]
> Output: [6,3,4,1,5,2,0,7]
> ```

1. Hard。
2. 双层拓扑排序。注意一个图可以有多个连通分量，那么一个DAG当然也可以有多个连通分量。
3. DAG+结点先后顺序 =》 拓扑排序。

```cpp
struct DAG {
    unordered_map<int, vector<int>> adj;
    unordered_map<int, int> indegree;
    
    DAG(int n) {
        for (int i=0; i<n; i++) {
            adj[i] = vector<int>(); // 必须要先在容器中创建好相应的元素，否则如果只是等addArc()来创建的话，若有一个DAG中有多个连通分量，且有某个连通分量只有一个结点，那么这个结点就不会被包含到容器中，那么在拓扑排序时就会漏掉。
            indegree[i] = 0;
        }
    }
    
    DAG(const vector<int>& nodes) {
        for (int x: nodes) {
            adj[x] = vector<int>();
            indegree[x] = 0;
        }
    }
    
    void addArc(int from, int to) {
        adj[from].push_back(to);
        indegree[to]++;
    }
    
    vector<int> topSort() {
        vector<int> res;
        queue<int> q;
        int x;
        for (const auto& p: indegree) {
            if (p.second == 0)
                q.push(p.first);
        }
        while (!q.empty()) {
            x = q.front();
            q.pop();
            res.push_back(x);
            for (int v: adj[x]) {
                if (--indegree[v] == 0)
                    q.push(v);
            }
        }
        return res;
    }
};

class Solution {
public:
    vector<int> sortItems(int n, int m, vector<int>& group, vector<vector<int>>& beforeItems) {
        // 双层拓扑排序，先对组间DAG进行拓扑排序，再对组内DAG进行拓扑排序。
        
        // 先将不属于任何组的结点规划为自己构成一个组。
        vector<vector<int>> groups(m);
        for (int i=0; i<n; i++) {
            if (group[i] == -1) {
                group[i] = groups.size();
                groups.push_back(vector<int>(1, i));
            } else {
                groups[group[i]].push_back(i);
            }
        }
        m = groups.size();
        
        DAG interGroupDAG(m); // m个组，则该DAG有m个结点。
        vector<DAG> innerDAGs; // m个组，则有m个组内DAG。
        for (int i=0; i<m; i++) {
            innerDAGs.emplace_back(groups[i]);
        }
        for (int i=0; i<n; i++) {
            for (int x: beforeItems[i]) {
                if (group[x] == group[i]) { // 组内加弧。
                    innerDAGs[group[i]].addArc(x, i);
                } else { // 组间加弧。
                    interGroupDAG.addArc(group[x], group[i]);
                }
            }
        }
        vector<int> res;
        auto seq(interGroupDAG.topSort());
        if (seq.size() != m) return {};
        for (int groupNo: seq) {
            auto temp(innerDAGs[groupNo].topSort()); // 移动构造，所以可以每次循环都定义一次temp。开销不大。
            if (temp.size() != groups[groupNo].size()) return {};
            for (int x: temp)
                res.push_back(x);
        }
        return res;
    }
};
```

