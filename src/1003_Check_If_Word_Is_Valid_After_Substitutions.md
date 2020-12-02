# 1003. Check If Word Is Valid After Substitutions

> We are given that the string `"abc"` is valid.
>
> From any valid string `V`, we may split `V` into two pieces `X` and `Y` such that `X + Y` (`X` concatenated with `Y`) is equal to `V`. (`X` or `Y` may be empty.) Then, `X + "abc" + Y` is also valid.
>
> If for example `S = "abc"`, then examples of valid strings are: `"abc", "aabcbc", "abcabc", "abcabcababcc"`. Examples of **invalid** strings are: `"abccba"`, `"ab"`, `"cababc"`, `"bac"`.
>
> Return `true` if and only if the given string `S` is valid.
>
> **Example 1:**
>
> ```
> Input: "aabcbc"
> Output: true
> Explanation: 
> We start with the valid string "abc".
> Then we can insert another "abc" between "a" and "bc", resulting in "a" + "abc" + "bc" which is "aabcbc".
> ```
>
> **Example 2:**
>
> ```
> Input: "abcabcababcc"
> Output: true
> Explanation: 
> "abcabcabc" is valid after consecutive insertings of "abc".
> Then we can insert "abc" before the last letter, resulting in "abcabcab" + "abc" + "c" which is "abcabcababcc".
> ```
>
> **Example 3:**
>
> ```
> Input: "abccba"
> Output: false
> ```
>
> **Example 4:**
>
> ```
> Input: "cababc"
> Output: false
> ```

1. Medium。
2. [Stack Solution O(N)](https://leetcode.com/problems/check-if-word-is-valid-after-substitutions/discuss/247626/JavaPythonC%2B%2B-Stack-Solution-O(N))
3. 类似于[Valid Parentheses](https://leetcode.com/problems/valid-parentheses/)。
4. 使用不断删除"abc"和不断拼接的方式，看最终是否为空字符串。相比于第一份代码，我们可以用字符栈来执行不断删除固定搭配然后拼接的操作。

```python
def isValid(self, S):
    S2 = ""
    while S != S2:
        S, S2 = S.replace("abc", ""), S
        return S == ""
```

```cpp
class Solution {
public:
    bool isValid(string S) {
        vector<char> stack;
        size_t n;
        for (char c: S) {
            if (c == 'c') {
                if (stack.empty() || stack.back()!='b') return false;
                stack.pop_back();
                if (stack.empty() || stack.back()!='a') return false;
                stack.pop_back();
            } else {
                stack.push_back(c);
            }
        }
        // return true;
        return stack.empty(); // 是否删掉了全部的"abc"。
    }
};
```

