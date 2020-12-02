# 872. Leaf-Similar Trees

> Consider all the leaves of a binary tree. From left to right order, the values of those leaves form a *leaf value sequence.*
>
> <img src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/16/tree.png" alt="img" style="zoom:33%;" />
>
> For example, in the given tree above, the leaf value sequence is `(6, 7, 4, 9, 8)`.
>
> Two binary trees are considered *leaf-similar* if their leaf value sequence is the same.
>
> Return `true` if and only if the two given trees with head nodes `root1` and `root2` are leaf-similar.
>
> **Note:**
>
> - Both of the given trees will have between `1` and `100` nodes.

1. Easy。

```java
// 最朴素的实现。
class Solution {
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        List<Integer> leaves1 = new ArrayList();
        List<Integer> leaves2 = new ArrayList();
        dfs(root1, leaves1);
        dfs(root2, leaves2);
        return leaves1.equals(leaves2);
    }

    public void dfs(TreeNode node, List<Integer> leafValues) {
        if (node != null) {
            if (node.left == null && node.right == null)
                leafValues.add(node.val);
            dfs(node.left, leafValues);
            dfs(node.right, leafValues);
        }
    }
}
```

```cpp
// This is a great way to save some space when both tree are balanced. However, the description does not mention that trees are balanced trees. So the worst space complexity should be O(Height of T1 + Height of T2) considering the trees may be straight lists in worst case.
bool leafSimilar(TreeNode* root1, TreeNode* root2) {
    stack<TreeNode*> s1 , s2;
    s1.push(root1); s2.push(root2);
    while (!s1.empty() && !s2.empty())
        if (dfs(s1) != dfs(s2)) return false;
    return s1.empty() && s2.empty();
}

int dfs(stack<TreeNode*>& s) {
    while (true) {
        TreeNode* node = s.top(); s.pop();
        if (node->right) s.push(node->right);
        if (node->left) s.push(node->left);
        if (!node->left && !node->right) return node->val;
    }
}
```

