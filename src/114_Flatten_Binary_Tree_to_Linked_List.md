# 114. Flatten Binary Tree to Linked List

> Given a binary tree, flatten it to a linked list in-place.
>
> For example, given the following tree:
>
> ```
>     1
>    / \
>   2   5
>  / \   \
> 3   4   6
> ```
>
> The flattened tree should look like:
>
> ```
> 1
>  \
>   2
>    \
>     3
>      \
>       4
>        \
>         5
>          \
>           6
> ```

1. Medium。

```cpp
class Solution {
public:
    void flatten(TreeNode* root) {
        if (!root) return;
        doFlatten(root);
    }
    
    // 递归函数的宏观设计，输入输出。
    // 该函数接受一棵树，将该树按题目要求压平后输出最后一个结点的地址。
    // 要求输入的树不为空。
    TreeNode* doFlatten(TreeNode* root) {
        if (!root->left && !root->right) return root;
        // 没有左子树，那么递归压平右子树。
        if (!root->left) return doFlatten(root->right);
        // 压平左子树，得到压平后左子树的最后一个结点，连接右子树。
        // 若右子树不为空则递归压平右子树。
        TreeNode* p = doFlatten(root->left);
        p->right = root->right;
        root->right = root->left;
        root->left = nullptr;
        return p->right? doFlatten(p->right): p;
    }
};
```

```java
// https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/36977/My-short-post-order-traversal-Java-solution-for-share
// 很简洁，但不太好理解。
private TreeNode prev = null;

public void flatten(TreeNode root) {
    if (root == null)
        return;
    flatten(root.right);
    flatten(root.left);
    root.right = prev;
    root.left = null;
    prev = root;
}
```

```java
// 有点像遍历二叉树的Morris算法。
// O(N)时间复杂度，因为每个结点被now遍历一次，被pre最多遍历一次。
class Solution {
public:
    void flatten(TreeNode *root) {
		TreeNode*now = root;
		while (now)
		{
			if(now->left)
			{
                //Find current node's prenode that links to current node's right subtree
				TreeNode* pre = now->left;
				while(pre->right)
				{
					pre = pre->right;
				}
				pre->right = now->right;
                //Use current node's left subtree to replace its right subtree(original right 
                //subtree is already linked by current node's prenode
				now->right = now->left;
				now->left = NULL;
			}
			now = now->right;
		}
    }
};
```

