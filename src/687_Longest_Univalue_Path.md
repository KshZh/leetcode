# 687. Longest Univalue Path

> Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.
>
> The length of path between two nodes is represented by the number of edges between them.
>
> **Example 1:**
>
> **Input:**
>
> ```
>               5
>              / \
>             4   5
>            / \   \
>           1   1   5
> ```
>
> **Output:** 2
>
> **Example 2:**
>
> **Input:**
>
> ```
>               1
>              / \
>             4   5
>            / \   \
>           4   4   5
> ```
>
> **Output:** 2
>
> **Note:** The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.

1. Easy。

```cpp
// 自己写的实现，没有利用子调用返回的结果。
// 这里可以递归到最底下，把结果存储在全局变量中，然后返回/传递回当前结点其中满足条件的较长的一条子路径的长度。
class Solution {
public:
    int longestUnivaluePath(TreeNode* root) {
        if (!root) return 0;
        int curr = dfs(root->left, root->val)+dfs(root->right, root->val);
        return max(curr, max(longestUnivaluePath(root->left), longestUnivaluePath(root->right)));
    }
    
    int dfs(TreeNode* root, int target) {
        if (!root || root->val!=target) return 0;
        // 因为路径不能有岔路，即只能一路走到底，不能回头，
        // 所以选择两个子树中路径长度最长的走。
        return 1+max(dfs(root->left, target), dfs(root->right, target));
    }
};
```

```cpp
class Solution {
    int ans = 0;
public:
    int longestUnivaluePath(TreeNode* root) {
        dfs(root);
        return ans;
    }
    
    int dfs(TreeNode* root) {
        if (!root) return 0;
        int left = dfs(root->left);
        int right = dfs(root->right);
        int leftLen=0, rightLen=0;
        if (root->left && root->left->val==root->val) {
            // 满足这个条件，那么当前结点就可以接上左子树的univalue路径。
            leftLen = left+1;
        }
        if (root->right && root->right->val==root->val) {
            rightLen = right+1;
        }
        ans = max(ans, leftLen+rightLen); // 把结果存在一个全局变量中。
        // 返回经过当前结点的左右univalue子路径中较长的一条的长度。
        return max(leftLen, rightLen);
    }
};
```

