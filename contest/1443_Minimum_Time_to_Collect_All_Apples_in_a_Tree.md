# 1443. Minimum Time to Collect All Apples in a Tree

> Given an undirected tree consisting of `n` vertices numbered from 0 to `n-1`, which has some apples in their vertices. You spend 1 second to walk over one edge of the tree. *Return the minimum time in seconds you have to spend in order to collect all apples in the tree starting at **vertex 0** and coming back to this vertex.*
>
> The edges of the undirected tree are given in the array `edges`, where `edges[i] = [fromi, toi]` means that exists an edge connecting the vertices `fromi` and `toi`. Additionally, there is a boolean array `hasApple`, where `hasApple[i] = true` means that vertex `i` has an apple, otherwise, it does not have any apple.
>
>  
>
> **Example 1:**
>
> **![img](https://assets.leetcode.com/uploads/2020/04/23/min_time_collect_apple_1.png)**
>
> ```
> Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,true,true,false]
> Output: 8 
> Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.  
> ```
>
> **Example 2:**
>
> **![img](https://assets.leetcode.com/uploads/2020/04/23/min_time_collect_apple_2.png)**
>
> ```
> Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,false,true,false]
> Output: 6
> Explanation: The figure above represents the given tree where red vertices have an apple. One optimal path to collect all apples is shown by the green arrows.  
> ```
>
> **Example 3:**
>
> ```
> Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,false,false,false,false,false]
> Output: 0
> ```
>
>  
>
> **Constraints:**
>
> - `1 <= n <= 10^5`
> - `edges.length == n-1`
> - `edges[i].length == 2`
> - `0 <= fromi, toi <= n-1`
> - `fromi < toi`
> - `hasApple.length == n`

```java
class Solution {
    private Map<Integer, List<Integer>> childs = new HashMap<>();
    private List<Boolean> hasApple;
    private Set<Integer> visited = new HashSet<>();
    
    public int minTime(int n, int[][] edges, List<Boolean> hasApple) {
        this.hasApple = hasApple;
        for (int i=0; i<edges.length; i++) {
            // Java的HashMap不像cpp一样不存在自动创建，
            // 所以要我们手动创建。
            // 无向图。（题目对edges的解释有误）
            if (!childs.containsKey(edges[i][0])) {
                childs.put(edges[i][0], new ArrayList<>());
            }
            if (!childs.containsKey(edges[i][1])) {
                childs.put(edges[i][1], new ArrayList<>());
            }
            childs.get(edges[i][0]).add(edges[i][1]);
            childs.get(edges[i][1]).add(edges[i][0]);
        }
        return dfs(0);
    }
    
    private int dfs(int tree) {
        if (visited.contains(tree)) {
            return 0;
        }
        visited.add(tree);
        int res = 0;
        if (childs.containsKey(tree)) {
            // res = dfs(childs.get(tree).get(0))+dfs(childs.get(tree).get(1));
            // 题目没有保证树一定有两棵子树，只是给出的示例都有两棵子树罢了。
            for (int child: childs.get(tree)) {
                res += dfs(child);
            }
        }
        // 注意如果是根，那么不管其子树是否有苹果，或者是根本身是否有苹果，
        // 因为上面都没有树需要往下走到这个根了，所以不花费从上面到这个根往返的时间。
        if (tree!=0 && (res!=0 || hasApple.get(tree))) {
            // 说明该树或其子树存在苹果，那么就上面的树必须走到这颗树了，
            // 需要花费往返两秒。
            res += 2;
        }
        return res;
    }
}
```

