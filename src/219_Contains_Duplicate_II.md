# 219. Contains Duplicate II

> Given an array of integers and an integer *k*, find out whether there are two distinct indices *i* and *j* in the array such that **nums[i] = nums[j]** and the **absolute** difference between *i* and *j* is at most *k*.
>
> **Example 1:**
>
> ```
> Input: nums = [1,2,3,1], k = 3
> Output: true
> ```
>
> **Example 2:**
>
> ```
> Input: nums = [1,0,1,1], k = 1
> Output: true
> ```
>
> **Example 3:**
>
> ```
> Input: nums = [1,2,3,1,2,3], k = 2
> Output: false
> ```

1. Easy。

```cpp
// 查重可考虑哈希表。
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        if (nums.empty() || k<1) return false;
        unordered_map<int, int> idx;
        for (int i=0; i<nums.size(); i++) {
            if (idx.find(nums[i]) != idx.end()) {
                if (i-idx[nums[i]] <= k)
                    return true;
            }
            idx[nums[i]] = i; // 创建或覆盖。
        }
        return false;
    }
};
```

```cpp
// 滑动窗口视角。
// 因为两个相同元素可以相距最大k，那么需要维护一个大小为k+1的窗口。
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        if (nums.empty() || k<1) return false;
        unordered_set<int> idx;
        for (int i=0; i<nums.size(); i++) {
            if (i > k) idx.erase(nums[i-(k+1)]);
            if (idx.find(nums[i]) != idx.end()) return true;
            idx.insert(nums[i]);
        }
        return false;
    }
};
```

