# 217. Contains Duplicate

> Given an array of integers, find if the array contains any duplicates.
>
> Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.
>
> **Example 1:**
>
> ```
> Input: [1,2,3,1]
> Output: true
> ```
>
> **Example 2:**
>
> ```
> Input: [1,2,3,4]
> Output: false
> ```
>
> **Example 3:**
>
> ```
> Input: [1,1,1,3,3,4,3,2,4,2]
> Output: true
> ```

1. Easy。

```java
public boolean containsDuplicate(int[] nums) {
    for (int i = 0; i < nums.length; ++i) {
        for (int j = 0; j < i; ++j) {
            if (nums[j] == nums[i]) return true;  
        }
    }
    return false;
}
// Time Limit Exceeded
```

```cpp
// 考虑排序。
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        if (nums.empty()) return false;
        sort(nums.begin(), nums.end());
        for (int i=0; i<nums.size()-1; i++) {
            if (nums[i] == nums[i+1])
                return true;
        }
        return false;
    }
};
```

```cpp
// 查重可用哈希表。
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        if (nums.empty()) return false;
        unordered_set<int> s;
        for (int i=0; i<nums.size(); i++) {
            if (s.find(nums[i]) != s.end())
                return true;
            s.insert(nums[i]);
        }
        return false;
    }
};
```

