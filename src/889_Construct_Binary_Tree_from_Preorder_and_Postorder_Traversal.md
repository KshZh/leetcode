# 889. Construct Binary Tree from Preorder and Postorder Traversal

> Return any binary tree that matches the given preorder and postorder traversals.
>
> Values in the traversals `pre` and `post` are distinct positive integers.
>
> **Example 1:**
>
> ```
> Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
> Output: [1,2,3,4,5,6,7]
> ```
>
> **Note:**
>
> - `1 <= pre.length == post.length <= 30`
> - `pre[]` and `post[]` are both permutations of `1, 2, ..., pre.length`.
> - It is guaranteed an answer exists. If there exists multiple answers, you can return any of them.

1. Medium。

```cpp
// O(N^2), O(height)，height最大为N，即单链表。
TreeNode* constructFromPrePost(vector<int>& pre, vector<int>& post) {
    // 先序和后序序列无法唯一确定一棵二叉树。根左右和左右根，
    // 比如AB,BA，可以是[A, B, null]，也可以是[A, null, B]。
    return f(pre, post, 0, post.size()-1, post.size());
}

TreeNode* f(vector<int>& pre, vector<int>& post, int preI, int postI, int len) {
    if (len == 0) return nullptr;
    TreeNode* root = new TreeNode(pre[preI]);
    int i;
    for (i=postI-1; i>postI-len && post[i]!=pre[preI+1]; i--)
        ;
    int rightSubLen = postI-i-1;
    int leftSubLen = len-rightSubLen-1; // 记得减一减掉当前根。
    root->left = f(pre, post, preI+1, i, leftSubLen);
    root->right = f(pre, post, preI+1+leftSubLen, postI-1, rightSubLen);
    return root;
}
```

```cpp
// https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/discuss/161268/C%2B%2BJavaPython-One-Pass-Real-O(N)
// O(N), O(height)
// 如果给出先序/后序和中序，好像就不能用这个方法。
int preIndex = 0, posIndex = 0;
TreeNode* constructFromPrePost(vector<int>& pre, vector<int>& post) {
    TreeNode* root = new TreeNode(pre[preIndex++]); // A
    if (root->val != post[posIndex])
        root->left = constructFromPrePost(pre, post); // B
    // else root->val==post[posIndex]，即左右子树已经构造完成。
    if (root->val != post[posIndex])
        root->right = constructFromPrePost(pre, post); // C
    posIndex++; // D
    // ABC是先序遍历，BCD是后序遍历。
    return root;
}
```

