# 671. Second Minimum Node In a Binary Tree

> Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly `two` or `zero` sub-node. If the node has two sub-nodes, then this node's value is the smaller value among its two sub-nodes. More formally, the property `root.val = min(root.left.val, root.right.val)` always holds.
>
> Given such a binary tree, you need to output the **second minimum** value in the set made of all the nodes' value in the whole tree.
>
> If no such second minimum value exists, output -1 instead.
>
> **Example 1:**
>
> ```
> Input: 
>     2
>    / \
>   2   5
>      / \
>     5   7
> 
> Output: 5
> Explanation: The smallest value is 2, the second smallest value is 5.
> ```
>
> **Example 2:**
>
> ```
> Input: 
>     2
>    / \
>   2   2
> 
> Output: -1
> Explanation: The smallest value is 2, but there isn't any second smallest value.
> ```

1. Easy。

```cpp
// 首先要读懂题目，一棵树，树根是最小的，所以输入的树的根也是整棵树最小的，然后搜索子树，如果子树的根比第一小的大，比第二小的小，那么更新第二小，然后就可以返回了，因为在这棵子树中，没有比树根更小的了，故没有搜索的价值。
class Solution {
    long candidate = LONG_MAX;
    int min1;
public:
    int findSecondMinimumValue(TreeNode* root) {
        if (!root) return -1;
        min1 = root->val; // 根是最小的。
        dfs(root);
        return candidate==LONG_MAX? -1: candidate;
    }
    
    void dfs(TreeNode* root) {
        if (!root) return;
        if (root->val > min1 && root->val < candidate) {
            candidate = root->val;
        } else {
            dfs(root->left);
            dfs(root->right);
        }
    }
};
```

