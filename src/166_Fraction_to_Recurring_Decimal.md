# 166. Fraction to Recurring Decimal

> Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
>
> If the fractional part is repeating, enclose the repeating part in parentheses.
>
> **Example 1:**
>
> ```
> Input: numerator = 1, denominator = 2
> Output: "0.5"
> ```
>
> **Example 2:**
>
> ```
> Input: numerator = 2, denominator = 1
> Output: "2"
> ```
>
> **Example 3:**
>
> ```
> Input: numerator = 2, denominator = 3
> Output: "0.(6)"
> ```

1. Medium。

```cpp
class Solution {
public:
    string fractionToDecimal(int numerator, int denominator) {
        if (numerator == 0) return "0";
        string ans;
        // 抑或求符号。
        if ((numerator>0) ^ (denominator>0))
            ans += '-';
        // 确定符号后，全转换为正数来处理。
        long n = labs(numerator);
        long d = labs(denominator);
        // 整数部分。
        ans += std::to_string(n/d);
        n %= d;
        if (n == 0) return ans;
        // 尾数部分。
        unordered_map<int, int> m;
        ans += ".";
        while (n) {
            if (m.find(n) != m.end()) {
                ans.insert(m[n], "(");
                ans += ")";
                return ans;
            }
            m[n] = ans.size();
            n *= 10;
            ans += std::to_string(n/d);
            n %= d;
        }
        return ans;
    }
};
```

