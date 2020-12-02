# 654. Maximum Binary Tree

> Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:
>
> 1. The root is the maximum number in the array.
> 2. The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
> 3. The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
>
> Construct the maximum tree by the given array and output the root node of this tree.
>
> **Example 1:**
>
> ```
> Input: [3,2,1,6,0,5]
> Output: return the tree root node representing the following tree:
> 
>       6
>     /   \
>    3     5
>     \    / 
>      2  0   
>        \
>         1
> ```
>
> **Note:**
>
> 1. The size of the given array will be in the range [1,1000].

1. Medium。

```java
// 空间复杂度，如果栈空间算的话，就是递归调用的深度，最坏是单链表的树，O(N)。
// 时间复杂度，在每一层调用上，总体上遍历n个元素（具体的话就是n减去上层结点数，不过是大O，所以不需要这么具体），然后如果是单链表的树，有n层，O(N^2)。
public class Solution {
    public TreeNode constructMaximumBinaryTree(int[] nums) {
        return construct(nums, 0, nums.length);
    }
    public TreeNode construct(int[] nums, int l, int r) {
        if (l == r)
            return null;
        int max_i = max(nums, l, r);
        TreeNode root = new TreeNode(nums[max_i]);
        root.left = construct(nums, l, max_i);
        root.right = construct(nums, max_i + 1, r);
        return root;
    }
    public int max(int[] nums, int l, int r) {
        int max_i = l;
        for (int i = l; i < r; i++) {
            if (nums[max_i] < nums[i])
                max_i = i;
        }
        return max_i;
    }
}
```

```cpp
// 时空为O(N)。
// https://leetcode.com/problems/maximum-binary-tree/discuss/106146/C%2B%2B-O(N)-solution
// 在栈中维护一个递减序列，比较tricky，学不来。
TreeNode* constructMaximumBinaryTree(vector<int>& nums) {
    vector<TreeNode*> stk;
    for (int i = 0; i < nums.size(); ++i)
    {
        TreeNode* cur = new TreeNode(nums[i]);
        // 栈中已有的元素中，其中之一为cur的左子树，这个之一就是栈中比cur小的元素中最大的元素（符合题意）。
        while (!stk.empty() && stk.back()->val < nums[i])
        {
            cur->left = stk.back();
            stk.pop_back();
        }
        // cur在nums中的位置上在stk.back()右边，且cur也是目前遇到的在stk.back()右边的比stk.back()小的最大的元素，所以cur可能为stk.back()的右子树，如果后面没有遇到比stk.back()小但比cur大的元素的话，如果有，那么stk.back()的右子树会被更新为那个元素。
        if (!stk.empty())
            stk.back()->right = cur;
        stk.push_back(cur);
    }
    return stk.front();
}
```

