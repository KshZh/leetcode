# 191. Number of 1 Bits

> Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the [Hamming weight](http://en.wikipedia.org/wiki/Hamming_weight)).
>
> **Example 1:**
>
> ```
> Input: 00000000000000000000000000001011
> Output: 3
> Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
> ```
>
> **Example 2:**
>
> ```
> Input: 00000000000000000000000010000000
> Output: 1
> Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
> ```
>
> **Example 3:**
>
> ```
> Input: 11111111111111111111111111111101
> Output: 31
> Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.
> ```

1. Easy。

![](https://leetcode.com/media/original_images/191_Number_Of_Bits.png)

```cpp
// 时间复杂度为O(1)，因为n是一个32位无符号数，注意，不是O(N)。
class Solution {
public:
    int hammingWeight(uint32_t n) {
        int cnt = 0;
        while (n) {
            cnt += n&1;
            n >>= 1;
        }
        return cnt;
    }
};
```

```cpp
// 在这个实现中，有多少个1就循环几次，而上面的实现对于最高的那几位有1的输入，几乎循环32次。
class Solution {
public:
    int hammingWeight(uint32_t n) {
        int cnt = 0;
        while (n) {
            cnt++;
            n &= (n-1); // 消除最低有效的1。`n-1`使得n的最低有效的1被借位变为0。
        }
        return cnt;
    }
};
```

