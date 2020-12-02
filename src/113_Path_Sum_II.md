# 113. Path Sum II

> Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
>
> **Note:** A leaf is a node with no children.
>
> **Example:**
>
> Given the below binary tree and `sum = 22`,
>
> ```
>       5
>      / \
>     4   8
>    /   / \
>   11  13  4
>  /  \    / \
> 7    2  5   1
> ```
>
> Return:
>
> ```
> [
>    [5,4,11,2],
>    [5,8,4,5]
> ]
> ```

1. Medium。

```cpp
class Solution {
public:
    vector<vector<int>> pathSum(TreeNode* root, int sum) {
        vector<vector<int>> res;
        vector<int> path;
        dfs(root, sum, path, res);
        return res;
    }
    
    void dfs(TreeNode* root, int sum, vector<int>& path, vector<vector<int>>& res) {
        if (!root) return;
        // 条件别写少了，sum为0且结点为叶结点才行。
        // 注意叶结点才是终止条件，要写在外面。
        // if (!root->left && !root->right && sum==root->val)
        if (!root->left && !root->right) {
            if (sum == root->val) {
                path.push_back(root->val);
                res.push_back(path);
                path.pop_back();
            }
            return;
        }
        path.push_back(root->val);
        dfs(root->left, sum-root->val, path, res);
        dfs(root->right, sum-root->val, path, res);
        path.pop_back();
    }
};
```

