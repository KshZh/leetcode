# 572. Subtree of Another Tree

> Given two non-empty binary trees **s** and **t**, check whether tree **t** has exactly the same structure and node values with a subtree of **s**. A subtree of **s** is a tree consists of a node in **s** and all of this node's descendants. The tree **s** could also be considered as a subtree of itself.
>
> **Example 1:**
> Given tree s:
>
> ```
>      3
>     / \
>    4   5
>   / \
>  1   2
> ```
>
> Given tree t:
>
> ```
>    4 
>   / \
>  1   2
> ```
>
> Return **true**, because t has the same structure and node values with a subtree of s.
>
> **Example 2:**
> Given tree s:
>
> ```
>      3
>     / \
>    4   5
>   / \
>  1   2
>     /
>    0
> ```
>
> Given tree t:
>
> ```
>    4
>   / \
>  1   2
> ```
>
> Return **false**.

1. Easy。

```cpp
// 错误的实现，这样一旦第一个结点匹配上，在后面中途miss了，本来应该回到起点尝试s的下一个结点，但这个实现在miss时不会回来。
bool isSubtree(TreeNode* s, TreeNode* t) {
    if (!s && !t) return true;
    if (!s || !t) return false;
    if (s->val == t->val) {
        return isSubtree(s->left, t->left) && isSubtree(s->right, t->right);
    } else {
        return isSubtree(s->left, t->left)||isSubtree(s->right, t->right);
    }
}
```

```cpp
// 时间复杂度O(N*M)，因为最坏情况下，对s的每一个结点，都调用了一次equals()，且在t的最后一个结点才不匹配。
// 空间复杂度O(N)，最坏情况s为单链表，递归深度为O(N)。
bool isSubtree(TreeNode* s, TreeNode* t) {
    // 短路操作，如果有一个为true，后面的递归调用就不会展开。
    return s && t && (equals(s, t) || isSubtree(s->left, t) || isSubtree(s->right, t));
}

bool equals(TreeNode* s, TreeNode* t) {
    if (!s && !t) return true;
    if (!s || !t) return false;
    return s->val==t->val && equals(s->left, t->left) && equals(s->right, t->right);
}
```

```java
// 对树做唯一编码。
// Time complexity : O(m^2+n^2+m*n). A total of nn nodes of the tree ss and mm nodes of tree tt are traversed. Assuming string concatenation takes O(k) time for strings of length kk and indexOf takes O(m*n).
// Space complexity : O(max(m,n))O(max(m,n)). The depth of the recursion tree can go upto nn for tree tt and mm for tree ss in worst case.
Space complexity : O(max(m,n))O(max(m,n)). The depth of the recursion tree can go upto nn for tree tt and mm for tree ss in worst case.
public class Solution {
    HashSet < String > trees = new HashSet < > ();
    public boolean isSubtree(TreeNode s, TreeNode t) {
        String tree1 = preorder(s, true);
        String tree2 = preorder(t, true);
        return tree1.indexOf(tree2) >= 0;
    }
    public String preorder(TreeNode t, boolean left) {
        if (t == null) {
            if (left)
                return "lnull";
            else
                return "rnull";
        }
        return "#"+t.val + " " +preorder(t.left, true)+" " +preorder(t.right, false);
    }
}
```

