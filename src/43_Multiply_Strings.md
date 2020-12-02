# 43. Multiply Strings

> Given two non-negative integers `num1` and `num2` represented as strings, return the product of `num1` and `num2`, also represented as a string.
>
> **Example 1:**
>
> ```
> Input: num1 = "2", num2 = "3"
> Output: "6"
> ```
>
> **Example 2:**
>
> ```
> Input: num1 = "123", num2 = "456"
> Output: "56088"
> ```
>
> **Note:**
>
> 1. The length of both `num1` and `num2` is < 110.
> 2. Both `num1` and `num2` contain only digits `0-9`.
> 3. Both `num1` and `num2` do not contain any leading zero, except the number 0 itself.
> 4. You **must not use any built-in BigInteger library** or **convert the inputs to integer** directly.

1. Medium。

```cpp
class Solution {
public:
    string multiply(string num1, string num2) {
        int m = num1.size(), n = num2.size();
        string ans(m + n, '0');
        for (int i = m - 1; i >= 0; i--) {
            for (int j = n - 1; j >= 0; j--) {
                // 当前位是i+j+1，这是因为i, j最大分别是m-1和n-1，
                // 故i+j最大为m+n-2，再加1得到m+n-1，也就是ans数组的最后一位。
                int sum = (num1[i] - '0') * (num2[j] - '0') + (ans[i + j + 1] - '0');
                ans[i + j + 1] = sum % 10 + '0';
                ans[i + j] += sum / 10;
            }
        }
        for (int i = 0; i < m + n; i++) {
            if (ans[i] != '0') {
                return ans.substr(i);
            }
        }
        return "0";
    }
};
```

