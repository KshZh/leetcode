# 235. Lowest Common Ancestor of a Binary Search Tree

> Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
>
> According to the [definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor): “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow **a node to be a descendant of itself**).”
>
> Given binary search tree: root = [6,2,8,0,4,7,9,null,null,3,5]
>
> ![img](https://assets.leetcode.com/uploads/2018/12/14/binarysearchtree_improved.png)
>
> **Example 1:**
>
> ```
> Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
> Output: 6
> Explanation: The LCA of nodes 2 and 8 is 6.
> ```
>
> **Example 2:**
>
> ```
> Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
> Output: 2
> Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
> ```
>
> **Note:**
>
> - All of the nodes' values will be unique.
> - p and q are different and both values will exist in the BST.

1. Medium。
2. **根据bst的性质，我们很容易判断一个结点是在其左子树，还是在其右子树中，所以可以直接往其中一个子树搜索，而不必两个子树都搜**。

```cpp
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (root->val>p->val && root->val>q->val)
            return lowestCommonAncestor(root->left, p, q);
        if (root->val<p->val && root->val<q->val)
            return lowestCommonAncestor(root->right, p, q);
        return root; // 如果p、q分别在root的两个子树中，或者root为p，或者root为q，那么root就是p和q的lca。
    }
};
```

```cpp
// 迭代版。递归版只是尾递归，所以很容易写出迭代版。
class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        while (root) {
            if (root->val>p->val && root->val>q->val)
                root = root->left;
            else if (root->val<p->val && root->val<q->val)
                root = root->right;
            else
                return root;
        }
        return nullptr;
    }
};
```

