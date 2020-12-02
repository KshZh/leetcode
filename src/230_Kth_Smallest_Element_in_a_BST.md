# 230. Kth Smallest Element in a BST

> Given a binary search tree, write a function `kthSmallest` to find the **k**th smallest element in it.
>
> **Note:**
> You may assume k is always valid, 1 ≤ k ≤ BST's total elements.
>
> **Example 1:**
>
> ```
> Input: root = [3,1,4,null,2], k = 1
>    3
>   / \
>  1   4
>   \
>    2
> Output: 1
> ```
>
> **Example 2:**
>
> ```
> Input: root = [5,3,6,2,4,null,null,1], k = 3
>        5
>       / \
>      3   6
>     / \
>    2   4
>   /
>  1
> Output: 3
> ```
>
> **Follow up:**
> What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

1. Medium。

> **Complexity Analysis**
>
> - Time complexity : O(*H*+*k*), where *H* is a tree height. This complexity is defined by the stack, which contains at least *H*+*k* elements, since before starting to pop out one has to go down to a leaf. This results in O(log*N*+*k*) for the balanced tree and O(*N*+*k*) for completely unbalanced tree with all the nodes in the left subtree.
> - Space complexity : O(*H*+*k*), the same as for time complexity, O(*N*+*k*) in the worst case, and O(log*N*+*k*) in the average case.

> #### Follow up
>
> > What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?
>
> [Insert](https://leetcode.com/articles/insert-into-a-bst/) and [delete](https://leetcode.com/articles/delete-node-in-a-bst/) in a BST were discussed last week, the time complexity of these operations is O(*H*), where *H* is a height of binary tree, and *H*=log*N* for the balanced tree.
>
> Hence without any optimisation insert/delete + search of kth element has O(2*H*+*k*) complexity. How to optimise that?
>
> That's a design question, basically we're asked to implement a structure which contains a BST inside and optimises the following operations :
>
> - Insert
> - Delete
> - Find kth smallest
>
> Seems like a database description, isn't it? Let's use here the same logic as for [LRU cache](https://leetcode.com/articles/lru-cache/) design, and combine an indexing structure (we could keep BST here) with a double linked list.
>
> Such a structure would provide:
>
> - O(*H*) time for the insert and delete.
> - O(*k*) for the search of kth smallest.
>
> ![bla](https://leetcode.com/problems/kth-smallest-element-in-a-bst/Figures/230/linked_list2.png)
>
> The overall time complexity for insert/delete + search of kth smallest is O(*H*+*k*) instead of O(2*H*+*k*).
>
> **Complexity Analysis**
>
> - Time complexity for insert/delete + search of kth smallest: O(*H*+*k*), where *H* is a tree height. O(log*N*+*k*) in the average case, O(*N*+*k*) in the worst case.
> - Space complexity : O(*N*) to keep the linked list.

```cpp
// 递归版先序遍历。这个问题用迭代好一点。
class Solution {
public:
    int kthSmallest(TreeNode* root, int k) {
        stack<TreeNode*> s;
        TreeNode* p = root;
        while (!s.empty() || p) {
            while (p) {
                s.push(p);
                p = p->left;
            }
            p = s.top();
            s.pop();
            if (--k == 0) return p->val;
            // 加了这个判断反而会错，如果p->right为空的话，那么p又不为nullptr，
            // 那么下次循环p又会入栈，这是错误的。
            // if (p->right)
            p = p->right;
        }
        return -1;
    }
};
```

