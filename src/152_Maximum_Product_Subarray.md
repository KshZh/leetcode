# 152. Maximum Product Subarray

> Given an integer array `nums`, find the contiguous subarray within an array (containing at least one number) which has the largest product.
>
> **Example 1:**
>
> ```
> Input: [2,3,-2,4]
> Output: 6
> Explanation: [2,3] has the largest product 6.
> ```
>
> **Example 2:**
>
> ```
> Input: [-2,0,-1]
> Output: 0
> Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
> ```

1. DP，Medium。

2. > multiplied by a negative makes big number smaller, small number bigger so we redefine the extremums by swapping them.

```cpp
// https://leetcode.com/problems/maximum-product-subarray/discuss/183483/In-Python-it-can-be-more-concise-PythonC%2B%2BJava
class Solution {
public:
    int maxProduct(vector<int> A) {
        int n = A.size(), res = A[0], l = 0, r = 0;
        // 两个方向是为了应对一个子序列中的负数个数为奇数个的情况。
        for (int i = 0; i < n; i++) {
            l =  (l ? l : 1) * A[i]; // 0会分隔输入序列，`(l ? l : 1)`的目的是遇到0时，从下一个序列重新开始累积。
            r =  (r ? r : 1) * A[n - 1 - i];
            res = max(res, max(l, r));
        }
        return res;
    }
};
```

```cpp
// https://leetcode.com/problems/maximum-product-subarray/discuss/48230/Possibly-simplest-solution-with-O(n)-time-complexity
int maxProduct(int A[], int n) {
    // store the result that is the max we have found so far
    int r = A[0];

    // imax/imin stores the max/min product of
    // subarray that ends with the current number A[i]
    for (int i = 1, imax = r, imin = r; i < n; i++) {
        // XXX multiplied by a negative makes big number smaller, small number bigger
        // so we redefine the extremums by swapping them
        if (A[i] < 0)
            swap(imax, imin);

        // max/min product for the current number is either the current number itself
        // or the max/min by the previous number times the current one
        imax = max(A[i], imax * A[i]);
        imin = min(A[i], imin * A[i]);

        // the newly computed max value is a candidate for our global result
        r = max(r, imax);
    }
    return r;
}
```

