# 623. Add One Row to Tree

> Given the root of a binary tree, then value `v` and depth `d`, you need to add a row of nodes with value `v` at the given depth `d`. The root node is at depth 1.
>
> The adding rule is: given a positive integer depth `d`, for each NOT null tree nodes `N` in depth `d-1`, create two tree nodes with value `v` as `N's` left subtree root and right subtree root. And `N's` **original left subtree** should be the left subtree of the new left subtree root, its **original right subtree** should be the right subtree of the new right subtree root. If depth `d` is 1 that means there is no depth d-1 at all, then create a tree node with value **v** as the new root of the whole original tree, and the original tree is the new root's left subtree.
>
> **Example 1:**
>
> ```
> Input: 
> A binary tree as following:
>        4
>      /   \
>     2     6
>    / \   / 
>   3   1 5   
> 
> v = 1
> 
> d = 2
> 
> Output: 
>        4
>       / \
>      1   1
>     /     \
>    2       6
>   / \     / 
>  3   1   5   
> ```
>
> **Example 2:**
>
> ```
> Input: 
> A binary tree as following:
>       4
>      /   
>     2    
>    / \   
>   3   1    
> 
> v = 1
> 
> d = 3
> 
> Output: 
>       4
>      /   
>     2
>    / \    
>   1   1
>       \  
> 3       1
> ```
>
> **Note:**
>
> 1. The given d is in range [1, maximum depth of the given tree + 1].
> 2. The given binary tree has at least one tree node.

1. Medium。

```cpp
// dfs.
class Solution {
public:
    // 这里假设题目给出的d是有效的。
    TreeNode* addOneRow(TreeNode* root, int v, int d) {
        if (d == 1) {
            TreeNode* p = new TreeNode(v);
            p->left = root;
            return p;
        }
        dfs(root, v, d, 1);
        return root;
    }
    
    void dfs(TreeNode* root, int v, int d, int currD) {
        if (!root) return;
        if (currD == d-1) {
            TreeNode* l = root->left;
            TreeNode* r = root->right;
            root->left = new TreeNode(v);
            root->right = new TreeNode(v);
            root->left->left = l;
            root->right->right = r;
        } else {
            dfs(root->left, v, d, currD+1);
            dfs(root->right, v, d, currD+1);
        }
    }
};
```

```cpp
// bfs.
class Solution {
public:
    TreeNode* addOneRow(TreeNode* root, int v, int d) {
        if (d == 1) {
            TreeNode* p = new TreeNode(v);
            p->left = root;
            return p;
        }
        queue<TreeNode*> q;
        q.push(root);
        int currD = 1;
        TreeNode *x, *l, *r;
        while (currD < d-1) {
            auto n = q.size();
            for (int i=0; i<n; i++) {
                x = q.front();
                q.pop();
                if (x->left) q.push(x->left);
                if (x->right) q.push(x->right);
            }
            currD++;
        }
        while (!q.empty()) {
            x = q.front();
            q.pop();
            l = x->left;
            r = x->right;
            x->left = new TreeNode(v);
            x->right = new TreeNode(v);
            x->left->left = l;
            x->right->right = r;
        }
        return root;
    }
};
```

