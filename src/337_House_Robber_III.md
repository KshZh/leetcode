# 337. House Robber III

> The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.
>
> Determine the maximum amount of money the thief can rob tonight without alerting the police.
>
> **Example 1:**
>
> ```
> Input: [3,2,3,null,3,null,1]
> 
>      3
>     / \
>    2   3
>     \   \ 
>      3   1
> 
> Output: 7 
> Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
> ```
>
> **Example 2:**
>
> ```
> Input: [3,4,5,1,3,null,1]
> 
>      3
>     / \
>    4   5
>   / \   \ 
>  1   3   1
> 
> Output: 9
> Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.
> ```

1. Medium。

```cpp
// https://leetcode.com/problems/house-robber-iii/discuss/79330/Step-by-step-tackling-of-the-problem
// 记忆化搜索。
class Solution {
    unordered_map<TreeNode*, int> cache;
public:
    // rob输入一棵树，输出从这棵树中可以偷得的最大金额。
    int rob(TreeNode* root) {
        if (!root) return 0; // 边界，空树，可以偷的钱为0。
        if (cache.find(root) != cache.end()) return cache[root];
        int val = root->val;
        if (root->left) val+=rob(root->left->left)+rob(root->left->right);
        if (root->right) val+=rob(root->right->left)+rob(root->right->right);
        cache[root] = max(val, rob(root->left)+rob(root->right));
        return cache[root];
    }
};
```

```java
// Now let's take one step back and ask why we have overlapping subproblems. If you trace all the way back to the beginning, you'll find the answer lies in the way how we have defined rob(root). As I mentioned, for each tree root, there are two scenarios: it is robbed or is not. rob(root) does not distinguish between these two cases, so "information is lost as the recursion goes deeper and deeper", which results in repeated subproblems.
// If we were able to maintain the information about the two scenarios for each tree root, let's see how it plays out. Redefine rob(root) as a new function which will return an array of two elements, the first element of which denotes the maximum amount of money that can be robbed if root is not robbed, while the second element signifies the maximum amount of money robbed if it is robbed.
public int rob(TreeNode root) {
    int[] res = robSub(root);
    return Math.max(res[0], res[1]);
}

private int[] robSub(TreeNode root) {
    if (root == null) return new int[2];
    
    int[] left = robSub(root.left);
    int[] right = robSub(root.right);
    int[] res = new int[2];

    res[0] = Math.max(left[0], left[1]) + Math.max(right[0], right[1]);
    res[1] = root.val + left[0] + right[0];
    
    return res;
}
```

