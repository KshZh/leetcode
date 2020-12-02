# 168. Excel Sheet Column Title

> Given a positive integer, return its corresponding column title as appear in an Excel sheet.
>
> For example:
>
> ```
>     1 -> A
>     2 -> B
>     3 -> C
>     ...
>     26 -> Z
>     27 -> AA
>     28 -> AB 
>     ...
> ```
>
> **Example 1:**
>
> ```
> Input: 1
> Output: "A"
> ```
>
> **Example 2:**
>
> ```
> Input: 28
> Output: "AB"
> ```
>
> **Example 3:**
>
> ```
> Input: 701
> Output: "ZY"
> ```

1. Medium。

```cpp
class Solution {
public:
    string convertToTitle(int n) {
        // 有26个状态，所以是26进制，但从1开始，
        // 所以获取一个数位时，要减掉1，使得从0开始。
        // 注意减一要作用到n上。
        vector<char> v;
        while (n) {
            v.push_back(--n%26+'A');
            n /= 26;
        }
        std::reverse(v.begin(), v.end()); // 因为先获得的是低位，所以要反转一下，让高位在前。
        return string(v.begin(), v.end());
    }
};
```

```cpp
class Solution {
public:
    string convertToTitle(int n) {
        // 递归写法。
        return n == 0 ? "" : convertToTitle(n / 26) + (char) (--n % 26 + 'A');
    }
};
```

