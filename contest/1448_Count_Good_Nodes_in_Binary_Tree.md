# 1448. Count Good Nodes in Binary Tree

> Given a binary tree `root`, a node *X* in the tree is named **good** if in the path from root to *X* there are no nodes with a value *greater than* X.
>
> Return the number of **good** nodes in the binary tree.
>
> 
>
> **Example 1:**
>
> **![img](https://assets.leetcode.com/uploads/2020/04/02/test_sample_1.png)**
>
> ```
> Input: root = [3,1,4,3,null,1,5]
> Output: 4
> Explanation: Nodes in blue are good.
> Root Node (3) is always a good node.
> Node 4 -> (3,4) is the maximum value in the path starting from the root.
> Node 5 -> (3,4,5) is the maximum value in the path
> Node 3 -> (3,1,3) is the maximum value in the path.
> ```
>
> **Example 2:**
>
> **![img](https://assets.leetcode.com/uploads/2020/04/02/test_sample_2.png)**
>
> ```
> Input: root = [3,3,null,4,2]
> Output: 3
> Explanation: Node 2 -> (3, 3, 2) is not good, because "3" is higher than it.
> ```
>
> **Example 3:**
>
> ```
> Input: root = [1]
> Output: 1
> Explanation: Root is considered as good.
> ```
>
> 
>
> **Constraints:**
>
> - The number of nodes in the binary tree is in the range `[1, 10^5]`.
> - Each node's value is between `[-10^4, 10^4]`.

```java
class Solution {
    public int goodNodes(TreeNode root) {
        return dfs(root, Integer.MIN_VALUE);
    }
    
    // 题意就是考察从根开始的路径，看当前结点的值是否大于等于路径上最大的结点值，是的话该结点就是good node。
    // 所以没什么好说的，就是深度有限搜索，然后在往下搜索时，维护一个路径上的最大结点值。
    // 输入：一棵二叉树。
    // 输出：该树中good node的个数。
    private int dfs(TreeNode root, int max) {
        if (root==null) {
            return 0;
        }
        int x = 0;
        if (root.val >= max) {
            x = 1;
            max = root.val;
        }
        return x+dfs(root.left, max)+dfs(root.right, max);
    }
}
```

