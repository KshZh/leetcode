# 501. Find Mode in Binary Search Tree

> Given a binary search tree (BST) with duplicates, find all the [mode(s)](https://en.wikipedia.org/wiki/Mode_(statistics)) (the most frequently occurred element) in the given BST.
>
> Assume a BST is defined as follows:
>
> - The left subtree of a node contains only nodes with keys **less than or equal to** the node's key.
> - The right subtree of a node contains only nodes with keys **greater than or equal to** the node's key.
> - Both the left and right subtrees must also be binary search trees.
>
> For example:
> Given BST `[1,null,2,2]`,
>
> ```
>    1
>     \
>      2
>     /
>    2
> ```
>
> return `[2]`.
>
> **Note:** If a tree has more than one mode, you can return them in any order.
>
> **Follow up:** Could you do that without using any extra space? (Assume that the implicit stack space incurred due to recursion does not count).

1. Easy。

```cpp
// 多次dfs，第一次先获取最大的出现频率，第二次将出现频率等于该最大频率的结点放入容器中。
// 因为是BST，所以相同的结点只能是该结点的左子结点或右子结点，然后递归计数。
// 也可以用哈希表计数，然后记住遇到过的最大频率，然后将哈希表中符合最大频率的元素放入容器中。
// 也可以用自定义排序的红黑树，在遍历过程中即维持有序。
class Solution {
public:
    int maxCount = INT_MIN;
    int currCount = 0;
    TreeNode* prev = NULL;
    vector<int> ans;
    
    void inorder(TreeNode* root, bool getlist){
        if(!root) return;
        
        inorder(root->left, getlist);
        
        if(prev && prev->val==root->val)
            currCount++;
        else
            currCount=1;
        if(!getlist) maxCount = max(maxCount, currCount);
        else if(currCount==maxCount) ans.push_back(root->val);
        prev = root;
        inorder(root->right, getlist);
    }
    
    vector<int> findMode(TreeNode* root) {
        ans.clear();
        if(!root) return ans;
        
        // Get the maxCount size
        inorder(root, false);
        
        // Get the final list
        prev = NULL;
        currCount = 0;
        inorder(root, true);
        
        return ans;
    }
};
```

