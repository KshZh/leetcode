# 894. All Possible Full Binary Trees

> A *full binary tree* is a binary tree where each node has exactly 0 or 2 children.
>
> Return a list of all possible full binary trees with `N` nodes. Each element of the answer is the root node of one possible tree.
>
> Each `node` of each tree in the answer **must** have `node.val = 0`.
>
> You may return the final list of trees in any order.
>
> **Example 1:**
>
> ```
> Input: 7
> Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
> Explanation:
> ```
>
> **Note:**
>
> - `1 <= N <= 20`

1. Medium。

```cpp
// 带缓存的分治策略，注意到有一些子树是被多个结点连向/共享。
class Solution {
    unordered_map<int, vector<TreeNode*>> cache;
public:
    vector<TreeNode*> allPossibleFBT(int N) {
        if (cache.find(N) != cache.end()) return cache[N];
        if (N == 1) return {new TreeNode(0)};
        TreeNode* root;
        vector<TreeNode*> ret;
        for (int i=1; i<N; i+=2) {
            vector<TreeNode*> left = allPossibleFBT(i);
            vector<TreeNode*> right = allPossibleFBT(N-i-1);
            for (auto* l: left) {
                for (auto* r: right) {
                    root = new TreeNode(0);
                    root->left = l;
                    root->right = r;
                    ret.push_back(root);
                }
            }
        }
        cache[N] = ret;
        return ret;
    }
};
```

