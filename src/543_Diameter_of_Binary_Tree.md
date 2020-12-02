# 543. Diameter of Binary Tree

> Given a binary tree, you need to compute the length of the diameter of the tree. The diameter of a binary tree is the length of the **longest** path between any two nodes in a tree. This path may or may not pass through the root.
>
> **Example:**
> Given a binary tree
>
> ```
>           1
>          / \
>         2   3
>        / \     
>       4   5    
> ```
>
> Return **3**, which is the length of the path [4,2,1,3] or [5,2,1,3].
>
> **Note:** The length of path between two nodes is represented by the number of edges between them.

1. Easy。

```java
// 注意，一棵树的diameter不一定经过根，一开始可能会下意识觉得diameter必经过根，但考虑根的左子树高度为8，右子数高度为1，左子树的左右子树高度为7，如此，该树的diameter就不经过根。
class Solution {
    private int maxDiameter = 0;
    
    public int diameterOfBinaryTree(TreeNode root) {
        dfs(root);
        return maxDiameter;
    }
    
    // 输入一棵树，输出：
    // 1. 从树的根到叶的多条路径中的最长长度；
    // 2. 该树的diameter。
    private int dfs(TreeNode root) {
        if (root == null) return 0;
        int l = dfs(root.left);
        int r = dfs(root.right);
        if (l+r > maxDiameter) maxDiameter = l+r;
        return 1+Math.max(l, r);
    }
}
```

```cpp
// 后序遍历（右左中），用一个哈希表记住一棵树的深度，顺便也标记该树是否被访问过。
// 对于只是用栈的后序遍历，可见[145. Binary Tree Postorder Traversal](./145_Binary_Tree_Postorder_Traversal.md)
int diameterOfBinaryTree(TreeNode* root) {
    if (!root) {
        return 0;
    }
    int diameter = 0;
    unordered_map<TreeNode*, int> depths;
    stack<TreeNode*> todo;
    todo.push(root);
    while (!todo.empty()) {
        TreeNode* node = todo.top();
        if (node -> left && depths.find(node -> left) == depths.end()) {
            todo.push(node -> left);
        } else if (node -> right && depths.find(node -> right) == depths.end()) {
            todo.push(node -> right);
        } else {
            // 该结点的左右子树都被访问过了，那就轮到访问该结点了。
            todo.pop();
            int l = depths[node -> left], r = depths[node -> right];
            depths[node] = max(l, r) + 1;
            diameter = max(diameter, l + r);
        }
    }
    return diameter;
}
```

