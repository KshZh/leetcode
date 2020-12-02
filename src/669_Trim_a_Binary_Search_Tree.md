# 669. Trim a Binary Search Tree

> Given a binary search tree and the lowest and highest boundaries as `L` and `R`, trim the tree so that all its elements lies in `[L, R]` (R >= L). You might need to change the root of the tree, so the result should return the new root of the trimmed binary search tree.
>
> **Example 1:**
>
> ```
> Input: 
>     1
>    / \
>   0   2
> 
>   L = 1
>   R = 2
> 
> Output: 
>     1
>       \
>        2
> ```
>
> **Example 2:**
>
> ```
> Input: 
>     3
>    / \
>   0   4
>    \
>     2
>    /
>   1
> 
>   L = 1
>   R = 3
> 
> Output: 
>       3
>      / 
>    2   
>   /
>  1
> ```

1. Easy。

```cpp
class Solution {
public:
    TreeNode* trimBST(TreeNode* root, int L, int R) {
        if (!root) return root;
        if (root->val < L) return trimBST(root->right, L, R); // 当前根小于L，按照BST的定义，其左子树都小于L，所以直接去掉。
        if (root->val > R) return trimBST(root->left, L, R);
        root->left = trimBST(root->left, L, R);
        root->right = trimBST(root->right, L, R);
        return root;
    }
};
```

```java
class Solution {
    public TreeNode trimBST(TreeNode root, int L, int R) {
        if (root == null) {
            return root;
        }
        //Find a valid root which is used to return.
        while (root!=null && root.val < L || root.val > R) {
            if (root.val < L) {
                root = root.right;
            }
            if (root.val > R) {
                root = root.left;
            }
        }
        TreeNode dummy = root;
        // Remove the invalid nodes from left subtree.
        // 如果root不为null，那么root->val就在区间[L, R]中，根据BST的定义，其左子树都小于root->val，所以其左子树不可能大于R，只需检查其左子树是否有小于L的子树，然后丢弃即可。
        while (dummy != null) {
            // 沿左下一直走，即一直检查最小的子树，如果最小的子树都不小于L，就不需要做什么，
            // 如果有子树小于L，那就要丢弃，然后连上其右子树（因为右子树可能在左子树到L之间，所以需要继续检查其右子树）
            while (dummy.left != null && dummy.left.val < L) {
                dummy.left = dummy.left.right; 
                // If the left child is smaller than L, then we just keep the right subtree of it. 
            }
            dummy = dummy.left;
        }
        dummy = root;
        // Remove the invalid nodes from right subtree
        // 同上。
        while (dummy != null) {
            while (dummy.right != null && dummy.right.val > R) {
                dummy.right = dummy.right.left;
                // If the right child is biggrt than R, then we just keep the left subtree of it. 
            }
            dummy = dummy.right;
        }
        return root;
    }
}
```

