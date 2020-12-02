#  508. Most Frequent Subtree Sum

> Given the root of a tree, you are asked to find the most frequent subtree sum. The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node (including the node itself). So what is the most frequent subtree sum value? If there is a tie, return all the values with the highest frequency in any order.
>
> **Examples 1**
> Input:
>
> ```
>   5
>  /  \
> 2   -3
> ```
>
> return [2, -3, 4], since all the values happen only once, return all of them in any order.
>
> **Examples 2**
> Input:
>
> ```
>   5
>  /  \
> 2   -5
> ```
>
> return [2], since 2 happens twice, however -5 only occur once.
>
> **Note:** You may assume the sum of values in any subtree is in the range of 32-bit signed integer.

1. Medium。

```cpp
class Solution {
    unordered_map<int, int> frequency;
    int max = INT_MIN;
public:
    vector<int> findFrequentTreeSum(TreeNode* root) {
        if (!root) return {};
        sum(root);
        vector<int> ans;
        for (auto& p: frequency) {
            if (p.second == max)
                ans.push_back(p.first);
        }
        return ans;
    }
    
    int sum(TreeNode* root) {
        if (!root) return 0;
        int x = root->val+sum(root->left)+sum(root->right);
        frequency[x]++;
        // 在遍历的过程中维护一个最大的频率，这样就不需要对哈希表排序(O(NlogN))了。
        if (frequency[x] > max) max = frequency[x];
        return x;
    }
};
```

