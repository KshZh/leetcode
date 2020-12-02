# 109. Convert Sorted List to Binary Search Tree

> Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
>
> For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of *every* node never differ by more than 1.
>
> **Example:**
>
> ```
> Given the sorted linked list: [-10,-3,0,5,9],
> 
> One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
> 
>       0
>      / \
>    -3   9
>    /   /
>  -10  5
> ```

1. Medium。

```cpp
// 超时。
class Solution {
    // 插入root的右子树的右边导致不平衡。
    TreeNode* RR(TreeNode* root) {
        TreeNode* newRoot = root->right;
        root->right = newRoot->left;
        newRoot->left = root;
        return newRoot;
    }
    
    // 插入root的左子树的左边导致不平衡。
    TreeNode* LL(TreeNode* root) {
        TreeNode* newRoot = root->left;
        root->left = newRoot->right;
        newRoot->right = root;
        return newRoot;
    }
    
    // 插入root的左子树的右边导致不平衡。
    TreeNode* LR(TreeNode* root) {
        root->left = RR(root->left);
        return LL(root);
    }
    
    TreeNode* RL(TreeNode* root) {
        root->right = LL(root->right);
        return RR(root);
    }
    
    int height(TreeNode* root) {
        if (!root) return 0;
        return 1 + max(height(root->left), height(root->right));
    }
    
    TreeNode* insert(TreeNode* root, int x) {
        if (!root) {
            return new TreeNode(x);
        }
        if (x < root->val) {
            // 注意这里别忘了接收返回值更新root->left，说不定插入后调整平衡后，左子树的根变了呢。
            // 这时就需要重新连起来。
            root->left = insert(root->left, x);
            if (height(root->left) > height(root->right)+1) {
                // 不平衡。
                root = x<root->left->val? LL(root): LR(root);
            }
        } else {
            root->right = insert(root->right, x);
            if (height(root->right) > height(root->left)+1) {
                root = x>root->right->val? RR(root): RL(root);
            }
        }
        return root;
    }
public:
    TreeNode* sortedListToBST(ListNode* head) {
        TreeNode* root = nullptr;
        while (head) {
            root = insert(root, head->val);
            head = head->next;
        }
        return root;
    }
};
```

```cpp
class Solution {
public:
    TreeNode* sortedListToBST(ListNode* head) {
        return toBST(head, nullptr);
    }
    
    TreeNode* toBST(ListNode* head, ListNode* tail) {
        if (head == tail) return nullptr;
        ListNode *slow=head, *fast=head;
        while (fast!=tail && fast->next!=tail) {
            fast = fast->next->next;
            slow = slow->next;
        }
        TreeNode* root = new TreeNode(slow->val);
        root->left = toBST(head, slow);
        root->right = toBST(slow->next, tail);
        return root;
    }
};
```

