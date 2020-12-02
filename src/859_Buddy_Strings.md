# 859. Buddy Strings

> Given two strings `A` and `B` of lowercase letters, return `true` if and only if we can swap two letters in `A` so that the result equals `B`.
>
> **Example 1:**
>
> ```
> Input: A = "ab", B = "ba"
> Output: true
> ```
>
> **Example 2:**
>
> ```
> Input: A = "ab", B = "ab"
> Output: false
> ```
>
> **Example 3:**
>
> ```
> Input: A = "aa", B = "aa"
> Output: true
> ```
>
> **Example 4:**
>
> ```
> Input: A = "aaaaaaabc", B = "aaaaaaacb"
> Output: true
> ```
>
> **Example 5:**
>
> ```
> Input: A = "", B = "aa"
> Output: false
> ```
>
> **Note:**
>
> 1. `0 <= A.length <= 20000`
> 2. `0 <= B.length <= 20000`
> 3. `A` and `B` consist only of lowercase letters.

1. Easy。

```cpp
class Solution {
public:
    bool buddyStrings(string A, string B) {
        // 并不需要真的去交换。
        // 1. 如果A!=B，且有且只有两个字符不相等，那么A可以通过交换一次与B相等，否则不行。并且别忘了，除了不相等字符数量上的限制，还要A与B对应的字符交叉相等才行。也可以直接交换一次，看A是否等于B。
        // 2. 如果A==B，且有某个字符出现次数大于等于2，那么可以通过交换这个相等的字符，使得还是A==B，否则不行。
        if (A.size() != B.size()) return false;
        if (A == B) {
            int cnt[26]{0}, i;
            for (i=0; i<A.size(); i++) {
                cnt[A[i]-'a']++;
            }
            for (i=0; i<26; i++) {
                if (cnt[i] > 1) return true;
            }
            return false;
        } else {
            // 这里也可以用一个vector，然后把不相等字符的下标直接推入其中，这样可以简化代码。
            int first=-1, second=-1, i;
            for (i=0; i<A.size(); i++) {
                if (A[i] != B[i]) {
                    if (first == -1) {
                        first = i;
                    } else if (second == -1) {
                        second = i;
                    } else { // 多于两个字符不相等，肯定无法通过一次交换使得A==B。
                        return false;
                    }
                }
            }
            return first!=-1 && second!=-1 && A[first]==B[second] && A[second]==B[first];
        }
    }
};
```

