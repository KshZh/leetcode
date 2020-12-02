# 1302. Deepest Leaves Sum

> Given a binary tree, return the sum of values of its deepest leaves.
>
> **Example 1:**
>
> **![img](https://assets.leetcode.com/uploads/2019/07/31/1483_ex1.png)**
>
> ```
> Input: root = [1,2,3,4,5,null,6,7,null,null,null,null,8]
> Output: 15
> ```
>
> **Constraints:**
>
> - The number of nodes in the tree is between `1` and `10^4`.
> - The value of nodes is between `1` and `100`.

1. Medium。

```cpp
// bfs.
class Solution {
public:
    int deepestLeavesSum(TreeNode* root) {
        int res = 0, i;
        queue<TreeNode*> q;
        q.push(root);
        while (q.size()) {
            for (i = q.size() - 1, res = 0; i >= 0; --i) {
                TreeNode* node = q.front(); q.pop();
                res += node->val;
                if (node->right) q.push(node->right);
                if (node->left)  q.push(node->left);
            }
        }
        return res;
    }
};
```

```cpp
// dfs，先计算树的深度。
class Solution {
public:
    int deepestLeavesSum(TreeNode* root) {
        int d = depth(root);
        return dfs(root, d);
    }
    
    int depth(TreeNode* root) {
        if (!root) return 0;
        return 1+max(depth(root->left), depth(root->right));
    }
    
    int dfs(TreeNode* root, int depth) {
        if (!root) return 0;
        if (root && depth == 1)
            return root->val;
        return dfs(root->left, depth-1)+dfs(root->right, depth-1);
    }
};
```

