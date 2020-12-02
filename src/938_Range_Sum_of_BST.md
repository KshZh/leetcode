# 938. Range Sum of BST

> Given the `root` node of a binary search tree, return the sum of values of all nodes with value between `L` and `R` (inclusive).
>
> The binary search tree is guaranteed to have unique values.
>
> **Example 1:**
>
> ```
> Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
> Output: 32
> ```
>
> **Example 2:**
>
> ```
> Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
> Output: 23
> ```
>
> **Note:**
>
> 1. The number of nodes in the tree is at most `10000`.
> 2. The final answer is guaranteed to be less than `2^31`.

1. Easy。

```cpp
// 因为BST的定义就是右子树大于根，左子树小于根，所以当根小于L时，其左子树必定小于L，剪掉，但其右子树可能大于等于L，需要继续递归处理。同理当根大于R时，剪掉右子树，递归处理左子树。
// 总结起来也就是如果根大于L，那么其左子树可能存在元素在[L, root)中，递归处理左子树，如果根小于R，那么其右子数可能存在元素在(root, R]中，递归处理右子树。
int rangeSumBST(TreeNode* root, int L, int R) {
    if (!root) return 0;
    // if (root->val<L || root->val>R) return 0; 
    // 根可能小于L，但它的右子树可能大于等于L，所以不能马上返回。
    int sum = 0;
    if (root->val>=L && root->val<=R)
        sum += root->val;
    if (root->val > L)
        sum += rangeSumBST(root->left, L, R);
    if (root->val < R)
        sum += rangeSumBST(root->right, L, R);
    return sum;
}
```

```cpp
// 迭代版，对于迭代版，重点在于记住栈后进先出，也就是最近才进的先出，然后结合代码想象遍历过程。
// 先序遍历，中右左。
int rangeSumBST(TreeNode* root, int L, int R) {
    if (!root) return 0;
    stack<TreeNode*> s;
    s.push(root);
    TreeNode* x;
    int sum = 0;
    while (!s.empty()) {
        x = s.top();
        s.pop();
        if (x->val>=L && x->val<=R)
            sum += x->val;
        if (x->val>L && x->left)
            s.push(x->left); // 先推入左子树，所以会先访问右子树。
        if (x->val<R && x->right)
            s.push(x->right);
    }
    return sum;
}
```

