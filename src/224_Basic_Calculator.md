# 224. Basic Calculator

> Implement a basic calculator to evaluate a simple expression string.
>
> The expression string may contain open `(` and closing parentheses `)`, the plus `+` or minus sign `-`, **non-negative** integers and empty spaces ``.
>
> **Example 1:**
>
> ```
> Input: "1 + 1"
> Output: 2
> ```
>
> **Example 2:**
>
> ```
> Input: " 2-1 + 2 "
> Output: 3
> ```
>
> **Example 3:**
>
> ```
> Input: "(1+(4+5+2)-3)+(6+8)"
> Output: 23
> ```
>
> **Note:**
>
> - You may assume that the given expression is always valid.
> - **Do not** use the `eval` built-in library function.

1. Medium。

```java
class Solution {
    public int calculate(String s) {
        if(s == null) return 0;

        int result = 0;
        int sign = 1;
        int num = 0;

        Stack<Integer> stack = new Stack<Integer>();
        stack.push(sign); // 将整个表达式看作被括号包围，括号外是一个正号。

        for(int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if(c >= '0' && c <= '9') {
                num = num * 10 + (c - '0');

            } else if(c == '+' || c == '-') {
                result += sign * num;
                sign = stack.peek() * (c == '+' ? 1: -1); // 要综合括号外的符号。
                num = 0;

            } else if(c == '(') {
                stack.push(sign);

            } else if(c == ')') {
                stack.pop();
            }
        }

        result += sign * num;
        return result;
    }
}
```

