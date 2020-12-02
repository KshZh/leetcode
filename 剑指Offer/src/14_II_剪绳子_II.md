# 14- II. 剪绳子 II

> 给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m] 。请问 k[0]\*k[1]\*...\*k[m] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
>
> 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。
>

1. Medium。

```java
// 这道题不能用dp了，因为乘法可能溢出，所以需要取模，但取模后就无法比较大小了。比如100取模后得到3，接着来一个不溢出的数40，这时如果按照正常规则比较，会得到错误的结果。
// 还是用数学/贪心方法，只不过用快速幂来自己求幂，而不是调用库函数，因为直接调用结果可能溢出（一个数的幂次很容易溢出），要在过程中也取模才行。
class Solution {
    public int cuttingRope(int n) {
        if(n <= 3) return n - 1;
        int b = n % 3, p = 1000000007;
        long rem = 1, x = 3; // 这里要用long，否则rem*x还没取模就溢出了，溢出后再取模就没意义了。
        for(int a = n / 3 - 1; a > 0; a /= 2) { // 指数a。
            if(a % 2 == 1) rem = (rem * x) % p;
            x = (x * x) % p;
        }
        if(b == 0) return (int)(rem * 3 % p);
        if(b == 1) return (int)(rem * 4 % p);
        return (int)(rem * 6 % p);
    }
}

// 作者：jyd
// 链接：https://leetcode-cn.com/problems/jian-sheng-zi-ii-lcof/solution/mian-shi-ti-14-ii-jian-sheng-zi-iitan-xin-er-fen-f/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```

