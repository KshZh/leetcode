# 227. Basic Calculator II

> Implement a basic calculator to evaluate a simple expression string.
>
> The expression string contains only **non-negative** integers, `+`, `-`, `*`, `/` operators and empty spaces ``. The integer division should truncate toward zero.
>
> **Example 1:**
>
> ```
> Input: "3+2*2"
> Output: 7
> ```
>
> **Example 2:**
>
> ```
> Input: " 3/2 "
> Output: 1
> ```
>
> **Example 3:**
>
> ```
> Input: " 3+5 / 2 "
> Output: 5
> ```
>
> **Note:**
>
> - You may assume that the given expression is always valid.
> - **Do not** use the `eval` built-in library function.

1. Medium。

```cpp
// 关键是要处理好运算的优先级，这里的做法是将+和-看作一元运算，而不是二元运算。
class Solution {
public:
    int calculate(string s) {
        stack<int> nums;
        auto n = s.size();
        long num = 0, x;
        char sign = '+';
        for (int i=0; i<n; i++) {
            if (isdigit(s[i])) num = num*10+s[i]-'0';
            if ((!isdigit(s[i]) && s[i]!=' ') || i==n-1) {
                if (sign == '+') nums.push(num);
                else if (sign == '-') nums.push(-num);
                else if (sign == '*') {
                    x = nums.top()*num;
                    nums.pop();
                    nums.push(x);
                } else {
                    x = nums.top()/num;
                    nums.pop();
                    nums.push(x);
                }
                sign = s[i];
                num = 0;
            }
        }
        int ans = 0;
        while (!nums.empty()) {
            ans += nums.top();
            nums.pop();
        }
        return ans;
    }
};
```

```cpp
// 思路与上面的差不多，但triky。
class Solution {
public:
    int calculate(string s) {
        // 使用istringstream，可以自动忽略空白符（包括前导空白符），很方便将数字字符串输出到整型或浮点型（科学计数法也能解析）。
        istringstream in("+"+s+"+");
        char op;
        int ans=0, temp=0, x;
        while (in >> op) {
            if (op=='+' || op=='-') {
                ans += temp;
                in >> temp;
                temp *= 44-op; // '+'的ascii码是45，'-'的ascii码是43。
            } else {
                in >> x;
                if (op == '*') temp*=x;
                else temp/=x;
            }
        }
        return ans;
    }
};
```

