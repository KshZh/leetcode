# 303. Range Sum Query - Immutable

> Given an integer array *nums*, find the sum of the elements between indices *i* and *j* (*i* ≤ *j*), inclusive.
>
> **Example:**
>
> ```
> Given nums = [-2, 0, 3, -5, 2, -1]
> 
> sumRange(0, 2) -> 1
> sumRange(2, 5) -> -1
> sumRange(0, 5) -> -3
> ```

1. Easy，有前缀和数组s，可以在O(1)内求出区间和。

```cpp
class NumArray {
    vector<int> s;
public:
    NumArray(vector<int>& nums) {
        int sum = 0;
        s.resize(nums.size());
        for (int i=0; i<nums.size(); i++) {
            sum += nums[i];
            s[i] = sum;
        }
    }
    
    int sumRange(int i, int j) {
        if (i == 0) // 为了不特殊处理这个边界情况，可以s[i]存储a[0, i-1]的和，i从1开始。
            return s[j];
        return s[j]-s[i-1];
    }
};

/**
 * Your NumArray object will be instantiated and called as such:
 * NumArray* obj = new NumArray(nums);
 * int param_1 = obj->sumRange(i,j);
 */
```

