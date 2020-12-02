# 110. Balanced Binary Tree

> Given a binary tree, determine if it is height-balanced.
>
> For this problem, a height-balanced binary tree is defined as:
>
> > a binary tree in which the left and right subtrees of *every* node differ in height by no more than 1.
>
> **Example 1:**
>
> Given the following tree `[3,9,20,null,null,15,7]`:
>
> ```
>     3
>    / \
>   9  20
>     /  \
>    15   7
> ```
>
> Return true.
>
> **Example 2:**
>
> Given the following tree `[1,2,2,3,3,null,null,4,4]`:
>
> ```
>        1
>       / \
>      2   2
>     / \
>    3   3
>   / \
>  4   4
> ```
>
> Return false.

1. Easy。

```cpp
class Solution {
public:
    // 结点的高度就是结点到叶子的边数，结点的深度就是结点到根的边数。
    // 根的高度反而最大。
    // 注意对于每一个结点，都要检查是否平衡，
    // 仅仅检查根是否平衡是不够的，比如[3, 9, 20, 3, null, null, 3]，
    // 仅检查根是平衡的，但实际上其他结点不平衡，故该树不平衡。
    bool isBalanced(TreeNode* root) {
        return height(root)!=-1;
    }
    
    int height(TreeNode* root) {
        if (!root) return 0;
        int lh = height(root->left);
        if (lh == -1) return -1;
        int rh = height(root->right);
        if (rh == -1) return -1;
        if (abs(lh-rh)>1) return -1;
        return max(lh, rh)+1;
    }
};
```

