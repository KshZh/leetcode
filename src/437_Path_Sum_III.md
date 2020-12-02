# 437. Path Sum III

> You are given a binary tree in which each node contains an integer value.
>
> Find the number of paths that sum to a given value.
>
> The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
>
> The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
>
> **Example:**
>
> ```
> root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
> 
>       10
>      /  \
>     5   -3
>    / \    \
>   3   2   11
>  / \   \
> 3  -2   1
> 
> Return 3. The paths that sum to 8 are:
> 
> 1.  5 -> 3
> 2.  5 -> 2 -> 1
> 3. -3 -> 11
> ```

1. Easy。

```cpp
class Solution {
public:
    int pathSum(TreeNode* root, int sum) {
        if (!root) return 0;
        return dfs(root, sum)+pathSum(root->left, sum)+pathSum(root->right, sum);
    }
    
    int dfs(TreeNode* root, int sum) {
        if (!root) return 0;
        // if (sum == 0) return 1; // XXX 到达空树再返回，如果一个上一个结点是叶子，可能调用两次，返回两个1，导致加多了。
        sum -= root->val;
        // if (sum == 0) return 1; // 还不能返回，可能往下继续扩展这条路径又能再次得到`sum==0`，这也算一条使得`sum==0`的不同的路径。
        return (sum==0)+dfs(root->left, sum)+dfs(root->right, sum);
    }
};
```

```cpp
// 时空为O(N)的解法。
// 是[560. Subarray Sum Equals K](./src/560_Subarray_Sum_Equals_K.md)的多路径版本。
class Solution {
    unordered_map<int, int> prefixSum{{0, 1}};
public:
    int pathSum(TreeNode* root, int sum) {
        if (!root) return 0;
        return dfs(root, 0, sum);
    }
    
    int dfs(TreeNode* root, int currSum, int target) {
        if (!root) return 0;
        currSum += root->val;
        int cnt = 0;
        if (prefixSum.find(currSum-target) != prefixSum.end()) {
            cnt = prefixSum[currSum-target];
        }
        prefixSum[currSum]++;
        cnt += dfs(root->left, currSum, target) + dfs(root->right, currSum, target);
        prefixSum[currSum]--; // XXX 从该结点返回了，所以currSum的出现次数减一。
        return cnt;
    }
};
```

