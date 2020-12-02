# 387. First Unique Character in a String

> Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
>
> **Examples:**
>
> ```
> s = "leetcode"
> return 0.
> 
> s = "loveleetcode",
> return 2.
> ```
>
> **Note:** You may assume the string contain only lowercase letters.

1. Easy。

```cpp
// 时间复杂度是O(N)，空间复杂度是O(26)，即O(1)。
class Solution {
public:
    int firstUniqChar(string s) {
        // int idx[26]{-1}; // 只有第一个元素被初始化为-1，其他初始化为0。
        // 要么就调用`std::fill_n(array, 100, -1);`进行初始化。
        vector<int> idx(26, -1);
        for (int i=0; i<s.size(); i++) {
            if (idx[s[i]-'a'] != -1) {
                idx[s[i]-'a'] = -2; // 不能置为-1，考虑"ababa"，那么会得出错误的结果4，但正确应该是-1。
            } else {
                idx[s[i]-'a'] = i;
            }
        }
        int min = INT_MAX;
        for (int i=0; i<26; i++) {
            if (idx[i]>=0 && idx[i]<min) {
                min = idx[i];
            }
        }
        return min==INT_MAX? -1: min;
    }
};
```

```cpp
// 其实直接计数代码会简单一些。
class Solution {
public:
    int firstUniqChar(string s) {
        int cnt[26]{0};
        for (int i=0; i<s.size(); i++) {
            cnt[s[i]-'a']++;
        }
        for (int i=0; i<s.size(); i++) {
            if (cnt[s[i]-'a'] == 1)
                return i;
        }
        return -1;
    }
};
```

