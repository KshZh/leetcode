# 783. Minimum Distance Between BST Nodes

> Given a Binary Search Tree (BST) with the root node `root`, return the minimum difference between the values of any two different nodes in the tree.
>
> **Example :**
>
> ```
> Input: root = [4,2,6,1,3,null,null]
> Output: 1
> Explanation:
> Note that root is a TreeNode object, not an array.
> 
> The given tree [4,2,6,1,3,null,null] is represented by the following diagram:
> 
>           4
>         /   \
>       2      6
>      / \    
>     1   3  
> 
> while the minimum difference in this tree is 1, it occurs between node 1 and node 2, also between node 3 and node 2.
> ```
>
> **Note:**
>
> 1. The size of the BST will be between 2 and `100`.
> 2. The BST is always valid, each node's value is an integer, and each node's value is different.
> 3. This question is the same as 530: https://leetcode.com/problems/minimum-absolute-difference-in-bst/

1. Easy。

```cpp
class Solution {
    int minDiff = INT_MAX;
public:
    int minDiffInBST(TreeNode* root) {
        // 要找到最小的差值，则两个数要“紧凑”。
        // bst的中序序列是有序的，所以进行中序遍历即可。
        dfs(root, INT_MAX);
        return minDiff;
    }
    
    // 输入一个（子）树和该树在中序遍历中的前驱结点，
    // 返回中序遍历该子树的最后一个结点。
    int dfs(TreeNode* root, int prev) {
        // if (!root) return INT_MAX;
        if (!root) return prev; // 注意要返回prev，而不是INT_MAX。因为这是一棵空树，空树的中序序列为空，所以遍历的最后一个结点还是prev。
        int l = dfs(root->left, prev);
        if (l!=INT_MAX && root->val-l<minDiff)
            minDiff = root->val-l;
        int r = dfs(root->right, root->val);
        // return root->val;
        // 若没有右子树，当前根就是该子树的中序序列中的最后一个结点。
        // return r==INT_MAX? root->val: r;
        return r;
    }
};
```

