# 106. Construct Binary Tree from Inorder and Postorder Traversal

> Given inorder and postorder traversal of a tree, construct the binary tree.
>
> **Note:**
> You may assume that duplicates do not exist in the tree.
>
> For example, given
>
> ```
> inorder = [9,3,15,20,7]
> postorder = [9,15,7,20,3]
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
    TreeNode* buildTree(vector<int>& inorder, vector<int>& postorder) {
        return helper(postorder, inorder, postorder.size()-1, 0, postorder.size());
    }
    
    TreeNode* helper(vector<int>& postorder, vector<int>& inorder, int pb, int ib, int len) {
        if (len <= 0) return nullptr;
        TreeNode* root = new TreeNode(postorder[pb]);
        int i;
        // 对于这一步，可以事先用哈希表记住inorder中元素对应的下标达到O(1)查找，但只限于inorder数组中没有重复元素。
        for (i=ib; i<ib+len && inorder[i]!=postorder[pb]; i++)
            ;
        int leftSubLen=i-ib, rightSubLen=len-1-leftSubLen; // 注意减一减掉根。
        root->left = helper(postorder, inorder, pb-rightSubLen-1, ib, leftSubLen);
        root->right = helper(postorder, inorder, pb-1, i+1, rightSubLen);
        return root;
    }
};
```

