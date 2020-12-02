# 1042. Flower Planting With No Adjacent

> You have `N` gardens, labelled `1` to `N`. In each garden, you want to plant one of 4 types of flowers.
>
> `paths[i] = [x, y]` describes the existence of a bidirectional path from garden `x` to garden `y`.
>
> Also, there is no garden that has more than 3 paths coming into or leaving it.
>
> Your task is to choose a flower type for each garden such that, for any two gardens connected by a path, they have different types of flowers.
>
> Return **any** such a choice as an array `answer`, where `answer[i]` is the type of flower planted in the `(i+1)`-th garden. The flower types are denoted 1, 2, 3, or 4. It is guaranteed an answer exists.
>
> **Example 1:**
>
> ```
> Input: N = 3, paths = [[1,2],[2,3],[3,1]]
> Output: [1,2,3]
> ```
>
> **Example 2:**
>
> ```
> Input: N = 4, paths = [[1,2],[3,4]]
> Output: [1,2,1,2]
> ```
>
> **Example 3:**
>
> ```
> Input: N = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
> Output: [1,2,3,4]
> ```
>
> **Note:**
>
> - `1 <= N <= 10000`
> - `0 <= paths.size <= 20000`
> - No garden has 4 or more paths coming into or leaving it.
> - It is guaranteed an answer exists.

1. Easy，图，用数组检查已被用过的元素。

```cpp
class Solution {
public:
    vector<int> gardenNoAdj(int N, vector<vector<int>>& paths) {
        vector<int> res(N); // 元素初始值都为0。
        vector<vector<int>> G(N);
        // 用邻接表存储图。
        for (const auto& p: paths) {
            G[p[0]-1].push_back(p[1]-1);
            G[p[1]-1].push_back(p[0]-1);
        }
        int i, j;
        // 逐个着色。
        for (i=0; i<N; i++) {
            bool colors[5] = {};
            // 考察该结点邻接的结点用了哪些颜色。
            for (int x: G[i]) {
                colors[res[x]] = true;
            }
            // 取其中没用到的那个颜色作为该结点的颜色。
            for (j=1; j<=4; j++) {
                if (!colors[j]) {
                    res[i] = j;
                    break;
                }
            }
        }
        return res;
    }
};
```

```python
def gardenNoAdj(self, N, paths):
    res = [0] * N
    G = [[] for i in range(N)]
    for x, y in paths:
        G[x - 1].append(y - 1)
        G[y - 1].append(x - 1)
        # {1, 2}是set字面值，[1, 2]是list字面值，set有差集运算。
        for i in range(N):
            res[i] = ({1, 2, 3, 4} - {res[j] for j in G[i]}).pop()
        return res
```

