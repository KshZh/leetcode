# 171. Excel Sheet Column Number

> Given a column title as appear in an Excel sheet, return its corresponding column number.
>
> For example:
>
> ```
>     A -> 1
>     B -> 2
>     C -> 3
>     ...
>     Z -> 26
>     AA -> 27
>     AB -> 28 
>     ...
> ```
>
> **Example 1:**
>
> ```
> Input: "A"
> Output: 1
> ```
>
> **Example 2:**
>
> ```
> Input: "AB"
> Output: 28
> ```
>
> **Example 3:**
>
> ```
> Input: "ZY"
> Output: 701
> ```

1. Easy。

```cpp
class Solution {
public:
    int titleToNumber(string s) {
        // 有26个状态，所以是26进制，但从1开始。所以要加一。
        int n=0;
        for (int i=0; i<s.size(); i++) {
            n = n*26+(s[i]-'A'+1); // 26进制。
        }
        return n;
    }
};
```

