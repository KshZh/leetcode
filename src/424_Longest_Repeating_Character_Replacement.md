# 424. Longest Repeating Character Replacement

> Given a string `s` that consists of only uppercase English letters, you can perform at most `k` operations on that string.
>
> In one operation, you can choose **any** character of the string and change it to any other uppercase English character.
>
> Find the length of the longest sub-string containing all repeating letters you can get after performing the above operations.
>
> **Note:**
> Both the string's length and *k* will not exceed 104.
>
> **Example 1:**
>
> ```
> Input:
> s = "ABAB", k = 2
> 
> Output:
> 4
> 
> Explanation:
> Replace the two 'A's with two 'B's or vice versa.
> ```
>
> **Example 2:**
>
> ```
> Input:
> s = "AABABBA", k = 1
> 
> Output:
> 4
> 
> Explanation:
> Replace the one 'A' in the middle with 'B' and form "AABBBBA".
> The substring "BBBB" has the longest repeating letters, which is 4.
> ```

1. Medium。

> **`maxCount` may be invalid at some points, but this doesn't matter, because it was valid earlier in the string, and all that matters is finding the max window that occurred \*anywhere\* in the string**. Additionally, it will expand ***if and only if\*** enough repeating characters appear in the window to make it expand. So whenever it expands, it's a valid expansion.

```cpp
class Solution {
public:
    int characterReplacement(string s, int k) {
        int cnt[26]{0}; // 窗口内的各字符的个数。
        // max是窗口内各字符个数的最大值。
        int max=INT_MIN, start=0, end;
        auto n = s.size();
        for (end=0; end<n; end++) {
            max = std::max(max, ++cnt[s[end]-'A']);
            if (end-start+1-max > k) { // end-start+1是当前窗口大小，如果窗口中除了max个字符x，还有其他大于k个字符，那么就无法通过k次操作使得窗口内只包含重复的单一字符，所以只能调整左端点。
                cnt[s[start++]-'A']--;
            }
        }
        return n-start;
    }
};
```

