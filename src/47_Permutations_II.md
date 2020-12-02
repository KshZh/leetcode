# 47. Permutations II

> Given a collection of numbers that might contain duplicates, return all possible unique permutations.
>
> **Example:**
>
> ```
> Input: [1,1,2]
> Output:
> [
>   [1,1,2],
>   [1,2,1],
>   [2,1,1]
> ]
> ```

1. 先要知道为什么包含重复元素的输入会产生重复的排列，比如[1, **1**, 2]，如果按照46的代码，会产生[1, **1**, 2]和[**1**, 1, 2]，也就是核心是第一个位置不能使用重复元素，它只有两种可能，分别是1和2。那么怎么跳过重复元素呢？可以**对序列排序，使得序列有序**，然后就可以跳过了。注意下面的实现中，nums是传值参数，并且我们没有swap()回来，这是因为要保证第一次swap()之后，子序列也是有序的。如果使用引用参数，并且swap()回来，会导致返回时在当前位置继续选择下一个数的时候子序列不再是有序的，如[(0), 0, (1), 9]，这是返回后swap()回来的情况，然后尝试下一个 可能9，得到[(9), 0, 1, (0)]，可以看到子序列[0, 1, 0]不是有序的，这就导致递归调用无法跳过重复的元素，从而产生重复的排列。
2. 第二份代码参考：https://leetcode-cn.com/problems/permutations-ii/solution/c-jian-dan-hui-su-by-da-li-wang/，关键就是用map来消除重复元素，原本**值相等的不同元素变成了一个带着可用次数属性的元素**。

```cpp
class Solution {
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        vector<vector<int>> res;
        std::sort(nums.begin(), nums.end());
        dfs(0, nums, res);
        return res;
    }

    // 注意nums是传值参数。
    void dfs(int pos, vector<int> nums, vector<vector<int>>& res) {
        if (pos == nums.size()-1) {
            res.push_back(nums);    
            return;
        }
        // [(0), 0, 1, 9]，
        // 尝试第一种可能[(0), 0, 1, 9]，子问题是有序序列[0, 1, 9]的排列；
        // 尝试第二种可能[(1), 0, 0, 9]，子问题是有序序列[0, 0, 9]的排列；
        // 尝试第三种可能[(9), 0, 0, 1]，子问题是有序序列[0, 0, 1]的排列。
        for (int i=pos; i<nums.size(); i++) {
            if (i>pos && nums[i]==nums[pos]) // 跳过重复元素。
                continue;
            std::swap(nums[i], nums[pos]);
            dfs(pos+1, nums, res);
        }
    }
};
```

```cpp
class Solution {
    unordered_map<int, int> m;
    vector<vector<int>> res;
    vector<int> path;
public:
    vector<vector<int>> permuteUnique(vector<int>& nums) {
        for (int x: nums) {
            m[x]++;
        }
        dfs(nums.size());
        return res;
    }

    void dfs(int nLeft) {
        if (nLeft == 0) {
            res.push_back(path);    
            return;
        }
        for (auto& p: m) {
            if (p.second == 0)
                continue;
            p.second--;
            path.push_back(p.first);
            dfs(nLeft-1);
            path.pop_back();
            p.second++;
        }
    }
};
```

