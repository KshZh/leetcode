# 684. Redundant Connection

> In this problem, a tree is an **undirected** graph that is connected and has no cycles.
>
> The given input is a graph that started as a tree with N nodes (with distinct values 1, 2, ..., N), with one additional edge added. The added edge has two different vertices chosen from 1 to N, and was not an edge that already existed.
>
> The resulting graph is given as a 2D-array of `edges`. Each element of `edges` is a pair `[u, v]` with `u < v`, that represents an **undirected** edge connecting nodes `u` and `v`.
>
> Return an edge that can be removed so that the resulting graph is a tree of N nodes. If there are multiple answers, return the answer that occurs last in the given 2D-array. The answer edge `[u, v]` should be in the same format, with `u < v`.
>
> **Example 1:**
>
> ```
> Input: [[1,2], [1,3], [2,3]]
> Output: [2,3]
> Explanation: The given undirected graph will be like this:
>   1
>  / \
> 2 - 3
> ```
>
> **Example 2:**
>
> ```
> Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
> Output: [1,4]
> Explanation: The given undirected graph will be like this:
> 5 - 1 - 2
>     |   |
>     4 - 3
> ```
>
> **Note:**
>
> The size of the input 2D-array will be between 3 and 1000.
>
> Every integer represented in the 2D-array will be between 1 and N, where N is the size of the input array.

1. Medium。

```java
// Time Complexity: O(N^2) where N is the number of vertices (and also the number of edges) in the graph. In the worst case, for every edge we include, we have to search every previously-occurring edge of the graph.
// Space Complexity: O(N). The current construction of the graph has at most N nodes.
class Solution {
    Set<Integer> seen = new HashSet();
    int MAX_EDGE_VAL = 1000;

    public int[] findRedundantConnection(int[][] edges) {
        ArrayList<Integer>[] graph = new ArrayList[MAX_EDGE_VAL + 1];
        for (int i = 0; i <= MAX_EDGE_VAL; i++) {
            graph[i] = new ArrayList();
        }

        for (int[] edge: edges) {
            // 哈希表seen记住遍历过的结点，避免走回头路和绕圈。
            seen.clear();
            // 如果edge的两个结点已经在图中，且图中存在另一条路径，
            // 从edge[0]到edge[1]，那么edge这条边就是冗余的，可以删去。
            if (!graph[edge[0]].isEmpty() && !graph[edge[1]].isEmpty() &&
                    dfs(graph, edge[0], edge[1])) {
                return edge;
            }
            // 注意这个邻接表是增量地构建出来的，
            graph[edge[0]].add(edge[1]);
            graph[edge[1]].add(edge[0]);
        }
        throw new AssertionError();
    }
    public boolean dfs(ArrayList<Integer>[] graph, int source, int target) {
        if (!seen.contains(source)) {
            seen.add(source);
            if (source == target) return true;
            // 对当前结点邻接的每个结点，
            // 先选一个结点深入，如果搜索失败，
            // 则回到这里选另一个结点继续深入搜索。
            for (int nei: graph[source]) {
                if (dfs(graph, nei, target)) return true;
            }
        }
        return false;
    }
}
```

```java
// Time Complexity: O(Nα(N))≈O(N), where N is the number of vertices (and also the number of edges) in the graph, and α is the Inverse-Ackermann function. We make up to N queries of dsu.union, which takes (amortized) O(α(N)) time. Outside the scope of this article, it can be shown why dsu.union has O(α(N)) complexity, what the Inverse-Ackermann function is, and why O(α(N)) is approximately O(1).
// Space Complexity: O(N). The current construction of the graph (embedded in our dsu structure) has at most N nodes.
class Solution {
    int MAX_EDGE_VAL = 1000;

    public int[] findRedundantConnection(int[][] edges) {
        DSU dsu = new DSU(MAX_EDGE_VAL + 1);
        for (int[] edge: edges) {
            // 如果一条边的两个结点已经在这个连通集合中，
            // 那么edge就是冗余的。
            if (!dsu.union(edge[0], edge[1])) return edge;
        }
        throw new AssertionError();
    }
}

class DSU {
    int[] parent;
    int[] rank;

    public DSU(int size) {
        parent = new int[size];
        for (int i = 0; i < size; i++) parent[i] = i;
        rank = new int[size];
    }

    public int find(int x) {
        if (parent[x] != x) parent[x] = find(parent[x]);
        return parent[x];
    }

    public boolean union(int x, int y) {
        int xr = find(x), yr = find(y);
        if (xr == yr) {
            return false;
        } else if (rank[xr] < rank[yr]) {
            parent[xr] = yr;
        } else if (rank[xr] > rank[yr]) {
            parent[yr] = xr;
        } else {
            parent[yr] = xr;
            rank[xr]++;
        }
        return true;
    }
}
```

