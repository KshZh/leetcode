# 652. Find Duplicate Subtrees

> Given a binary tree, return all duplicate subtrees. For each kind of duplicate subtrees, you only need to return the root node of any **one** of them.
>
> Two trees are duplicate if they have the same structure with same node values.
>
> **Example 1:**
>
> ```
>         1
>        / \
>       2   3
>      /   / \
>     4   2   4
>        /
>       4
> ```
>
> The following are two duplicate subtrees:
>
> ```
>       2
>      /
>     4
> ```
>
> and
>
> ```
>     4
> ```
>
> Therefore, you need to return above trees' root in the form of a list.

1. Medium。

> #### Approach #1: Depth-First Search [Accepted]
>
> **Intuition**
>
> We can serialize each subtree. For example, the tree
>
> ```python
>    1
>   / \
>  2   3
>     / \
>    4   5
> ```
>
> can be represented as the serialization `1,2,#,#,3,4,#,#,5,#,#`, which is a unique representation of the tree.

1. Medium。

```java
class Solution {
    Map<String, Integer> count;
    List<TreeNode> ans;
    public List<TreeNode> findDuplicateSubtrees(TreeNode root) {
        count = new HashMap();
        ans = new ArrayList();
        collect(root);
        return ans;
    }

    public String collect(TreeNode node) {
        if (node == null) return "#";
        String serial = node.val + "," + collect(node.left) + "," + collect(node.right);
        count.put(serial, count.getOrDefault(serial, 0) + 1);
        if (count.get(serial) == 2)
            ans.add(node);
        return serial;
    }
}
```

