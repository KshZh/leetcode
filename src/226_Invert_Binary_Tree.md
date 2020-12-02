# 226. Invert Binary Tree

> Invert a binary tree.
>
> **Example:**
>
> Input:
>
> ```
>      4
>    /   \
>   2     7
>  / \   / \
> 1   3 6   9
> ```
>
> Output:
>
> ```
>      4
>    /   \
>   7     2
>  / \   / \
> 9   6 3   1
> ```
>
> **Trivia:**
> This problem was inspired by [this original tweet](https://twitter.com/mxcl/status/608682016205344768) by [Max Howell](https://twitter.com/mxcl):
>
> > Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.

1. Easy。

```cpp
class Solution {
public:
    // invertTree()本身就是递归定义的。
    // 输入一棵树，输出反转后的这棵树。
    TreeNode* invertTree(TreeNode* root) {
        if (!root) return nullptr; // 空树直接返回空树。
        TreeNode* l = root->left;
        root->left = invertTree(root->right); // 让反转后的右子树作为左子树。
        root->right = invertTree(l); // 让反转后的左子树作为右子树。
        return root;
    }
};
```

```cpp
class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        // bfs.
        if (!root) return nullptr;
        queue<TreeNode*> q;
        q.push(root);
        TreeNode* x;
        while (!q.empty()) {
            x = q.front();
            q.pop();
            std::swap(x->left, x->right);
            if (x->left) q.push(x->left);
            if (x->right) q.push(x->right);
        }
        return root;
    }
};
```

