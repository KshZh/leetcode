# 515. Find Largest Value in Each Tree Row

> You need to find the largest value in each row of a binary tree.
>
> **Example:**
>
> ```
> Input: 
> 
>           1
>          / \
>         3   2
>        / \   \  
>       5   3   9 
> 
> Output: [1, 3, 9]
> ```

1. Medium。

```cpp
vector<int> largestValues(TreeNode* root) {
    if (!root) return {};
    vector<int> ans;
    queue<TreeNode*> q;
    q.push(root);
    TreeNode* x;
    while (!q.empty()) {
        auto n = q.size();
        int max = INT_MIN;
        for (int i=0; i<n; i++) {
            x = q.front();
            q.pop();
            if (x->val > max)
                max = x->val;
            if (x->left) q.push(x->left);
            if (x->right) q.push(x->right);
        }
        ans.push_back(max);
    }
    return ans;
}
```

```python
def findValueMostElement(self, root):
    maxes = []
    row = [root]
    while any(row):
        maxes.append(max(node.val for node in row))
        row = [kid for node in row for kid in (node.left, node.right) if kid]
    return maxes
```

> @lee215 I'll try to explain this part. Please tell me if I'm wrong.
>
> ```python
> row = [kid for node in row for kid in (node.left, node.right) if kid]
> ```
>
> is equal to:
>
> ```python
> row = [a,b,c,d...]
> xxx = []
> for node in row:
>     for kid in (node.left, node.right):
>         if kid:
>             xxx += kid,
> row = xxx
> ```

