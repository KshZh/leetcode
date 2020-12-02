# 701. Insert into a Binary Search Tree

> Given the root node of a binary search tree (BST) and a value to be inserted into the tree, insert the value into the BST. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.
>
> Note that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.
>
> For example, 
>
> ```
> Given the tree:
>         4
>        / \
>       2   7
>      / \
>     1   3
> And the value to insert: 5
> ```
>
> You can return this binary search tree:
>
> ```
>          4
>        /   \
>       2     7
>      / \   /
>     1   3 5
> ```
>
> This tree is also valid:
>
> ```
>          5
>        /   \
>       2     7
>      / \   
>     1   3
>          \
>           4
> ```

1. Medium。

```cpp
class Solution {
public:
    TreeNode* insertIntoBST(TreeNode* root, int val) {
        if (!root)
            return new TreeNode(val);
        // 注意子树的根可能变化，所以要赋值，让当前根的左指针指向左子树的可能的新根。
        if (val < root->val)
            root->left = insertIntoBST(root->left, val);
        else
            root->right = insertIntoBST(root->right, val);
        return root;
    }
};
```

```java
// 迭代版。
public TreeNode insertIntoBST(TreeNode root, int val) {
    if(root == null) return new TreeNode(val);
    TreeNode cur = root;
    while(true) {
        if(cur.val <= val) {
            if(cur.right != null) cur = cur.right;
            else {
                cur.right = new TreeNode(val);
                break;
            }
        } else {
            if(cur.left != null) cur = cur.left;
            else {
                cur.left = new TreeNode(val);
                break;
            }
        }
    }
    return root;
}
```

