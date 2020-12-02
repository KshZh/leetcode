# 563. Binary Tree Tilt

> Given a binary tree, return the tilt of the **whole tree**.
>
> The tilt of a **tree node** is defined as the **absolute difference** between the sum of all left subtree node values and the sum of all right subtree node values. Null node has tilt 0.
>
> The tilt of the **whole tree** is defined as the sum of all nodes' tilt.
>
> **Example:**
>
> ```
> Input: 
>          1
>        /   \
>       2     3
> Output: 1
> Explanation: 
> Tilt of node 2 : 0
> Tilt of node 3 : 0
> Tilt of node 1 : |2-3| = 1
> Tilt of binary tree : 0 + 0 + 1 = 1
> ```
>
> **Note:**
>
> 1. The sum of node values in any subtree won't exceed the range of 32-bit integer.
> 2. All the tilt values won't exceed the range of 32-bit integer.

1. Easy。

```cpp
class Solution {
    unordered_map<TreeNode*, int> cache;
public:
    int findTilt(TreeNode* root) {
        if (!root || (!root->left && !root->right)) return 0;
        // 自顶向下。
        return abs(sum(root->left)-sum(root->right))+findTilt(root->left)+findTilt(root->right);
    }
    
    int sum(TreeNode* root) {
        if (!root) return 0;
        if (!root->left && !root->right) return root->val;
        if (cache.find(root) != cache.end()) return cache[root];
        cache[root] = sum(root->left)+sum(root->right)+root->val;
        return cache[root];
    }
};
```

```java
public class Solution {
    int tilt = 0;
    public int findTilt(TreeNode root) {
        // 自底向上。
        traverse(root);
        return tilt;
    }
    public int traverse(TreeNode root)
    {
        if (root == null )
            return 0;
        int left = traverse(root.left);
        int right = traverse(root.right);
        tilt += Math.abs(left-right);
        return left + right + root.val;
    }
}
```



