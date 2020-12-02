# 1315. Sum of Nodes with Even-Valued Grandparent

> Given a binary tree, return the sum of values of nodes with even-valued grandparent. (A *grandparent* of a node is the parent of its parent, if it exists.)
>
> If there are no nodes with an even-valued grandparent, return `0`.
>
> **Example 1:**
>
> **![img](https://assets.leetcode.com/uploads/2019/07/24/1473_ex1.png)**
>
> ```
> Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
> Output: 18
> Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.
> ```
>
> **Constraints:**
>
> - The number of nodes in the tree is between `1` and `10^4`.
> - The value of nodes is between `1` and `100`.

1. Medium。

```cpp
int sumEvenGrandparent(TreeNode* root) {
    if (!root) return 0;
    int sum = 0;
    if ((root->val&1) == 0) {
        if (root->left) {
            if (root->left->left) sum += root->left->left->val;
            if (root->left->right) sum += root->left->right->val;
        }
        if (root->right) {
            if (root->right->left) sum += root->right->left->val;
            if (root->right->right) sum += root->right->right->val;
        }
    }
    return sum+sumEvenGrandparent(root->left)+sumEvenGrandparent(root->right);
}
```

```cpp
// Intuition
// Let children know who their grandparent is.
// Complexity
// Time O(N)
// Space O(height)
int sumEvenGrandparent(TreeNode* root, int p = 1, int gp = 1) {
    return root ? sumEvenGrandparent(root->left, root->val, p)
        + sumEvenGrandparent(root->right, root->val, p)
        + (gp % 2 ? 0 : root->val)  : 0;
}
```

