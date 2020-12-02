# 173. Binary Search Tree Iterator

> Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.
>
> Calling `next()` will return the next smallest number in the BST.
>
> **Example:**
>
> **![img](https://assets.leetcode.com/uploads/2018/12/25/bst-tree.png)**
>
> ```
> BSTIterator iterator = new BSTIterator(root);
> iterator.next();    // return 3
> iterator.next();    // return 7
> iterator.hasNext(); // return true
> iterator.next();    // return 9
> iterator.hasNext(); // return true
> iterator.next();    // return 15
> iterator.hasNext(); // return true
> iterator.next();    // return 20
> iterator.hasNext(); // return false
> ```
>
> **Note:**
>
> - `next()` and `hasNext()` should run in average O(1) time and uses O(*h*) memory, where *h* is the height of the tree.
> - You may assume that `next()` call will always be valid, that is, there will be at least a next smallest number in the BST when `next()` is called.

1. Medium。

```cpp
// 按需计算。
// 在单链表的情况下，next()最坏需要O(N)，平均应该可以是O(1)。
// 但空间复杂度为O(1)。
class BSTIterator {
    TreeNode* curr;
public:
    BSTIterator(TreeNode* root) {
        curr = root;
    }
    
    /** @return the next smallest number */
    int next() {
        // Morris算法。
        int ret;
        TreeNode* prev;
        while (curr) {
            if (curr->left == nullptr) { // 没有左子树，在中序遍历中，就轮到访问当前结点/根了。
                ret = curr->val;
                curr = curr->right;
                return ret;
            }
            // 找到当前结点在中序遍历中的前驱结点，即左子树的最右下角的结点。
            prev = curr->left;
            while (prev->right && prev->right!=curr)
                prev = prev->right;
            if (prev->right == nullptr) { // 左子树还未访问，所以需要先访问左子树。
                prev->right = curr;
                curr = curr->left;
            } else {
                prev->right = nullptr; // 左子树已经访问过了，所以轮到访问当前结点/根了。
                ret = curr->val;
                curr = curr->right;
                return ret;
            }
        }
        return -1;
    }
    
    /** @return whether we have a next smallest number */
    bool hasNext() {
        return curr!=nullptr;
    }
};
```

```java
// 一次性计算出来，符合题目的时间和空间复杂度要求。
class BSTIterator {

    ArrayList<Integer> nodesSorted;
    int index;

    public BSTIterator(TreeNode root) {

        // Array containing all the nodes in the sorted order
        this.nodesSorted = new ArrayList<Integer>();
        
        // Pointer to the next smallest element in the BST
        this.index = -1;
        
        // Call to flatten the input binary search tree
        this._inorder(root);
    }

    private void _inorder(TreeNode root) {

        if (root == null) {
            return;
        }

        this._inorder(root.left);
        this.nodesSorted.add(root.val);
        this._inorder(root.right);
    }

    /**
     * @return the next smallest number
     */
    public int next() {
        return this.nodesSorted.get(++this.index);
    }

    /**
     * @return whether we have a next smallest number
     */
    public boolean hasNext() {
        return this.index + 1 < this.nodesSorted.size();
    }
}
```

