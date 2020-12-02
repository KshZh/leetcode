# 103. Binary Tree Zigzag Level Order Traversal

> Given a binary tree, return the *zigzag level order* traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).
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
> return its zigzag level order traversal as:
>
> ```
> [
>   [3],
>   [20,9],
>   [15,7]
> ]
> ```

1. Medium。

```cpp
class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        if (!root) return {};
        vector<vector<int>> res;
        queue<TreeNode*> q;
        q.push(root);
        TreeNode* p;
        int i, idx;
        size_t size;
        bool l2R = true;
        while (!q.empty()) {
            size = q.size();
            vector<int> v(size);
            for (i=0; i<size; i++) {
                p = q.front();
                q.pop();
                idx = l2R? i: size-1-i;
                v[idx] = p->val;
                if (p->left) q.push(p->left);
                if (p->right) q.push(p->right);
            }
            l2R = !l2R;
            res.push_back(move(v)); // 移动语义，避免拷贝堆内存。
        }
        return res;
    }
};
```

