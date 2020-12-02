# 392. Is Subsequence

> Given a string **s** and a string **t**, check if **s** is subsequence of **t**.
>
> You may assume that there is only lower case English letters in both **s** and **t**. **t** is potentially a very long (length ~= 500,000) string, and **s** is a short string (<=100).
>
> A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, `"ace"` is a subsequence of `"abcde"` while `"aec"` is not).
>
> **Follow up:**
> If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

1. Easy，双指针。
2. 第一份代码的时间复杂度是O(T)，对于follow up，如果对于每次查询都调用一次第一份代码，那么总的最坏时间复杂度是O(KT)，而用第二份代码，那么是O(KSlogN)，这对于s比较短，t比较长的输入，改进还是比较显著的。
3. 第二份代码的思路在于，**如果s是t的子序列，那么`s[i]`在t中的下标必然大于`s[i-1]`在t中的下标**。然后按字符归类一个字符在t中的下标，这就得到该字符在t中的下标序列，这是一个上升序列，由此可以使用二分查找而非线性查找。

```cpp
class Solution {
public:
    bool isSubsequence(string s, string t) {
        int i, j;
        for (i=j=0; i<s.size() && j<t.size(); j++) {
            if (s[i] == t[j])
                i++;
        }
        return i==s.size();
    }
};
```

```cpp
class Solution {
public:
    bool isSubsequence(string s, string t) {
        int i, left, right, mid;
        // ==
        // 对于多次查询，下面这一部分只需要做一次即可。
        unordered_map<char, vector<int>> idx;
        for (i=0; i<t.size(); i++) {
            idx[t[i]].push_back(i); // 记录字符c在t中的下标。
        }
        // ==
        int prev = -1;
        for (char c: s) {
            if (idx.find(c) == idx.end())
                return false;
            // binary search
            // 找到当前c在t的下标序列中，第一个大于s中前一个字符在t中的下标的元素。
            left=0, right=idx[c].size();
            while (left < right) {
                mid = (left+right)/2;
                if (idx[c][mid] > prev)
                    right = mid;
                else
                    left = mid+1;
            }
            if (right == idx[c].size()) // 找不到说明s不是t的子串。
                return false;
            prev = idx[c][right];
        }
        return true;
    }
};
```

