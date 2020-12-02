# 40. Combination Sum II

> Given a collection of candidate numbers (`candidates`) and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sums to `target`.
>
> Each number in `candidates` may only be used **once** in the combination.
>
> **Note:**
>
> - All numbers (including `target`) will be positive integers.
> - The solution set must not contain duplicate combinations.
>
> **Example 1:**
>
> ```
> Input: candidates = [10,1,2,7,6,1,5], target = 8,
> A solution set is:
> [
>   [1, 7],
>   [1, 2, 5],
>   [2, 6],
>   [1, 1, 6]
> ]
> ```
>
> **Example 2:**
>
> ```
> Input: candidates = [2,5,2,1,2], target = 5,
> A solution set is:
> [
>   [1,2,2],
>   [5]
> ]
> ```

1. Medium，回溯。
2. TODO：时间复杂度不清楚。

```cpp
// 时间复杂度是O(n^m)，其中n是candidates.size()，m是结果中最长的那个组合的长度。因为每个槽有最多n种选择？
// 另一种说法是O(2^n)，因为可选可不选？
class Solution {
    vector<vector<int>> res;
public:
    vector<vector<int>> combinationSum2(vector<int>& candidates, int target) {
        sort(candidates.begin(), candidates.end()); // 为了让重复元素聚在一起。
        vector<int> path;
        dfs(candidates, target, path, 0);
        return res;
    }
    
    // 在每一个槽上，选择candidates[i,]中的元素填入其中。
    void dfs(vector<int>& candidates, int target, vector<int>& path, int i) {
        if (target < 0) return;
        if (target == 0) {
            res.push_back(path);
            return;
        }
        for (int j=i; j<candidates.size(); j++) {
            if (j>i && candidates[j]==candidates[j-1]) // 重复元素只用一次，也就是不能在当前的空位上多次填同一个值相等的元素，这样可以避免产生两个[1, 7]的情况，对于[10, 1, 2, 7, 6, 1, 5]这样的输入。
                continue;
            path.push_back(candidates[j]);
            dfs(candidates, target-candidates[j], path, j+1);
            path.pop_back();
        }
    }
};
```

