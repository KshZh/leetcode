# 151. Reverse Words in a String

> Given an input string, reverse the string word by word.
>
> **Example 1:**
>
> ```
> Input: "the sky is blue"
> Output: "blue is sky the"
> ```
>
> **Example 2:**
>
> ```
> Input: "  hello world!  "
> Output: "world! hello"
> Explanation: Your reversed string should not contain leading or trailing spaces.
> ```
>
> **Example 3:**
>
> ```
> Input: "a good   example"
> Output: "example good a"
> Explanation: You need to reduce multiple spaces between two words to a single space in the reversed strig.
> ```
>
> **Note:**
>
> - A word is defined as a sequence of non-space characters.
> - Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
> - You need to reduce multiple spaces between two words to a single space in the reversed string.
>
> **Follow up:**
>
> For C programmers, try to solve it *in-place* in *O*(1) extra space.

1. Medium。

```cpp
class Solution {
public:
    string reverseWords(string s) {
        auto n = s.size();
        int i, j, begin;
        bool needSpace = false;
        // 使用双指针移动单词后再对单词做反转。
        for (i=j=0; i<n; i++) {
            // 跳过空格。
            if (s[i] != ' ') {
                if (needSpace) s[j++] = ' '; // XXX 前面有单词，添加一个空格。而不是一个单词随后跟一个空格，这样不好处理，因为会有多种情况，如"a wi"，这种情况j不指向空格，但"a wi "，这种情况，j指向空格。然后当我们根据j确定去掉重复空格后的字符串长度时，就会很麻烦。
                begin = j;
                for (; i<n && s[i]!=' '; i++) {
                    s[j++] = s[i];
                }
                reverse(s, begin, j);
                numWord = true;
            }
        }
        reverse(s, 0, j);
        return s.substr(0, j);
    }
    
    // s[i, j).
    void reverse(string& s, int i, int j) {
        while (i < j) {
            std::swap(s[i++], s[--j]);
        }
    }
};
```

