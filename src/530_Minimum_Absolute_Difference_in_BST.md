# 530. Minimum Absolute Difference in BST

> Given a binary search tree with non-negative values, find the minimum [absolute difference](https://en.wikipedia.org/wiki/Absolute_difference) between values of any two nodes.
>
> **Example:**
>
> ```
> Input:
> 
>    1
>     \
>      3
>     /
>    2
> 
> Output:
> 1
> 
> Explanation:
> The minimum absolute difference is 1, which is the difference between 2 and 1 (or between 2 and 3).
> ```
>
> **Note:**
>
> - There are at least two nodes in this BST.
> - This question is the same as 783: https://leetcode.com/problems/minimum-distance-between-bst-nodes/

1. Easy。

```cpp
class Solution {
    int minDiff = INT_MAX;
public:
    int getMinimumDifference(TreeNode* root) {
        dfs(root, INT_MAX);
        return minDiff;
    }
    
    int dfs(TreeNode* root, int prev) {
        if (!root) return prev;
        int l = dfs(root->left, prev);
        if (l!=INT_MAX && root->val-l<minDiff)
            minDiff = root->val-l;
        int r = dfs(root->right, root->val);
        return r;
    }
};
```

