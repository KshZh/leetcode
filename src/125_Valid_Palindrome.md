# 125. Valid Palindrome

> Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
>
> **Note:** For the purpose of this problem, we define empty string as valid palindrome.
>
> **Example 1:**
>
> ```
> Input: "A man, a plan, a canal: Panama"
> Output: true
> ```
>
> **Example 2:**
>
> ```
> Input: "race a car"
> Output: false
> ```

1. Easy。

```cpp
class Solution {
public:
    bool isPalindrome(string s) {
        if (s.empty()) return true;
        for (int i=0, j=s.size()-1; i<j; ) {
            if (!isalnum(s[i])) {
                i++;
                continue;
            }
            if (!isalnum(s[j])) {
                j--;
                continue;
            }
            // 这个谓词利用大小写字母相差32的性质，但是会被"0P"这样的边界测试卡住。
            // if (s[i]-s[j]!=0 && abs(s[i]-s[j])!=32)
            if (tolower(s[i])!=tolower(s[j]))
                return false;
            else
                i++, j--;
        }
        return true;
    }
};
```

