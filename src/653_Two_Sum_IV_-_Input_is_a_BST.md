# 653. Two Sum IV - Input is a BST

> Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.
>
> **Example 1:**
>
> ```
> Input: 
>     5
>    / \
>   3   6
>  / \   \
> 2   4   7
> 
> Target = 9
> 
> Output: True
> ```
>
> **Example 2:**
>
> ```
> Input: 
>     5
>    / \
>   3   6
>  / \   \
> 2   4   7
> 
> Target = 28
> 
> Output: False
> ```

1. Easy。

```cpp
// 时空均为O(N)。
bool findTarget(TreeNode* root, int k) {
    vector<int> v;
    dfs(root, v);
    // 首尾双指针。
    for (int i=0, j=v.size()-1; i<j; ) {
        if (v[i]+v[j] > k) j--;
        else if (v[i]+v[j] < k) i++;
        else return true;
    }
    return false;
}

// BST的性质，对BST进行中序遍历得到一个有序的上升序列。
void dfs(TreeNode* root, vector<int>& v) {
    if (!root) return;
    dfs(root->left, v);
    v.push_back(root->val);
    dfs(root->right, v);
}
```

```cpp
// 哈希表。
// 时空均为O(N)。
class Solution {
    unordered_set<int> book;
public:
    bool findTarget(TreeNode* root, int k) {
        if (!root) return false;
        if (book.find(k-root->val) != book.end()) return true;
        book.insert(root->val);
        return findTarget(root->left, k) || findTarget(root->right, k);
    }
};
```

