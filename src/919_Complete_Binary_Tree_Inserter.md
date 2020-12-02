# 919. Complete Binary Tree Inserter

> A *complete* binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.
>
> Write a data structure `CBTInserter` that is initialized with a complete binary tree and supports the following operations:
>
> - `CBTInserter(TreeNode root)` initializes the data structure on a given tree with head node `root`;
> - `CBTInserter.insert(int v)` will insert a `TreeNode` into the tree with value `node.val = v` so that the tree remains complete, **and returns the value of the parent of the inserted `TreeNode`**;
> - `CBTInserter.get_root()` will return the head node of the tree.
>
> **Example 1:**
>
> ```
> Input: inputs = ["CBTInserter","insert","get_root"], inputs = [[[1]],[2],[]]
> Output: [null,1,[1,2]]
> ```
>
> **Example 2:**
>
> ```
> Input: inputs = ["CBTInserter","insert","insert","get_root"], inputs = [[[1,2,3,4,5,6]],[7],[8],[]]
> Output: [null,3,4,[1,2,3,4,5,6,7,8]]
> ```
>
> **Note:**
>
> 1. The initial given tree is complete and contains between `1` and `1000` nodes.
> 2. `CBTInserter.insert` is called at most `10000` times per test case.
> 3. Every value of a given or inserted node is between `0` and `5000`.

1. Medium。

```cpp
// 完全二叉树用数组存储，从1开始，对于结点i，其左子结点在2*i，右子结点在2*i+1，其父结点在i/2。
class CBTInserter {
    vector<TreeNode*> cbt;
public:
    CBTInserter(TreeNode* root): cbt(1) {
        queue<TreeNode*> q;
        q.push(root);
        TreeNode* x;
        while (!q.empty()) {
            x = q.front();
            q.pop();
            cbt.push_back(x);
            if (x->left) q.push(x->left);
            if (x->right) q.push(x->right);
        }
    }
    
    int insert(int v) {
        cbt.push_back(new TreeNode(v));
        auto* p = cbt[(cbt.size()-1)/2];
        if ((cbt.size()-1)%2 == 0)
            p->left = cbt.back();
        else
            p->right = cbt.back();
        return p->val;
    }
    
    TreeNode* get_root() {
        return cbt[1];
    }
};
```

