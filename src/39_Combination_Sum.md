# 39. Combination Sum

> Given a **set** of candidate numbers (`candidates`) **(without duplicates)** and a target number (`target`), find all unique combinations in `candidates` where the candidate numbers sums to `target`.
>
> The **same** repeated number may be chosen from `candidates` unlimited number of times.
>
> **Note:**
>
> - All numbers (including `target`) will be positive integers.
> - The solution set must not contain duplicate combinations.
>
> **Example 1:**
>
> ```
> Input: candidates = [2,3,6,7], target = 7,
> A solution set is:
> [
>   [7],
>   [2,2,3]
> ]
> ```
>
> **Example 2:**
>
> ```
> Input: candidates = [2,3,5], target = 8,
> A solution set is:
> [
>   [2,2,2,2],
>   [2,3,3],
>   [3,5]
> ]
> ```

1. Medium，回溯。
2. TODO：时间复杂度不清楚。

```cpp
class Solution {
    vector<vector<int>> res;
public:
    vector<vector<int>> combinationSum(vector<int>& candidates, int target) {
        vector<int> path;
        dfs(candidates, target, path, 0);
        return move(res);
    }
    
    // 在每一个槽上，选择candidates中的元素填入其中。
    // 比如对于[2, 2, 3]，这个dfs产生[2, 2, 3], [2, 3, 2], [3, 2, 2]，下面的dfs产生[2, 2, 3]。
    // 因为增加了一个参数i，限制了后面的递归对一个位置所能选择放置的元素，这样就可以消除[2, 3, 2]和[3, 2, 2]，因为选了3之后，无法选2。
    // void dfs(vector<int>& candidates, int target, vector<int>& path) {
    //     if (target < 0) return;
    //     if (target == 0) {
    //         res.push_back(path);
    //         return;
    //     }
    //     for (int i: candidates) {
    //         path.push_back(i);
    //         dfs(candidates, target-i, path);
    //         path.pop_back();
    //     }
    // }
    
    // 在每一个槽上，选择candidates[i,]中的元素填入其中。
    void dfs(vector<int>& candidates, int target, vector<int>& path, int i) {
        if (target < 0) return;
        if (target == 0) {
            res.push_back(path);
            return;
        }
        for (; i<candidates.size(); i++) {
            path.push_back(candidates[i]);
            dfs(candidates, target-candidates[i], path, i);
            path.pop_back();
        }
    }
};
```

