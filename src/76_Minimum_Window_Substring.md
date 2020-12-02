# 76. Minimum Window Substring

> Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
>
> **Example:**
>
> ```
> Input: S = "ADOBECODEBANC", T = "ABC"
> Output: "BANC"
> ```
>
> **Note:**
>
> - If there is no such window in S that covers all characters in T, return the empty string `""`.
> - If there is such window, you are guaranteed that there will always be only one unique minimum window in S.

1. Hard，滑动窗口。

> In any sliding window based problem we have two pointers. One *right* pointer whose job is to **expand** the current window and then we have the *left* pointer whose job is to **contract** a given window. **At any point in time only one of these pointers move** and the other one remains fixed.

```cpp
class Solution {
public:
    string minWindow(string s, string t) {
        int begin=0, end=0;
        unordered_map<char, int> dictT;
        for (char c: t) dictT[c]++;
        int numRequired=t.size(), min=INT_MAX, head=0;
        while (end < s.size()) {
            if (dictT.find(s[end])!=dictT.end() && dictT[s[end]]-->0) numRequired--;
            while (numRequired == 0) {
                if (end-begin+1 < min) { // 右闭减左闭加一等于区间长度。
                    min = end-begin+1;
                    head = begin;
                }
                if (dictT.find(s[begin])!=dictT.end() && dictT[s[begin]]++==0) numRequired++;
                begin++;
            }
            end++;
        }
        return min==INT_MAX? "": s.substr(head, min);
    }
};
```

```cpp
// Approach 2: Optimized Sliding Window.
class Solution {
public:
    string minWindow(string s, string t) {
        int begin=0, end=0;
        unordered_map<char, int> dictT;
        for (char c: t) dictT[c]++;
        int numRequired=t.size(), min=INT_MAX, head=0;
        
        vector<pair<char, int>> filteredS;
        for (int i=0; i<s.size(); i++) {
            if (dictT.find(s[i]) != dictT.end()) {
                filteredS.emplace_back(s[i], i);
            }
        }
        
        while (end < filteredS.size()) {
            if (dictT[filteredS[end].first]-->0) numRequired--;
            while (numRequired == 0) {
                if (filteredS[end].second-filteredS[begin].second+1 < min) { // 右闭减左闭加一等于区间长度。
                    min = filteredS[end].second-filteredS[begin].second+1;
                    head = filteredS[begin].second;
                }
                if (dictT[filteredS[begin].first]++==0) numRequired++;
                begin++;
            }
            end++;
        }
        return min==INT_MAX? "": s.substr(head, min);
    }
};
```

