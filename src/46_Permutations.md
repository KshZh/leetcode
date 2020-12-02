# 46. Permutations

> Given a collection of **distinct** integers, return all possible permutations.
>
> **Example:**
>
> ```
> Input: [1,2,3]
> Output:
> [
>   [1,2,3],
>   [1,3,2],
>   [2,1,3],
>   [2,3,1],
>   [3,1,2],
>   [3,2,1]
> ]
> ```

1. Medium，回溯。

```cpp
class Solution {
public:
    vector<vector<int>> permute(vector<int>& nums) {
        vector<vector<int>> ans;
        backtracking(0, nums, ans);
        return ans;
    }
    
    // 求A[0, n)的全排列，A[0]有n种可能，然后接上A[1, n)的全排列。
    void permutation(int pos, vector<int>& nums, vector<vector<int>>& ans) {
        if (pos == nums.size()) {
            ans.push_back(nums);
            return;
        }
        for (int i=pos; i<nums.size(); i++) {
            swap(nums[i], nums[pos]);
            permutation(pos+1, nums, ans);
            swap(nums[i], nums[pos]);
        }
    }
};
```



