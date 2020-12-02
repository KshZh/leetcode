# 1456. Maximum Number of Vowels in a Substring of Given Length

> Given a string `s` and an integer `k`.
>
> Return *the maximum number of vowel letters* in any substring of `s` with length `k`.
>
> **Vowel letters** in English are (a, e, i, o, u).
>
>  
>
> **Example 1:**
>
> ```
> Input: s = "abciiidef", k = 3
> Output: 3
> Explanation: The substring "iii" contains 3 vowel letters.
> ```
>
> **Example 2:**
>
> ```
> Input: s = "aeiou", k = 2
> Output: 2
> Explanation: Any substring of length 2 contains 2 vowels.
> ```
>
> **Example 3:**
>
> ```
> Input: s = "leetcode", k = 3
> Output: 2
> Explanation: "lee", "eet" and "ode" contain 2 vowels.
> ```
>
> **Example 4:**
>
> ```
> Input: s = "rhythms", k = 4
> Output: 0
> Explanation: We can see that s doesn't have any vowel letters.
> ```
>
> **Example 5:**
>
> ```
> Input: s = "tryhard", k = 4
> Output: 1
> ```
>
>  
>
> **Constraints:**
>
> - `1 <= s.length <= 10^5`
> - `s` consists of lowercase English letters.
> - `1 <= k <= s.length`

```java
class Solution {
    public int maxVowels(String s, int k) {
        int n = s.length();
        int max=0, cnt=0;
        for (int i=0, j=0; j<n; j++) {
            if (j-i >= k) {
                // 扩展右端点导致窗口大小超出限制，那么推进窗口的左端点。
                if (isVowelLetter(s.charAt(i++))) {
                    cnt--;
                }
            }
            if (isVowelLetter(s.charAt(j))) {
                cnt++;
                if (cnt > max) {
                    max = cnt;
                }
            }
        }
        return max;
    }
    
    private boolean isVowelLetter(char c) {
        return c=='a' || c=='e' || c=='i' || c=='o' || c=='u';
    }
}
```

