# 105. Construct Binary Tree from Preorder and Inorder Traversal

> Given preorder and inorder traversal of a tree, construct the binary tree.
>
> **Note:**
> You may assume that duplicates do not exist in the tree.
>
> For example, given
>
> ```
> preorder = [3,9,20,15,7]
> inorder = [9,3,15,20,7]
> ```
>
> Return the following binary tree:
>
> ```
>     3
>    / \
>   9  20
>     /  \
>    15   7
> ```

1. Medium。

```cpp
class Solution {
public:
    TreeNode* buildTree(vector<int>& preorder, vector<int>& inorder) {
        return helper(preorder, inorder, 0, 0, inorder.size());
    }
    
    TreeNode* helper(vector<int>& preorder, vector<int>& inorder, int pb, int ib, int len) {
        if (len <= 0) return nullptr;
        TreeNode* root = new TreeNode(preorder[pb]);
        int i;
        // 对于这一步，可以事先用哈希表记住inorder中元素对应的下标达到O(1)查找，但只限于inorder数组中没有重复元素。
        for (i=ib; i<ib+len && inorder[i]!=preorder[pb]; i++)
            ;
        int leftSubLen=i-ib, rightSubLen=len-1-leftSubLen; // 注意减一减掉根。
        root->left = helper(preorder, inorder, pb+1, ib, leftSubLen);
        root->right = helper(preorder, inorder, pb+1+leftSubLen, i+1, rightSubLen);
        return root;
    }
};
```

