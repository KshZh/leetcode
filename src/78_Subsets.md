# 78. Subsets

> Given a set of **distinct** integers, *nums*, return all possible subsets (the power set).
>
> **Note:** The solution set must not contain duplicate subsets.
>
> **Example:**
>
> ```
> Input: nums = [1,2,3]
> Output:
> [
>   [3],
>   [1],
>   [2],
>   [1,2,3],
>   [1,3],
>   [2,3],
>   [1,2],
>   []
> ]
> ```

1. Medium。

> First, their solution space is often quite large:
>
> - [Permutations](https://en.wikipedia.org/wiki/Permutation#k-permutations_of_n): N!.
> - [Combinations](https://en.wikipedia.org/wiki/Combination#Number_of_k-combinations): C_N^k = *N*!/(*N*−*k*)!*k*!
> - Subsets: 2^N, since each element could be absent or present.

#### Approach 3: Lexicographic (Binary Sorted) Subsets

> The idea is that we map each subset to a bitmask of length n, where `1` on the i*th* position in bitmask means the presence of `nums[i]` in the subset, and `0` means its absence.

![diff](https://leetcode.com/problems/subsets/Figures/78/bitmask4.png)

```cpp
// Time complexity: O(N×2^N) to generate all subsets and then copy them into output list.
// Space complexity: O(2^N). This is exactly the number of solutions for subsets.
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> ans(1); // 子集集合中总有一个空集。
        for (int num: nums) {
            vector<vector<int>> newSubset;
            for (auto& v: ans) {
                newSubset.push_back(vector<int>(v));
                newSubset.back().push_back(num);
            }
            for (auto& v: newSubset) {
                ans.push_back(move(v));
            }
        }
        return ans;
    }
};
```

```cpp
// 回溯。
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> ans;
        vector<int> path;
        backtrack(0, nums, path, ans);
        return ans;
    }
    
    void backtrack(int i, vector<int>& nums, vector<int>& path, vector<vector<int>>& ans) {
        if (i == nums.size()) {
            ans.push_back(path);
            return;
        }
        // 选。
        path.push_back(nums[i]);
        backtrack(i+1, nums, path, ans);
        path.pop_back();
        
        // 不选。
        backtrack(i+1, nums, path, ans);
    }
};
```

```cpp
// 回溯。
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> ans;
        vector<int> path;
        for (int len=0; len<=nums.size(); len++) {
            backtrack(0, len, nums, path, ans);
        }
        return ans;
    }
    
    void backtrack(int i, int len, vector<int>& nums, vector<int>& path, vector<vector<int>>& ans) {
        if (i == len) {
            ans.push_back(path);
            return;
        }
        // 在迭代的过程中，隐含了选和不选。
        for (; i<nums.size(); i++) {
            path.push_back(nums[i]);
            backtrack(i+1, len, nums, path, ans);
            path.pop_back();
        }
    }
};
```

```cpp
class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        vector<vector<int>> ans;
        auto n = nums.size();
        unsigned end = 1<<n;
        unsigned temp, j;
        for (unsigned i=0; i<end; i++) {
            vector<int> curr;
            for (temp=i, j=0; j<n; j++) {
                if (temp&1) curr.push_back(nums[j]);
                temp >>= 1;
            }
            ans.push_back(move(curr));
        }
        return ans;
    }
};
```

