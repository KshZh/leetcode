# 216. Combination Sum III

> Find all possible combinations of ***k*** numbers that add up to a number ***n***, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
>
> **Note:**
>
> - All numbers will be positive integers.
> - The solution set must not contain duplicate combinations.
>
> **Example 1:**
>
> ```
> Input: k = 3, n = 7
> Output: [[1,2,4]]
> ```
>
> **Example 2:**
>
> ```
> Input: k = 3, n = 9
> Output: [[1,2,6], [1,3,5], [2,3,4]]
> ```

1. Medium，回溯，用哈希表O(1)记住用过的元素。

```cpp
// 时间复杂度是O(9^k)，因为选k个数，每个数有9个选择。
class Solution {
    vector<vector<int>> res;
    bool used[10]{false};
public:
    vector<vector<int>> combinationSum3(int k, int n) {
        vector<int> path;
        dfs(k, n, path, 1);
        return res;
    }
    
    // 遍历每一个slot，在[i, 9]中选择一个没用过数放入槽中。
    // 如果没有i参数，每次从[1, 9]中选一个没用过的数，那么
    // 可能导致[1, 2, 4]和[1, 4, 2]这样重复的集合，有了i参数，
    // 选了4之后就不能选2了，避免出现重复集合。
    void dfs(int k, int n, vector<int>& path, int i) {
        if (k<0 || n<0) return;
        if (k==0 && n==0) { // 不仅仅n减为0就行了，还要凑够元素个数。
            res.push_back(path);
            return;
        }
        for (; i<=9; i++) {
            if (used[i]) continue;
            used[i] = true;
            path.push_back(i);
            dfs(k-1, n-i, path, i);
            path.pop_back();
            used[i] = false;
        }
    }
};
```

```cpp
// 其实不用哈希表。
class Solution {
    vector<vector<int>> res;
public:
    vector<vector<int>> combinationSum3(int k, int n) {
        vector<int> path;
        dfs(k, n, path, 1);
        return res;
    }
    
    // 遍历每一个slot，在[i, 9]中选择一个没用过数放入槽中。
    // 如果没有i参数，每次从[1, 9]中选一个没用过的数，那么
    // 可能导致[1, 2, 4]和[1, 4, 2]这样重复的集合，有了i参数，
    // 选了4之后就不能选2了，避免出现重复集合。
    void dfs(int k, int n, vector<int>& path, int i) {
        if (k<0 || n<0) return;
        if (k==0 && n==0) { // 不仅仅n减为0就行了，还要凑够元素个数。
            res.push_back(path);
            return;
        }
        for (; i<=9; i++) {
            path.push_back(i);
            dfs(k-1, n-i, path, i+1);
            path.pop_back();
        }
    }
};
```

