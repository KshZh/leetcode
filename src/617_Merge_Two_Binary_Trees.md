# 617. Merge Two Binary Trees

> **Example 1:**
>
> ```
> Input: 
> 	Tree 1                     Tree 2                  
>           1                         2                             
>          / \                       / \                            
>         3   2                     1   3                        
>        /                           \   \                      
>       5                             4   7                  
> Output: 
> Merged tree:
> 	     3
> 	    / \
> 	   4   5
> 	  / \   \ 
> 	 5   4   7
> ```

1. 树，Easy。
2. 这是一个二叉树的先序遍历，如果要求迭代版本，就是要自己维护一个栈来保存实参。

```cpp
/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
        if (t1==nullptr && t2==nullptr) {
            return nullptr;
        }
        TreeNode* t = new TreeNode((t1!=nullptr? t1->val: 0) + (t2!=nullptr? t2->val: 0));
        // TreeNode* t = new TreeNode(t1!=nullptr? t1->val: 0 + t2!=nullptr? t2->val: 0); // 注意要加括号设置优先级和结合性，否则可能就错了，实际执行的运算不是我们期望的。
        t->left = mergeTrees(t1!=nullptr? t1->left: nullptr, t2!=nullptr? t2->left: nullptr);
        t->right = mergeTrees(t1!=nullptr? t1->right: nullptr, t2!=nullptr? t2->right: nullptr);
        return t;
    }
};
```

```cpp
// 如果只是就地修改，
class Solution {
public:
    TreeNode* mergeTrees(TreeNode* t1, TreeNode* t2) {
        if (t1 == nullptr)
            return t2;
        if (t2 == nullptr)
            return t1;
        t1->val += t2->val;
        t1->left = mergeTrees(t1->left, t2->left);
        t1->right = mergeTrees(t1->right, t2->right);
        return t1;
    }
};
```

