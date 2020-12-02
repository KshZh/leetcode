# [235. Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)

> Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
>
> According to the [definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor): “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow **a node to be a descendant of itself**).”
>
> Given binary search tree: root = [6,2,8,0,4,7,9,null,null,3,5]
>
> ![img](https://assets.leetcode.com/uploads/2018/12/14/binarysearchtree_improved.png)
>
>  
>
> **Example 1:**
>
> ```
> Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
> Output: 6
> Explanation: The LCA of nodes 2 and 8 is 6.
> ```
>
> **Example 2:**
>
> ```
> Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
> Output: 2
> Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.
> ```
>
>  
>
> **Note:**
>
> - All of the nodes' values will be unique.
> - p and q are different and both values will exist in the BST.

```java
// 时间复杂度为O(N)，最坏情况下树为单链表。
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {

        // Value of current node or parent node.
        int parentVal = root.val;

        // Value of p
        int pVal = p.val;

        // Value of q;
        int qVal = q.val;

        if (pVal > parentVal && qVal > parentVal) {
            // If both p and q are greater than parent
            return lowestCommonAncestor(root.right, p, q);
        } else if (pVal < parentVal && qVal < parentVal) {
            // If both p and q are lesser than parent
            return lowestCommonAncestor(root.left, p, q);
        } else {
            // We have found the split point, i.e. the LCA node.
            return root;
        }
    }
}
// 注意不能直接比较p和root的地址，因为可能p不是直接从树中取的，而是另外创建的结点。
```

```java
// 尾递归转换为迭代。
class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {

        // Value of p
        int pVal = p.val;

        // Value of q;
        int qVal = q.val;

        // Start from the root node of the tree
        TreeNode node = root;

        // Traverse the tree
        while (node != null) {

            // Value of ancestor/parent node.
            int parentVal = node.val;

            if (pVal > parentVal && qVal > parentVal) {
                // If both p and q are greater than parent
                node = node.right;
            } else if (pVal < parentVal && qVal < parentVal) {
                // If both p and q are lesser than parent
                node = node.left;
            } else {
                // We have found the split point, i.e. the LCA node.
                return node;
            }
        }
        return null;
    }
}
```

# [236. Lowest Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)

> Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.
>
> According to the [definition of LCA on Wikipedia](https://en.wikipedia.org/wiki/Lowest_common_ancestor): “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow **a node to be a descendant of itself**).”
>
> Given the following binary tree: root = [3,5,1,6,2,0,8,null,null,7,4]
>
> ![img](https://assets.leetcode.com/uploads/2018/12/14/binarytree.png)
>
>  
>
> **Example 1:**
>
> ```
> Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
> Output: 3
> Explanation: The LCA of nodes 5 and 1 is 3.
> ```
>
> **Example 2:**
>
> ```
> Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
> Output: 5
> Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant of itself according to the LCA definition.
> ```
>
>  
>
> **Note:**
>
> - All of the nodes' values will be unique.
> - p and q are different and both values will exist in the binary tree.

```java
// 与上一题不同的是，BST中走哪一个分支是可以提前确定的，走其中一个分支即可。这里无法确定，两个分支都要走，然后依靠返回值进行计算。
class Solution {
public:
    // 这个递归函数输入一棵树，返回（传递回上层调用/沿路径往上传递回去）：
    // 1. nullptr，表明这棵树中不存在p或q或p和q的lca；
    // 2. p和q的lca（包括p的lca为q和q的lca为p的情况），或者p，或者q。
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        // 这个谓词也处理了p是q的lca和q是p的lca的情况，即p在q的子树中，或q在p的子树中，这两种情况可以直接返回q或p，不必再搜索。
        if (!root || root == p || root == q) return root;
        TreeNode* left = lowestCommonAncestor(root->left, p, q);
        TreeNode* right = lowestCommonAncestor(root->right, p, q);
        // 如果left和right都不为nullptr，即p和q分别在root的两个子树中，那么当前root就是lca，返回root，传递回去。
        return !left ? right : !right ? left : root;
    }
};
```

