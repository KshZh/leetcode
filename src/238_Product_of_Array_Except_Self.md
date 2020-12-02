# 238. Product of Array Except Self

> Given an array `nums` of *n* integers where *n* > 1,  return an array `output` such that `output[i]` is equal to the product of all the elements of `nums` except `nums[i]`.
>
> **Example:**
>
> ```
> Input:  [1,2,3,4]
> Output: [24,12,8,6]
> ```
>
> **Note:** Please solve it **without division** and in O(*n*).
>
> **Follow up:**
> Could you solve it with constant space complexity? (The output array **does not** count as extra space for the purpose of space complexity analysis.)

1. Medium，前缀积数组。

```cpp
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        auto n = nums.size();
        // pl[i]表示元素i左边的所有元素的乘积，也就是前缀积。
        vector<int> pl(n), pr(n), ans(n);
        for (int i=0, product=1; i<n; i++) {
            pl[i] = product;
            product *= nums[i];
        }
        for (int i=n-1, product=1; i>=0; i--) {
            pr[i] = product;
            product *= nums[i];
        }
        for (int i=0; i<n; i++) {
            ans[i] = pl[i]*pr[i];
        }
        return ans;
    }
};
```

```cpp
// 先构建其中一个前缀积数组，constructing the other one on the fly.
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        auto n = nums.size();
        vector<int> ans(n);
        for (int i=n-1, product=1; i>=0; i--) {
            ans[i] = product;
            product *= nums[i];
        }
        for (int i=0, product=1; i<n; i++) {
            ans[i] = ans[i]*product;
            product *= nums[i];
        }
        return ans;
    }
};
```

