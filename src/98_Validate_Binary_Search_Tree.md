# 98. Validate Binary Search Tree

> Given a binary tree, determine if it is a valid binary search tree (BST).
>
> Assume a BST is defined as follows:
>
> - The left subtree of a node contains only nodes with keys **less than** the node's key.
> - The right subtree of a node contains only nodes with keys **greater than** the node's key.
> - Both the left and right subtrees must also be binary search trees.
>
> **Example 1:**
>
> ```
>     2
>    / \
>   1   3
> 
> Input: [2,1,3]
> Output: true
> ```
>
> **Example 2:**
>
> ```
>     5
>    / \
>   1   4
>      / \
>     3   6
> 
> Input: [5,1,4,null,null,3,6]
> Output: false
> Explanation: The root node's value is 5 but its right child's value is 4.
> ```

1. Medium。

```cpp
// 利用二叉搜索树的性质：BST的中序序列是一个非递减序列。
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        if (!root) return true;
        vector<int> sorted;
        inorderTraversal(root, sorted);
        // int i;
        // for (i=0; i<sorted.size()-1; i++) {
        //     if (sorted[i] >= sorted[i+1])
        //         break;
        // }
        // return i==sorted.size()-1;
        int i;
        // 也做一个dummy prev来进行比较。
        // int prev = INT_MIN; // 测试用例居然有[-2147483648]，丧心病狂。
        long prev = LONG_MIN;
        for (i=0; i<sorted.size(); i++) {
            if (sorted[i] <= prev)
                break;
            prev = sorted[i];
        }
        return i==sorted.size();
    }
    
    void inorderTraversal(TreeNode* root, vector<int>& ret) {
        if (!root) return;
        if (!root->left && !root->right) {
            ret.push_back(root->val);
            return;
        }
        inorderTraversal(root->left, ret);
        ret.push_back(root->val);
        inorderTraversal(root->right, ret);
    }
};
```

```cpp
// 这是上面同一个思路的迭代版。
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        TreeNode* p = root;
        stack<TreeNode*> s;
        // 做一个dummy prev。
        // int prev = INT_MIN; // 测试用例居然有[-2147483648]，丧心病狂。
        long prev = LONG_MIN;
        while (!s.empty() || p) {
            // 走到该子树的最左结点。
            while (p) { // `if (p==nullptr) return;`.
                s.push(p);
                p = p->left;
            }
            // if (!s.empty()) // 多余的判断，因为while谓词的设置决定了这里必然不为空。
            // 返回后处理路径上的当前结点。
            p = s.top();
            s.pop();
            if (p->val <= prev)
                return false;
            prev = p->val;
            // if (p->right) // 如果有右子树，则处理右子树。
            // 这个判断也是多余的，因为如果没有右子树，那么下一次循环还会
            // 从取栈顶/路径中的结点回溯处理。
            p = p->right;
        }
        return true;
    }
};
```

```cpp
// 传递两个参数，root的左子树必须在(lower, root->val)范围内，root的右子树必须在(root->val, upper)范围内，lower和upper会在路径中传递给子树。
class Solution {
public:
    bool isValidBST(TreeNode* root) {
        return helper(root, LONG_MIN, LONG_MAX);
    }
    
    // root->val必须在(lower, upper)范围内。
    bool helper(TreeNode* root, long lower, long upper) {
        if (!root) return true;
        
        if (lower!=LONG_MIN && root->val<=lower) return false;
        if (upper!=LONG_MAX && root->val>=upper) return false;
        
        return helper(root->left, lower, root->val) && helper(root->right, root->val, upper);
    }
};
```

