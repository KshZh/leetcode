# 450. Delete Node in a BST

> Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.
>
> Basically, the deletion can be divided into two stages:
>
> 1. Search for a node to remove.
> 2. If the node is found, delete the node.
>
> **Note:** Time complexity should be O(height of tree).
>
> **Example:**
>
> ```
> root = [5,3,6,2,4,null,7]
> key = 3
> 
>     5
>    / \
>   3   6
>  / \   \
> 2   4   7
> 
> Given key to delete is 3. So we find the node with value 3 and delete it.
> 
> One valid answer is [5,4,6,2,null,null,7], shown in the following BST.
> 
>     5
>    / \
>   4   6
>  /     \
> 2       7
> 
> Another valid answer is [5,2,6,null,4,null,7].
> 
>     5
>    / \
>   2   6
>    \   \
>     4   7
> ```

1. Medium。

```cpp
// 递归函数的宏观设计，输入是一棵树和该树中的一个结点的值，输出是正确删除了该结点的一棵树。
TreeNode* deleteNode(TreeNode* root, int key) {
    if (!root) return root;
    if (root->val == key) {
        // 如果没有左子树，那就直接返回右子树。
        if (!root->left) {
            auto* p = root->right;
            delete root;
            return p;
        }
        // 同上。
        if (!root->right) {
            auto* p = root->left;
            delete root;
            return p;
        }
        // 否则，找到左子树中最大的结点替代当前被要被删除的根。
        // 这样新的根才能大于左子树，仍小于右子数，保持BST的性质。
        // 当然也可以找到右子数中最小的结点替代当前将要被删除的根，
        // 这样新的根才能小于右子数，仍大于左子树，保持BST的性质。
        auto* p = root->left;
        while (p->right) {
            p = p->right;
        }
        root->val = p->val;
        root->left = deleteNode(root->left, root->val);
    } else if (root->val > key) {
        root->left = deleteNode(root->left, key);
    } else {
        root->right = deleteNode(root->right, key);
    }
    return root;
}
```

```cpp
// 迭代版。
// 给定一个结点值，在bst中搜索的迭代实现是很容易的，因为根据bst的性质，每次可以在两个方向/子树中明确一个方向，而普通二叉树则无法给出一个值，在一个根处确定两个方向中的一个，可能选错了子树，就需要回来搜另一棵子树。
TreeNode* deleteNode(TreeNode* root, int key) {
    TreeNode* p = root;
    TreeNode* q{};
    while (p && p->val!=key) {
        q = p;
        if (key < p->val)
            p = p->left;
        else
            p = p->right;
    }
    if (!p) // key不在树中。
        return root;
    if (!q)
        return deleteRoot(root);
    if (q->left == p) {
        q->left = deleteRoot(q->left);
    } else {
        q->right = deleteRoot(q->right);
    }
    return root;
}

TreeNode* deleteRoot(TreeNode* root) {
    TreeNode* x;
    if (!root->left) {
        x = root->right;
        delete root;
        return x;
    }
    if (!root->right) {
        x = root->left;
        delete root;
        return x;
    }
    TreeNode* p = root->left;
    TreeNode* q = root;
    while (p->right) {
        q = p;
        p = p->right;
    }
    // 下面这段调整结点的代码值得学习。
    // p作为新的根。
    p->right = root->right;
    if (root->left != p) {
        // 如果新的根不是原根的左子结点，
        q->right = p->left;
        p->left = root->left;
    }
    delete root;
    return p;
}
```

