# 236. Lowest Common Ancestor of a Binary Tree

> Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
>
> According to the [definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor): “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow **a node to be a descendant of itself**).”
>
> Given the following binary tree: root = [3,5,1,6,2,0,8,null,null,7,4]
>
> ![img](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)
>
> **Example 1:**
>
> ```
> Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
> Output: 3
> Explanation: The LCA of nodes 5 and 1 is 3.
> ```
>
> **Example 2:**
>
> ```
> Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
> Output: 5
> Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
> ```
>
> **Note:**
>
> - All of the nodes' values will be unique.
> - p and q are different and both values will exist in the binary tree.

1. Medium。

```cpp
class Solution {
    TreeNode* ans = nullptr;
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        dfs(root, p, q);
        return ans;
    }
    
    bool dfs(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (!root) return false;
        // 使用int直接可以运算，代码更简洁。
        int left = dfs(root->left, p, q);
        int right = dfs(root->right, p, q);
        int mid = root==p || root==q;
        if (left+right+mid >= 2)
            ans = root;
        return mid+left+right>0;
    }
};
```

```cpp
class Solution {
public:
    // 这个递归函数输入一棵树，返回（传递回上层调用/沿路径往上传递回去）：
    // 1. nullptr，表明这棵树中不存在p或q或p和q的lca；
    // 2. p和q的lca（包括p的lca为q和q的lca为p的情况），或者p，或者q。
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        // 这个谓词也处理了p是q的lca和q是p的lca的情况，即p在q的子树中，或q在p的子树中，这两种情况可以直接返回q或p，不必再搜索。
        if (!root || root == p || root == q) return root;
        TreeNode* left = lowestCommonAncestor(root->left, p, q);
        TreeNode* right = lowestCommonAncestor(root->right, p, q);
        // 如果left和right都不为nullptr，即p和q分别在root的两个子树中，那么当前root就是lca，返回root，传递回去。
        return !left ? right : !right ? left : root;
    }
};
```

