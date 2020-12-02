# 111. Minimum Depth of Binary Tree

> Given a binary tree, find its minimum depth.
>
> The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
>
> **Note:** A leaf is a node with no children.
>
> **Example:**
>
> Given binary tree `[3,9,20,null,null,15,7]`,
>
> ```
>     3
>    / \
>   9  20
>     /  \
>    15   7
> ```
>
> return its minimum depth = 2.

1. Easy。

```cpp
// bfs.
class Solution {
public:
    int minDepth(TreeNode* root) {
        if (!root) return 0;
        queue<TreeNode*> q;
        q.push(root);
        TreeNode* last = root;
        TreeNode* x;
        int level = 1;
        while (!q.empty()) {
            x = q.front();
            q.pop();
            if (!x->left && !x->right) {
                return level;
            }
            if (x->left) q.push(x->left);
            if (x->right) q.push(x->right);
            if (x == last) {
                level++;
                if (!q.empty()) last=q.back(); // 这里记得判断队列非空，不然会内存访问异常。
            }
        }
        return -1; // unreachable.
    }
};
```

```cpp
// dfs.
class Solution {
public:
    int minDepth(TreeNode* root) {
        if (!root) return 0;
        int l=minDepth(root->left), r=minDepth(root->right);
        return 1+(min(l, r)? min(l, r): max(l, r)); // 如果其中一个或两个为0，那么返回当前结点另一个分支的深度。
    }
};
```

