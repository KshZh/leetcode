# 220. Contains Duplicate III

> Given an array of integers, find out whether there are two distinct indices *i* and *j* in the array such that the **absolute** difference between **nums[i]** and **nums[j]** is at most *t* and the **absolute** difference between *i* and *j* is at most *k*.
>
> **Example 1:**
>
> ```
> Input: nums = [1,2,3,1], k = 3, t = 0
> Output: true
> ```
>
> **Example 2:**
>
> ```
> Input: nums = [1,0,1,1], k = 1, t = 2
> Output: true
> ```
>
> **Example 3:**
>
> ```
> Input: nums = [1,5,9,1,5,9], k = 2, t = 3
> Output: false
> ```

1. Medium。
2. 采用和[219. Contains Duplicate II](./219_Contains_Duplicate_II.md)同样的思路，也就是滑动窗口，但是这里元素之间可以相差一个常数t，大佬的做法是把每个元素映射到一个个大小为`t+1`的桶中，如果两个元素映射到同一个桶，那么说明这两个元素相差小于等于t。当然，如果在相邻的桶中，也可能相差小于等于t。

```cpp
class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
        if (k<1 || t<0 || nums.size()<2) return false;
        unordered_map<long, long> buckets;
        long bucket;
        for (int i=0; i<nums.size(); i++) {
            // -INT_MIN是为了把所有负数映射到正数来处理。
            if (i > k) buckets.erase((static_cast<long>(nums[i-(k+1)])-INT_MIN)/(static_cast<long>(t)+1));
            bucket = (static_cast<long>(nums[i])-INT_MIN)/(static_cast<long>(t)+1);
            if (buckets.find(bucket)!=buckets.end()
                || (buckets.find(bucket-1)!=buckets.end() && nums[i]-buckets[bucket-1]<=t)
                || (buckets.find(bucket+1)!=buckets.end() && buckets[bucket+1]-nums[i]<=t))
                return true;
            buckets[bucket] = nums[i];
        }
        return false;
    }
};
```

```cpp
// 使用红黑树/平衡bst，查找范围，O(logK)，因为窗口大小为K，所以树大小为K。
// 时间复杂度是O(NlogK)。
class Solution {
public:
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
        if (k<1 || t<0 || nums.size()<2) return false;
        set<long> s;
        set<long>::iterator it;
        for (int i=0; i<nums.size(); i++) {
            if (i > k) s.erase(nums[i-(k+1)]); // 移动左端点。
            // it = s.lower_bound(nums[i]);
            // if (it!=s.end() && *it-nums[i]<=t) return true;
            it = s.lower_bound(static_cast<long>(nums[i])-t);
            if (it!=s.end() && abs(static_cast<long>(nums[i])-*it)<=t) return true;
            s.insert(nums[i]);
        }
        return false;
    }
};
// 给出一个中点x，查看set中是否有一个元素在[x-t, x+t]的范围内，只需一次O(logN)查找即可。
```

