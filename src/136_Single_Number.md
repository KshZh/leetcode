# 136. Single Number

> Given a **non-empty** array of integers, every element appears *twice* except for one. Find that single one.
>
> **Note:**
>
> Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
>
> **Example 1:**
>
> ```
> Input: [2,2,1]
> Output: 1
> ```
>
> **Example 2:**
>
> ```
> Input: [4,1,2,1,2]
> Output: 4
> ```

1. Easy。

```cpp
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        unordered_map<int, int> cnt;
        for (int num: nums)
            cnt[num]++;
        for (auto it=cnt.begin(); it!=cnt.end(); it++) {
            if (it->second == 1)
                return it->first;
        }
        return -1;
    }
};
```

```cpp
// 1^0=1，保持原样。
// a^a=0，因为除了一个，其他都成对出现，所以最后只剩下那个单独出现的元素。
class Solution {
public:
    int singleNumber(vector<int>& nums) {
        int x = 0;
        for (int num: nums)
            x ^= num;
        return x;
    }
};
```

