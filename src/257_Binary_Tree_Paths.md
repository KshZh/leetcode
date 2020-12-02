#  257. Binary Tree Paths

> Given a binary tree, return all root-to-leaf paths.
>
> **Note:** A leaf is a node with no children.
>
> **Example:**
>
> ```
> Input:
> 
>    1
>  /   \
> 2     3
>  \
>   5
> 
> Output: ["1->2->5", "1->3"]
> 
> Explanation: All root-to-leaf paths are: 1->2->5, 1->3
> ```

1. Easy。

```cpp
class Solution {
public:
    vector<string> binaryTreePaths(TreeNode* root) {
        if (!root) return {};
        vector<string> res;
        vector<char> path;
        path.reserve(20); // 不是resize()，这个改变的是size，而不是capacity。
        dfs(root, res, path);
        return res;
    }
    
    void dfs(TreeNode* root, vector<string>& res, vector<char>& path) {
        if (!root) {
            res.push_back(string(path.begin(), path.end()));
            return;
        }
        auto n = path.size();
        if (n > 0) {
            path.push_back('-');
            path.push_back('>');
        }
        string val = std::to_string(root->val);
        for (char c: val)
            path.push_back(c);
        if (!root->left && !root->right) {
            // 叶结点，只递归一次，如果递归两次，就会重复添加相同的路径。
            dfs(root->left, res, path);
        } else {
            if (root->left) dfs(root->left, res, path);
            if (root->right) dfs(root->right, res, path);
        }
        path.resize(n); // resize()只在超过capacity时才会重新分配内存，这里也可以用earse(path.begin()+n, path.end())。
    }
};
```

