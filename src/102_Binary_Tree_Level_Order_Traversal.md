# 102. Binary Tree Level Order Traversal

> Given a binary tree, return the *level order* traversal of its nodes' values. (ie, from left to right, level by level).
>
> For example:
> Given binary tree `[3,9,20,null,null,15,7]`,
>
> ```
>     3
>    / \
>   9  20
>     /  \
>    15   7
> ```
>
> 
>
> return its level order traversal as:
>
> ```
> [
>   [3],
>   [9,20],
>   [15,7]
> ]
> ```

1. Medium。

```cpp
// 记住层次的bfs。
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        if (!root) return {};
        queue<TreeNode*> q;
        q.push(root);
        TreeNode* last = root;
        TreeNode* p;
        vector<int> level;
        vector<vector<int>> levels;
        while (!q.empty()) {
            p = q.front();
            q.pop();
            level.push_back(p->val);
            if (p->left)
                q.push(p->left);
            if (p->right)
                q.push(p->right);
            if (p == last) {
                last = q.back();
                levels.push_back(level);
                level.clear();
            }
        }
        return levels;
    }
};
```

```cpp
// 记住层次的dfs。
class Solution {
public:
    vector<vector<int>> levelOrder(TreeNode* root) {
        vector<vector<int>> levels;
        dfs(root, 0, levels);
        return levels;
    }
    
    void dfs(TreeNode* root, int height, vector<vector<int>>& levels) {
        if (!root) return;
        if (levels.size() <= height)
            levels.emplace_back();
        levels[height].push_back(root->val);
        dfs(root->left, height+1, levels);
        dfs(root->right, height+1, levels);
    }
};
```

