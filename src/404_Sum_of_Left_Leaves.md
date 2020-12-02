#  404. Sum of Left Leaves

> Find the sum of all left leaves in a given binary tree.
>
> **Example:**
>
> ```
>     3
>    / \
>   9  20
>     /  \
>    15   7
> 
> There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
> ```

1. Easy。

```java
class Solution {
    public int sumOfLeftLeaves(TreeNode root) {
        return dfs(root, false);
    }
    
    private int dfs(TreeNode root, boolean leftChild) {
        if (root == null) return 0;
        if (root.left==null && root.right==null) {
            if (leftChild) return root.val;
            return 0;
        }
        return dfs(root.left, true)+dfs(root.right, false);
    }
}
```

