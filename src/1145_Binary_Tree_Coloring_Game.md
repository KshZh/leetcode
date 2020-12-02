# 1145_Binary_Tree_Coloring_Game

> Two players play a turn based game on a binary tree. We are given the `root` of this binary tree, and the number of nodes `n` in the tree. `n` is odd, and each node has a distinct value from `1` to `n`.
>
> Initially, the first player names a value `x` with `1 <= x <= n`, and the second player names a value `y` with `1 <= y <= n` and `y != x`. The first player colors the node with value `x` red, and the second player colors the node with value `y` blue.
>
> Then, the players take turns starting with the first player. In each turn, that player chooses a node of their color (red if player 1, blue if player 2) and colors an **uncolored** neighbor of the chosen node (either the left child, right child, or parent of the chosen node.)
>
> If (and only if) a player cannot choose such a node in this way, they must pass their turn. If both players pass their turn, the game ends, and the winner is the player that colored more nodes.
>
> You are the second player. If it is possible to choose such a `y` to ensure you win the game, return `true`. If it is not possible, return `false`.
>
> **Example 1:**
>
> ![img](https://assets.leetcode.com/uploads/2019/08/01/1480-binary-tree-coloring-game.png)
>
> ```
> Input: root = [1,2,3,4,5,6,7,8,9,10,11], n = 11, x = 3
> Output: true
> Explanation: The second player can choose the node with value 2.
> ```
>
> **Constraints:**
>
> - `root` is the root of a binary tree with `n` nodes and distinct node values from `1` to `n`.
> - `n` is odd.
> - `1 <= x <= n <= 100`

1. Medium。

```java
// The best move y must be immediately adjacent to x, since it locks out that subtree.
class Solution {
    private int left, right, val;
    public boolean btreeGameWinningMove(TreeNode root, int n, int x) {
        val = x;
        count(root);
        // 选择x相邻的三个子树中结点最多的那个子树，如果所选的那个子树结点数大于一半，则y就能赢。
        return Math.max(Math.max(left, right), n-left-right-1) > n/2;
    }
    
    // 输入一棵树root，返回该树的结点数。
    private int count(TreeNode root) {
        if (root == null) return 0;
        int l=count(root.left), r=count(root.right);
        if (root.val == val) {
            left = l;
            right = r;
        }
        return l+r+1;
    }
}
```

