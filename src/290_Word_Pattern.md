# 290. Word Pattern

> Given a `pattern` and a string `str`, find if `str` follows the same pattern.
>
> Here **follow** means a full match, such that there is a bijection between a letter in `pattern` and a **non-empty** word in `str`.
>
> **Example 1:**
>
> ```
> Input: pattern = "abba", str = "dog cat cat dog"
> Output: true
> ```
>
> **Example 2:**
>
> ```
> Input:pattern = "abba", str = "dog cat cat fish"
> Output: false
> ```
>
> **Example 3:**
>
> ```
> Input: pattern = "aaaa", str = "dog cat cat dog"
> Output: false
> ```
>
> **Example 4:**
>
> ```
> Input: pattern = "abba", str = "dog dog dog dog"
> Output: false
> ```
>
> **Notes:**
> You may assume `pattern` contains only lowercase letters, and `str` contains lowercase letters that may be separated by a single space.

1. Easy。

```cpp
// "abba"
// "dog cat cat dog" true
// "abba"
// "dog cat cat fish" false
// "aaa"
// "aa aa aa aa" false
// "jquery"
// "jquery" false
// 两种边界情况，一是pattern比较短，而是str比较短。
bool wordPattern(string pattern, string str) {
    unordered_map<char, string> p2s;
    unordered_map<string, char> s2p;
    auto n=str.size();
    int i=0, j;
    for (char c: pattern) {
        if (i == n+1) {
            return false;
        }
        for (j=i; j<n && str[j]!=' '; j++)
            ;
        // string s = str.substr(i, j);
        // 注意string::substr()的第二个参数是长度，而不是结束位置。
        string s = str.substr(i, j-i);
        if (s2p.find(s)==s2p.end() && p2s.find(c)==p2s.end()) {
            s2p[s] = c;
            p2s[c] = s;
        } else if (s2p[s]!=c || p2s[c]!=s) {
            return false;
        }
        i = j+1;
    }
    return i==n+1;
}
```

```cpp
bool wordPattern(string pattern, string str) {
    unordered_map<char, int> p2i;
    unordered_map<string, int> w2i;
    istringstream in(str);
    int i = 0, n = pattern.size();
    for (string word; in >> word; ++i) {
        if (i == n || p2i[pattern[i]] != w2i[word])
            return false;
        p2i[pattern[i]] = w2i[word] = i + 1;
    }
    return i == n;
}
```

