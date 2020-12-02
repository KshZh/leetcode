# 20. Valid Parentheses

> **Example 1:**
>
> ```
> Input: "()"
> Output: true
> ```
>
> **Example 2:**
>
> ```
> Input: "()[]{}"
> Output: true
> ```
>
> **Example 3:**
>
> ```
> Input: "(]"
> Output: false
> ```
>
> **Example 4:**
>
> ```
> Input: "([)]"
> Output: false
> ```
>
> **Example 5:**
>
> ```
> Input: "{[]}"
> Output: true
> ```

1. Easy，用栈执行删除固定搭配然后拼接的操作。

```cpp
class Solution {
public:
    bool isValid(string s) {
        vector<char> stack;
        for (char c: s) {
            switch (c) {
                case '(': stack.push_back(')'); break;
                case '[': stack.push_back(']'); break;
                case '{': stack.push_back('}'); break;
                default:
                    if (stack.empty() || stack.back() != c)
                        return false;
                    stack.pop_back();
            }
        }
        return stack.empty(); // 是否把所有配对的()[]{}删光了？
    }
};
```

