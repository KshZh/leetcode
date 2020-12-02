#  897. Increasing Order Search Tree

> Given a binary search tree, rearrange the tree in **in-order** so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only 1 right child.
>
> ```
> Example 1:
> Input: [5,3,6,2,4,null,8,1,null,null,null,7,9]
> 
>        5
>       / \
>     3    6
>    / \    \
>   2   4    8
>  /        / \ 
> 1        7   9
> 
> Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]
> 
>  1
>   \
>    2
>     \
>      3
>       \
>        4
>         \
>          5
>           \
>            6
>             \
>              7
>               \
>                8
>                 \
>                  9  
> ```
>
> **Constraints:**
>
> - The number of nodes in the given tree will be between `1` and `100`.
> - Each node will have a unique integer value from `0` to `1000`.

1. Medium。

```cpp
class Solution {
    TreeNode* curr;
public:
    TreeNode* increasingBST(TreeNode* root) {
        if (!root) return {};
        TreeNode x(-1);
        curr = &x;
        dfs(root);
        return x.right;
    }
    
    // 输入一棵树，输出按照题目要求调整后的树。
    // 如果设计成返回调整后的树的最后一个结点，就很麻烦，因为这样返回后，上面的树不能接上这个调整好的子树。
    void dfs(TreeNode* root) {
        if (!root) return;
        dfs(root->left);
        curr->right = root;
        root->left = nullptr;
        curr = root;
        dfs(root->right);
    }
};
```

```cpp
// https://leetcode.com/problems/increasing-order-search-tree/discuss/165885/C%2B%2BJavaPython-Self-Explained-5-line-O(N)
// 输入一棵树和对该树进行中序遍历后的后继结点，返回按照题目要求调整后的树。
TreeNode* increasingBST(TreeNode* root, TreeNode* tail = NULL) {
    if (!root) return tail;
    TreeNode* res = increasingBST(root->left, root);
    root->left = NULL;
    root->right = increasingBST(root->right, tail);
    return res;
}
```

