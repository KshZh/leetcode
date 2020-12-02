# 454. 4Sum II

> Given four lists A, B, C, D of integer values, compute how many tuples `(i, j, k, l)` there are such that `A[i] + B[j] + C[k] + D[l]` is zero.
>
> To make problem a bit easier, all A, B, C, D have same length of N where 0 ≤ N ≤ 500. All integers are in the range of -228 to 228 - 1 and the result is guaranteed to be at most 231 - 1.
>
> **Example:**
>
> ```
> Input:
> A = [ 1, 2]
> B = [-2,-1]
> C = [-1, 2]
> D = [ 0, 2]
> 
> Output:
> 2
> 
> Explanation:
> The two tuples are:
> 1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
> 2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
> ```

1. Medium。

```cpp
// 时间和空间复杂度都为O(N^2)。
// 不是写成四层循环，降低了时间复杂度。
class Solution {
public:
    int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D) {
        int res = 0;
        unordered_map<int, int> AB;
        for (int a : A)
            for (int b : B)
                AB[a + b]++;
        for (int c : C)
            for (int d : D)
                // 不用先查找元素是否存在哈希表中，利用unordered_map不存在即创建的性质且pair的value值初始化为0。
                res += AB[-c - d];
        return res;
    }
};
```

