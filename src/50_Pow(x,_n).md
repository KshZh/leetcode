# 50. Pow(x, n)

> Implement [pow(*x*, *n*)](http://www.cplusplus.com/reference/valarray/pow/), which calculates *x* raised to the power *n* (xn).
>
> **Example 1:**
>
> ```
> Input: 2.00000, 10
> Output: 1024.00000
> ```
>
> **Example 2:**
>
> ```
> Input: 2.10000, 3
> Output: 9.26100
> ```
>
> **Example 3:**
>
> ```
> Input: 2.00000, -2
> Output: 0.25000
> Explanation: 2-2 = 1/22 = 1/4 = 0.25
> ```
>
> **Note:**
>
> - -100.0 < *x* < 100.0
> - *n* is a 32-bit signed integer, within the range [−231, 231 − 1]

1. Medium。

```cpp
// double x。
class Solution {
public:
    double myPow(double x, int n) {
        if (n == 0) return 1;
        if (n < 0) {
            // 指数的负号转移给底数，这样变成了指数为正的情况。最多执行一次。
            n = -n; // 这里在n为INT_MIN时，由于INT_MAX比-INT_MIN小1，所以`-n`会溢出得到INT_MIN。补码取相反数就是二进制位取反加一，INT_MIN是1(0)31，即没有正权抵消负权的情况，而INT_MAX是0(1)31，即正权最大，没有负权的情况，INT_MIN取反得到INT_MAX，再加一还是得到INT_MIN。
            x = 1/x;
        }
        return ((n&1)? x: 1)*myPow(x*x, n/2);
    }
};
```

```cpp
// double myPow。
class Solution {
public:
    double myPow(double x, int n) {
        if (n == 0) return 1;
        double t = myPow(x, n/2); // 递归函数的宏观设计，不管n是正是负，myPow都会输出正确的答案t。
        if (n&1)
            return (n<0? 1/x: x)*t*t; // 如果n是负的，
        return t*t;
    }
};
```

```cpp
// 迭代版，3^21=3^(16+4+1)=(3^16)*(3^4)*(3^1)。
class Solution {
public:
    double myPow(double x, int n) {
        if (n < 0) {
            if (n == INT_MIN) {
                // n--; // 也可以，补码减法就是加上减数取反后的数。加了-1，最高位会进位溢出，丢掉。但leetcode会报错，所以不用。
                n = -(n+1);
                x = 1/(x*x);
            } else {
                n = -n;
                x = 1/x;
            }
        }
        double ans = 1.0;
        while (n) {
            if (n&1) ans *= x;
            x *= x;
            n >>= 1;
            // n >> 1; // 容易写错，没有赋值更新循环变量，就会无限循环。
        }
        return ans;
    }
};
```

