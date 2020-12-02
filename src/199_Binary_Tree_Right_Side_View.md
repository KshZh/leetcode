# 199. Binary Tree Right Side View

> Given a binary tree, imagine yourself standing on the *right* side of it, return the values of the nodes you can see ordered from top to bottom.
>
> **Example:**
>
> ```
> Input: [1,2,3,null,5,null,4]
> Output: [1, 3, 4]
> Explanation:
> 
>    1            <---
>  /   \
> 2     3         <---
>  \     \
>   5     4       <---
> ```

1. Medium。

![](https://leetcode.com/problems/binary-tree-right-side-view/Figures/199/199_depth_first.png)

```cpp
// bfs.
class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        if (!root) return {};
        queue<TreeNode*> q;
        vector<int> v;
        q.push(root);
        TreeNode *last=root, *p;
        while (!q.empty()) {
            p = q.front();
            q.pop();
            if (p->left) q.push(p->left);
            if (p->right) q.push(p->right);
            if (p == last) {
                v.push_back(p->val);
                if (!q.empty()) last=q.back();
            }
        }
        return v;
    }
};
```

```cpp
// dfs.
class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> v;
        dfs(root, v, 0);
        return v;
    }
    
    void dfs(TreeNode* root, vector<int>& v, int level) {
        if (!root) return;
        // 下面这个条件，保证如果右子树中某个level没有，回到左子树中，不会重复插入同一个level的结点。
        if (v.size() == level) v.push_back(root->val);
        
        dfs(root->right, v, level+1); // 先走右边。
        dfs(root->left, v, level+1);
    }
};
```

