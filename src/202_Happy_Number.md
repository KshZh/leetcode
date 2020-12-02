# 202. Happy Number

> Write an algorithm to determine if a number is "happy".
>
> A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.
>
> **Example:** 
>
> ```
> Input: 19
> Output: true
> Explanation: 
> 12 + 92 = 82
> 82 + 22 = 68
> 62 + 82 = 100
> 12 + 02 + 02 = 1
> ```

1. Easy。

```cpp
class Solution {
public:
    bool isHappy(int n) {
        unordered_set<int> visited;
        visited.insert(n);
        int x;
        while (true) {
            x = 0;
            while (n) {
                x += (n%10)*(n%10);
                n/=10;
            }
            if (x == 1) return true;
            if (visited.find(x) != visited.end()) return false;
            n = x;
            visited.insert(n);
        }
    }
};
```

```cpp
// folyd算法检测环/快慢指针，O(1)空间复杂度。
int digitSquareSum(int n) {
    int sum = 0, tmp;
    while (n) {
        tmp = n % 10;
        sum += tmp * tmp;
        n /= 10;
    }
    return sum;
}

bool isHappy(int n) {
    int slow, fast;
    slow = fast = n;
    do {
        slow = digitSquareSum(slow);
        fast = digitSquareSum(fast);
        fast = digitSquareSum(fast);
    } while(slow != fast);
    if (slow == 1) return 1;
    else return 0;
}
```

