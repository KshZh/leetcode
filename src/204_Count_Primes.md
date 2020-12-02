# 204. Count Primes

> Count the number of prime numbers less than a non-negative number, ***n\***.
>
> **Example:**
>
> ```
> Input: 10
> Output: 4
> Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
> ```

1. Easy。

```cpp
class Solution {
    bool isPrime(int x) {
        if (x <= 1) return false;
        int end = sqrt(x);
        for (int i=2; i<=end; i++) { // 注意要等于。
            if (x%i == 0) return false;
        }
        return true;
    }
public:
    int countPrimes(int n) {
        int cnt = 0;
        for (int i=2; i<n; i++) {
            if (isPrime(i)) cnt++;
        }
        return cnt;
    }
};
```

```cpp
// 筛法获取素数。
class Solution {
public:
    int countPrimes(int n) {
        if (n <= 1) return 0;
        vector<bool> prime(n, true);
        prime[0] = false, prime[1] = false;
        int cnt = 0;
        for (int i=2; i<n; i++) {
            if (prime[i]) {
                cnt++;
                for (int j=i+i; j<n; j+=i) {
                    prime[j] = false;
                }
            }
        }
        return cnt;
    }
};
```

