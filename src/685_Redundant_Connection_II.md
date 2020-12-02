# 685. Redundant Connection II

> In this problem, a rooted tree is a **directed** graph such that, there is exactly one node (the root) for which all other nodes are descendants of this node, plus every node has exactly one parent, except for the root node which has no parents.
>
> The given input is a directed graph that started as a rooted tree with N nodes (with distinct values 1, 2, ..., N), with one additional directed edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.
>
> The resulting graph is given as a 2D-array of `edges`. Each element of `edges` is a pair `[u, v]` that represents a **directed** edge connecting nodes `u` and `v`, where `u` is a parent of child `v`.
>
> Return an edge that can be removed so that the resulting graph is a rooted tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array.
>
> **Example 1:**
>
> ```
> Input: [[1,2], [1,3], [2,3]]
> Output: [2,3]
> Explanation: The given directed graph will be like this:
>   1
>  / \
> v   v
> 2-->3
> ```
>
> **Example 2:**
>
> ```
> Input: [[1,2], [2,3], [3,4], [4,1], [1,5]]
> Output: [4,1]
> Explanation: The given directed graph will be like this:
> 5 <- 1 -> 2
>      ^    |
>      |    v
>      4 <- 3
> ```
>
> **Note:**
>
> The size of the input 2D-array will be between 3 and 1000.
>
> Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.

1. Hard。

```cpp
// https://leetcode.com/problems/redundant-connection-ii/discuss/278105/topic
class Solution {
    struct UF {
        vector<int> parent;
        UF(size_t n): parent(n+1) {
            for (int i=1; i<=n; i++)
                parent[i] = i;
        }
        
        bool union_(int u, int v) {
            // 这里不能按秩合并，要始终沿一个方向合并。
            int pu = find(u);
            int pv = find(v);
            if (pu == pv) {
                // pu和pv已经直接/间接相连了。
                return false;
            } else {
                parent[v] = pu;
                return true;
            }
        }
        
        // 找到u所在集合中的头目。
        int find(int u) {
            if (parent[u] != u)
                parent[u] = find(parent[u]);
            return parent[u];
        }
    };
public:
    vector<int> findRedundantDirectedConnection(vector<vector<int>>& edges) {
        // 注意，edges中edge并不是按照树从根到叶有一定顺序给出的。
        // 所以不要误以为造成环的最后那一条边也是导致某个结点入度变为2
        // 的那条边。所以不要以为删掉形成环的最后那一条边就顺便把入度为2
        // 的结点的入度变成1了。
        // 
        // 因为是在树上加一条边，所以这个图中一定有环。
        UF uf(2*edges.size()+1); // 最多有这么多个结点。
        vector<int> edge1, edge2, lastEdgeCauseCircle;
        unordered_map<int, int> parent;
        for (auto& edge: edges) {
            if (parent.find(edge[1]) != parent.end()) {
                // edge[1]已经有一个入度了，现在加上当前edge就有两个入度了。
                // 记住使得edge[1]有两个入度的两条边。
                edge1 = {parent[edge[1]], edge[1]};
                edge2 = edge;
                // 这里不把edge2合并到集合中。
                // 如果最后集合中没有环，则edge2就是环中的一条边，
                // 删除edge2即消除了环也消除了入度为2的结点。
                // 如果有环，则edge1就是环中的一条边，这时同理删除edge1即可。
            } else {
                if (!uf.union_(edge[0], edge[1])) {
                    // edge是形成环的最后一条边。
                    lastEdgeCauseCircle = edge;
                }
                parent[edge[1]] = edge[0];
            }
        }
        if (edge1.empty()) {
            // 冗余边指向根，所以所有结点的入度均为1。
            return lastEdgeCauseCircle;
        }
        return lastEdgeCauseCircle.empty()? edge2: edge1;
    }
};
```

