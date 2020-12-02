# 150. Evaluate Reverse Polish Notation

> Evaluate the value of an arithmetic expression in [Reverse Polish Notation](http://en.wikipedia.org/wiki/Reverse_Polish_notation).
>
> Valid operators are `+`, `-`, `*`, `/`. Each operand may be an integer or another expression.
>
> **Note:**
>
> - Division between two integers should truncate toward zero.
> - The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
>
> **Example 1:**
>
> ```
> Input: ["2", "1", "+", "3", "*"]
> Output: 9
> Explanation: ((2 + 1) * 3) = 9
> ```
>
> **Example 2:**
>
> ```
> Input: ["4", "13", "5", "/", "+"]
> Output: 6
> Explanation: (4 + (13 / 5)) = 6
> ```
>
> **Example 3:**
>
> ```
> Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
> Output: 22
> Explanation: 
>   ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
> = ((10 * (6 / (12 * -11))) + 17) + 5
> = ((10 * (6 / -132)) + 17) + 5
> = ((10 * 0) + 17) + 5
> = (0 + 17) + 5
> = 17 + 5
> = 22
> ```

1. Medium。
2. 逆波兰表示法的结构使得我们不必考虑运算符的优先级。

```cpp
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        stack<int> nums;
        int num1, num2;
        for (int i=0; i<tokens.size(); i++) {
            // if (tokens[i][0]>='0' && tokens[i][0]<='9') { // 数字字符串可能是"-213"或"+21"。
            // 也可以先判断是否为+-*/其中的任意一个。
            try {
                nums.push(std::stoi(tokens[i]));
            } catch (std::invalid_argument e) {
                num1 = nums.top();
                nums.pop();
                num2 = nums.top();
                nums.pop();
                switch (tokens[i][0]) {
                    case '+': nums.push(num1+num2); break;
                    case '-': nums.push(num2-num1); break; // 注意后弹出的是先入栈的，是二元运算中的第一个操作数。
                    case '*': nums.push(num1*num2); break;
                    case '/': nums.push(num2/num1); break;
                }
            }
        }
        return nums.top();
    }
};
```

```cpp
class Solution {
public:
    int evalRPN(vector<string>& tokens) {
        unordered_map<string, function<int (int, int) > > map = {
            { "+" , [] (int a, int b) { return a + b; } },
            { "-" , [] (int a, int b) { return a - b; } },
            { "*" , [] (int a, int b) { return a * b; } },
            { "/" , [] (int a, int b) { return a / b; } }
        };
        std::stack<int> stack;
        for (string& s : tokens) {
            if (!map.count(s)) {
                stack.push(stoi(s));
            } else {
                int op1 = stack.top();
                stack.pop();
                int op2 = stack.top();
                stack.pop();
                stack.push(map[s](op2, op1));
            }
        }
        return stack.top();
    }
};
```

