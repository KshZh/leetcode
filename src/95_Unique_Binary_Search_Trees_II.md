# 95. Unique Binary Search Trees II

> Given an integer *n*, generate all structurally unique **BST's** (binary search trees) that store values 1 ... *n*.
>
> **Example:**
>
> ```
> Input: 3
> Output:
> [
>   [1,null,3,2],
>   [3,2,null,1],
>   [3,1,null,null,2],
>   [2,1,3],
>   [1,null,2,null,3]
> ]
> Explanation:
> The above output corresponds to the 5 unique BST's shown below:
> 
>    1         3     3      2      1
>     \       /     /      / \      \
>      3     2     1      1   3      2
>     /     /       \                 \
>    2     1         2                 3
> ```

1. Medium，树，dp，分治。

```cpp
class Solution {
public:
    vector<TreeNode*> generateTrees(int n) {
        if (n == 0) return {};
        vector<vector<TreeNode*>> dp(n+1);
        dp[0] = {nullptr};
        for (int len=1; len<=n; len++) {
            for (int root=1; root<=len; root++) {
                // 扩展`dp[i] += dp[j-1]*dp[i-j];`。
                for (auto* left: dp[root-1]) {
                    for (auto* right: dp[len-root]) {
                        auto* t = new TreeNode(root);
                        t->left = left;
                        t->right = clone(right, root); // dp[len-root]这些树的结点值范围在[1, len-root]，这里要映射到[root+1, len]
                        dp[len].push_back(t);
                    }
                }
            }
        }
        return dp[n];
    }
    
    // 树的处理与递归相性很高。
    TreeNode* clone(TreeNode* t, int offset) {
        if (!t) return nullptr;
        auto* x = new TreeNode(t->val+offset);
        x->left = clone(t->left, offset);
        x->right = clone(t->right, offset);
        return x;
    }
};
```

```cpp
class Solution {
public:
    vector<TreeNode*> generateTrees(int n) {
        if (n == 0) return {};
        return divideAndConquer(1, n);
    }
    
    // [start, end].
    vector<TreeNode*> divideAndConquer(int start, int end) {
        if (start > end) return {nullptr};
        if (start == end) return {new TreeNode(start)};
        
        vector<TreeNode*> ans;
        TreeNode* x;
        for (int root=start; root<=end; root++) {
            auto lefts = divideAndConquer(start, root-1);
            auto rights = divideAndConquer(root+1, end);
            
            for (auto* l: lefts) {
                for (auto* r: rights) {
                    x = new TreeNode(root);
                    x->left = l;
                    x->right = r;
                    ans.push_back(x);
                }
            }
        }
        return ans;
    }
};
```

