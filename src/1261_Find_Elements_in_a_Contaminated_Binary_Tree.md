# 1261. Find Elements in a Contaminated Binary Tree

> Given a binary tree with the following rules:
>
> 1. `root.val == 0`
> 2. If `treeNode.val == x` and `treeNode.left != null`, then `treeNode.left.val == 2 * x + 1`
> 3. If `treeNode.val == x` and `treeNode.right != null`, then `treeNode.right.val == 2 * x + 2`
>
> Now the binary tree is contaminated, which means all `treeNode.val` have been changed to `-1`.
>
> You need to first recover the binary tree and then implement the `FindElements` class:
>
> - `FindElements(TreeNode* root)` Initializes the object with a contamined binary tree, you need to recover it first.
> - `bool find(int target)` Return if the `target` value exists in the recovered binary tree.
>
> **Example 1:**
>
> **![img](https://assets.leetcode.com/uploads/2019/11/06/untitled-diagram-4-1.jpg)**
>
> ```
> Input
> ["FindElements","find","find"]
> [[[-1,null,-1]],[1],[2]]
> Output
> [null,false,true]
> Explanation
> FindElements findElements = new FindElements([-1,null,-1]); 
> findElements.find(1); // return False 
> findElements.find(2); // return True 
> ```
>
> **Example 2:**
>
> **![img](https://assets.leetcode.com/uploads/2019/11/06/untitled-diagram-4.jpg)**
>
> ```
> Input
> ["FindElements","find","find","find"]
> [[[-1,-1,-1,-1,-1]],[1],[3],[5]]
> Output
> [null,true,true,false]
> Explanation
> FindElements findElements = new FindElements([-1,-1,-1,-1,-1]);
> findElements.find(1); // return True
> findElements.find(3); // return True
> findElements.find(5); // return False
> ```
>
> **Example 3:**
>
> **![img](https://assets.leetcode.com/uploads/2019/11/07/untitled-diagram-4-1-1.jpg)**
>
> ```
> Input
> ["FindElements","find","find","find","find"]
> [[[-1,null,-1,-1,null,-1]],[2],[3],[4],[5]]
> Output
> [null,true,false,false,true]
> Explanation
> FindElements findElements = new FindElements([-1,null,-1,-1,null,-1]);
> findElements.find(2); // return True
> findElements.find(3); // return False
> findElements.find(4); // return False
> findElements.find(5); // return True
> ```
>
> **Constraints:**
>
> - `TreeNode.val == -1`
> - The height of the binary tree is less than or equal to `20`
> - The total number of nodes is between `[1, 10^4]`
> - Total calls of `find()` is between `[1, 10^4]`
> - `0 <= target <= 10^6`

1. Medium。

```cpp
class FindElements {
    void dfs1(TreeNode* root) {
        if (!root) return;
        if (root->left) {
            root->left->val=root->val*2+1;
            dfs1(root->left);
        }
        if (root->right) {
            root->right->val=root->val*2+2;
            dfs1(root->right);
        }
    }
    
    bool dfs2(TreeNode* root, int x) {
        if (!root) return false;
        if (root->val == x) return true;
        return dfs2(root->left, x) || dfs2(root->right, x);
    }
    
    TreeNode* root_;
public:
    FindElements(TreeNode* root) {
        root_ = root;
        if (root) {
            root->val = 0;
            dfs1(root);
        }
    }
    
    bool find(int target) {
        return dfs2(root_, target);
    }
};
```

```cpp
// 用哈希表缓存查询结果，使得查询O(1)，而不是每次查询都dfs。
class FindElements {
    void dfs1(TreeNode* root) {
        if (!root) return;
        cache_.insert(root->val);
        if (root->left) {
            root->left->val=root->val*2+1;
            dfs1(root->left);
        }
        if (root->right) {
            root->right->val=root->val*2+2;
            dfs1(root->right);
        }
    }
    
    TreeNode* root_;
    unordered_set<int> cache_;
public:
    FindElements(TreeNode* root) {
        root_ = root;
        if (root) {
            root->val = 0;
            dfs1(root);
        }
    }
    
    bool find(int target) {
        return cache_.find(target)!=cache_.end();
    }
};
```

