# 116. Populating Next Right Pointers in Each Node

> You are given a **perfect binary tree** where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:
>
> ```
> struct Node {
>   int val;
>   Node *left;
>   Node *right;
>   Node *next;
> }
> ```
>
> Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to `NULL`.
>
> Initially, all next pointers are set to `NULL`.
>
> **Follow up:**
>
> - You may only use constant extra space.
> - Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
>
> **Example 1:**
>
> ![img](https://assets.leetcode.com/uploads/2019/02/14/116_sample.png)
>
> ```
> Input: root = [1,2,3,4,5,6,7]
> Output: [1,#,2,3,#,4,5,6,7,#]
> Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
> ```
>
> **Constraints:**
>
> - The number of nodes in the given tree is less than `4096`.
> - `-1000 <= node.val <= 1000`

1. Medium。

```cpp
// bfs/层序遍历，O(N)空间复杂度。
class Solution {
public:
    Node* connect(Node* root) {
        if (!root) return root;
        queue<Node*> q;
        q.push(root);
        Node* last=root;
        Node* x;
        while (!q.empty()) {
            x = q.front();
            q.pop();
            if (x!=last && !q.empty())
                x->next = q.front();
            // 不要以为是完全二叉树就不用判断左右孩子指针为不为空了，
            // 只是内部结点一定有两个孩子，但叶子结点没有孩子。
            if (x->left) q.push(x->left);
            if (x->right) q.push(x->right);
            if (x == last) {
                if (!q.empty()) last = q.back();
            }
        }
        return root;
    }
};
```

```cpp
// O(1)空间复杂度，也是层序遍历。
class Solution {
public:
    Node* connect(Node* root) {
        if (!root) return root;
        Node *p=root, *q;
        while (p->left) {
            q = p;
            while (q) {
                q->left->next = q->right;
                if (q->next)
                    q->right->next = q->next->left;
                q = q->next;
            }
            p = p->left;
        }
        return root;
    }
};
```

