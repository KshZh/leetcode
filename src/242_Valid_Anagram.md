# 242. Valid Anagram

> Given two strings *s* and *t* , write a function to determine if *t* is an anagram of *s*.
>
> **Example 1:**
>
> ```
> Input: s = "anagram", t = "nagaram"
> Output: true
> ```
>
> **Example 2:**
>
> ```
> Input: s = "rat", t = "car"
> Output: false
> ```
>
> **Note:**
> You may assume the string contains only lowercase alphabets.
>
> **Follow up:**
> What if the inputs contain unicode characters? How would you adapt your solution to such case?

1. Easy。

```cpp
// 如果包含更大范围的字符，那就用哈希表。
// 也可以排序，比较字符串是否相同，不过这个方法的时间复杂度是O(NlogN)。
class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;
        int cnt[26]{};
        for (int i=0; i<s.size(); i++) {
            cnt[s[i]-'a']++;
            cnt[t[i]-'a']--;
        }
        for (int i=0; i<26; i++) {
            if (cnt[i] != 0)
                return false;
        }
        return true;
    }
};
```

