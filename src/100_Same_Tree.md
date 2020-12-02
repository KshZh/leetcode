# 100. Same Tree

> Given two binary trees, write a function to check if they are the same or not.
>
> Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

1. Easy。

```cpp
// 递归。
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        if (!p && !q) return true;
        if (!p || !q) return false;
        return p->val==q->val && isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
    }
};
```

```cpp
// 迭代。
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
        queue<pair<TreeNode*, TreeNode*>> que;
        que.push({p, q});
        while (!que.empty()) {
            auto x = que.front();
            que.pop();
            if (!x.first && !x.second) continue;
            if (!x.first || !x.second) return false;
            if (x.first->val != x.second->val) return false;
            que.push({x.first->left, x.second->left});
            que.push({x.first->right, x.second->right});
        }
        return true;
    }
};
```

