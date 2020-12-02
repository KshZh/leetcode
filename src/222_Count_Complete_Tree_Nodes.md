# 222. Count Complete Tree Nodes

> Given a **complete** binary tree, count the number of nodes.
>
> **Note:**
>
> **Definition of a complete binary tree from [Wikipedia](http://en.wikipedia.org/wiki/Binary_tree#Types_of_binary_trees):**
> In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.
>
> **Example:**
>
> ```
> Input: 
>     1
>    / \
>   2   3
>  / \  /
> 4  5 6
> 
> Output: 6
> ```

1. Medium。

```java
// 时间复杂度O(N)。
class Solution {
    public int countNodes(TreeNode root) {
        if (root == null) return 0;
        return dfs(root, 1);
    }
    
    // 完全二叉树用数组存储，从下标1开始，
    // 对于结点i，左孩子下标是i*2，右孩子下标是i*2+1。
    // dfs输入一棵树和该树的根在数组中的下标，返回子树中叶子最大的下标。
    int dfs(TreeNode root, int pos) {
        if (root==null) return -1;
        if (root.left==null && root.right==null) return pos;
        return Math.max(dfs(root.left, pos*2), dfs(root.right, pos*2+1));
    }
}
```

```java
// 和上面的实现复杂度相同，但更简洁。countNodes()本身就是递归的。
class Solution {
    public int countNodes(TreeNode root) {
        if (root == null) return 0;
        return 1+countNodes(root.left)+countNodes(root.right); // 左右子树结点数加上当前根一个结点。
    }
}
```

```cpp
class Solution {
public:
    int countNodes(TreeNode* root) {

        if(!root) return 0;

        int hl=0, hr=0;

        TreeNode *l=root, *r=root;

        while(l) {hl++;l=l->left;}

        while(r) {hr++;r=r->right;}

        if(hl==hr) return pow(2,hl)-1;

        return 1+countNodes(root->left)+countNodes(root->right);

    }
};
```

> Let n be the total number of the tree. It is likely that **you will get a child tree as a perfect binary tree and a non-perfect binary tree** (T(n/2)) at each level.（lgn是树的高度）
>
> ```
> T(n) = T(n/2) + c1 lgn
>        = T(n/4) + c1 lgn + c2 (lgn - 1)
>        = ...
>        = T(1) + c [lgn + (lgn-1) + (lgn-2) + ... + 1]
>        = O(lgn*lgn)   
> ```