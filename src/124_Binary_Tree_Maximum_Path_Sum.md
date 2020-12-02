# 124. Binary Tree Maximum Path Sum

> Given a **non-empty** binary tree, find the maximum path sum.
>
> For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain **at least one node** and does not need to go through the root.
>
> **Example 1:**
>
> ```
> Input: [1,2,3]
> 
>        1
>       / \
>      2   3
> 
> Output: 6
> ```
>
> **Example 2:**
>
> ```
> Input: [-10,9,20,null,null,15,7]
> 
>    -10
>    / \
>   9  20
>     /  \
>    15   7
> 
> Output: 42
> ```

1. Hard。

```cpp
class Solution {
    int max_ = INT_MIN;
public:
    int maxPathSum(TreeNode* root) {
        dfs(root);
        return max_;
    }
    
    int dfs(TreeNode* root) {
        if (!root) return 0;
        // int left = dfs(root->left); // 如果下面的路径和为负，就不包括下面的路径了。
        int left = max(0, dfs(root->left));
        int right = max(0, dfs(root->right));
        max_ = max(max_, left+right+root->val); // 考察经过当前结点的路径是否路径和最大。
        return max(left, right)+root->val; // 返回路径和最大的一个分支组成上面结点的路径。
    }
};
```

