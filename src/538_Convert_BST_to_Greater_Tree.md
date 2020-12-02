# 538. Convert BST to Greater Tree

> Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus sum of all keys greater than the original key in BST.
>
> **Example:**
>
> ```
> Input: The root of a Binary Search Tree like this:
>               5
>             /   \
>            2     13
> 
> Output: The root of a Greater Tree like this:
>              18
>             /   \
>           20     13
> ```
>
> **Note:** This question is the same as 1038: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

1. Easy。

```cpp
class Solution {
    int sum = 0;
public:
    TreeNode* convertBST(TreeNode* root) {
        if (!root) return nullptr;
        convertBST(root->right);
        sum += root->val;
        root->val = sum;
        convertBST(root->left);
        return root;
    }
};
```

```cpp
// Morris算法。
class Solution {
public:
    TreeNode* convertBST(TreeNode* root) {
        int sum = 0;
        TreeNode* p = root;
        TreeNode* prev;
        // 右中左。
        while (root) {
            if (!root->right) { // 没有右子树，那就轮到访问当前结点了。
                sum += root->val;
                root->val = sum;
                root = root->left;
                continue;
            }
            // 找到当前结点在中序遍历中的前驱结点。
            prev = root->right;
            while (prev->left && prev->left!=root)
                prev = prev->left;
            if (prev->left == nullptr) {
                // 前驱结点还没访问过，那就先访问这些前驱结点。
                prev->left = root;
                root = root->right;
            } else {
                // 前驱结点访问过了，那就轮到访问当前结点了。
                prev->left = nullptr; // 恢复树的形状。
                sum += root->val;
                root->val = sum;
                root = root->left;
            }
        }
        return p;
    }
};
```

