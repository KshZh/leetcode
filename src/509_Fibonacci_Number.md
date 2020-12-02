# 509. Fibonacci Number

> The **Fibonacci numbers**, commonly denoted `F(n)` form a sequence, called the **Fibonacci sequence**, such that each number is the sum of the two preceding ones, starting from `0` and `1`. That is,
>
> ```
> F(0) = 0,   F(1) = 1
> F(N) = F(N - 1) + F(N - 2), for N > 1.
> ```
>
> Given `N`, calculate `F(N)`.
>
> **Example 1:**
>
> ```
> Input: 2
> Output: 1
> Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
> ```
>
> **Example 2:**
>
> ```
> Input: 3
> Output: 2
> Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
> ```
>
> **Example 3:**
>
> ```
> Input: 4
> Output: 3
> Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
> ```
>
> **Note:**
>
> 0 ≤ `N` ≤ 30.

1. Easy。

```cpp
class Solution {
public:
    int fib(int N) {
        if (N <= 1) return N; // 递归边界记得写。
        return fib(N-1)+fib(N-2);
    }
};
```

```cpp
// 记忆化搜索，还是超时。
class Solution {
    unordered_map<int, int> cache;
public:
    int fib(int N) {
        if (N <= 1) return N; // 递归边界记得写。
        if (cache.find(N) != cache.end()) return cache[N];
        int x = fib(N-1)+fib(N-2);
        cache[N] = x;
        return x;
    }
};
```

```cpp
// dp[i]只有前两个dp确定，所以可以用两个变量，避免用数组，使得空间复杂度为O(1)。
class Solution {
public:
    int fib(int N) {
        if (N <= 1) return N;
        int a=0, b=1, temp;
        for (int i=2; i<=N; i++) {
            temp = a+b;
            a = b;
            b = temp;
        }
        return b;
    }
};
```

