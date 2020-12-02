# 1325. Delete Leaves With a Given Value

> Given a binary tree `root` and an integer `target`, delete all the **leaf nodes** with value `target`.
>
> Note that once you delete a leaf node with value `target`**,** if it's parent node becomes a leaf node and has the value `target`, it should also be deleted (you need to continue doing that until you can't).
>
> **Example 1:**
>
> **![img](https://assets.leetcode.com/uploads/2020/01/09/sample_1_1684.png)**
>
> ```
> Input: root = [1,2,3,2,null,2,4], target = 2
> Output: [1,null,3,null,4]
> Explanation: Leaf nodes in green with value (target = 2) are removed (Picture in left). 
> After removing, new nodes become leaf nodes with value (target = 2) (Picture in center).
> ```
>
> **Example 2:**
>
> **![img](https://assets.leetcode.com/uploads/2020/01/09/sample_2_1684.png)**
>
> ```
> Input: root = [1,3,3,3,2], target = 3
> Output: [1,3,null,null,2]
> ```
>
> **Example 3:**
>
> **![img](https://assets.leetcode.com/uploads/2020/01/15/sample_3_1684.png)**
>
> ```
> Input: root = [1,2,null,2,null,2], target = 2
> Output: [1]
> Explanation: Leaf nodes in green with value (target = 2) are removed at each step.
> ```
>
> **Example 4:**
>
> ```
> Input: root = [1,1,1], target = 1
> Output: []
> ```
>
> **Example 5:**
>
> ```
> Input: root = [1,2,3], target = 1
> Output: [1,2,3]
> ```
>
> **Constraints:**
>
> - `1 <= target <= 1000`
> - Each tree has at most `3000` nodes.
> - Each node's value is between `[1, 1000]`.

1. Medium。

```cpp
class Solution {
public:
    TreeNode* removeLeafNodes(TreeNode* root, int target) {
        // 因为当前结点可能变成叶子，所以用后序遍历，
        // 如果其子树被删掉了导致当前结点变成了叶子，
        // 那就可以顺便处理。
        if (!root) return root;
        root->left = removeLeafNodes(root->left, target);
        root->right = removeLeafNodes(root->right, target);
        if (!root->left && !root->right && root->val==target) {
            // delete root;
            return nullptr;
        }
        return root;
    }
};
```

