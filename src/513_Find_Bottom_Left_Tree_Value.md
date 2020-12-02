# 513. Find Bottom Left Tree Value

> Given a binary tree, find the leftmost value in the last row of the tree.
>
> **Example 1:**
>
> ```
> Input:
> 
>     2
>    / \
>   1   3
> 
> Output:
> 1
> ```
>
> **Example 2:**
>
> ```
> Input:
> 
>         1
>        / \
>       2   3
>      /   / \
>     4   5   6
>        /
>       7
> 
> Output:
> 7
> ```
>
> **Note:** You may assume the tree (i.e., the given root node) is not **NULL**.

1. Medium。

```cpp
int findBottomLeftValue(TreeNode* root) {
    if (!root) return -1;
    queue<TreeNode*> q;
    q.push(root);
    int firstOfRow;
    TreeNode* x;
    while (!q.empty()) {
        auto n = q.size();
        firstOfRow = q.front()->val;
        for (int i=0; i<n; i++) {
            x = q.front();
            q.pop();
            if (x->left) q.push(x->left);
            if (x->right) q.push(x->right);
        }
    }
    return firstOfRow;
}
```

```java
// Right-to-Left BFS.
public int findLeftMostNode(TreeNode root) {
    Queue<TreeNode> queue = new LinkedList<>();
    queue.add(root);
    while (!queue.isEmpty()) {
        root = queue.poll();
        if (root.right != null)
            queue.add(root.right);
        if (root.left != null)
            queue.add(root.left);
    }
    return root.val;
}
```

```python
# Right-to-Left BFS.
def findLeftMostNode(self, root):
    queue = [root]
    for node in queue:
        queue += filter(None, (node.right, node.left))
    return node.val
```

