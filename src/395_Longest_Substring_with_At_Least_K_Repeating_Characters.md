# 395. Longest Substring with At Least K Repeating Characters

> Find the length of the longest substring ***T\*** of a given string (consists of lowercase letters only) such that every character in ***T\*** appears no less than *k* times.
>
> **Example 1:**
>
> ```
> Input:
> s = "aaabb", k = 3
> 
> Output:
> 3
> 
> The longest substring is "aaa", as 'a' is repeated 3 times.
> ```
>
> **Example 2:**
>
> ```
> Input:
> s = "ababbc", k = 2
> 
> Output:
> 5
> 
> The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
> ```

1. Medium。

```java
// 滑动窗口。
class Solution {
    public int longestSubstring(String s, int k) {
        int d = 0;

        for (int numUniqueTarget = 1; numUniqueTarget <= 26; numUniqueTarget++)
            d = Math.max(d, longestSubstringWithNUniqueChars(s, k, numUniqueTarget));

        return d;
    }

    private int longestSubstringWithNUniqueChars(String s, int k, int numUniqueTarget) {
        // ascii编码了128个字符，如果使用int[26]，那么就需要map[s.get(i)-'a']了。
        int[] cnt = new int[128];
        int numUnique = 0; // counter 1
        int numNoLessThanK = 0; // counter 2
        int begin = 0, end = 0;
        int d = 0;

        while (end < s.length()) {
            if (cnt[s.charAt(end)]++ == 0) numUnique++; // s[end]的数量为0，那么扩展end后，不重复的字母个数增加了。
            if (cnt[s.charAt(end++)] == k) numNoLessThanK++; // s[end]在窗口中的个数大于等于k了。

            while (numUnique > numUniqueTarget) {
                if (cnt[s.charAt(begin)]-- == k) numNoLessThanK--;
                if (cnt[s.charAt(begin++)] == 0) numUnique--; // 当缩小窗口后，不重复的字母个数少了一个。
            }

            // if we found a string where the number of unique chars equals our target
            // and all those chars are repeated at least K times then update max
            if (numUnique == numUniqueTarget && numUnique == numNoLessThanK)
                d = Math.max(end - begin, d);
        }

        return d;
    }
}
```

```java
// 分治策略。
public class Solution {

    /**
     * Given a String s and an integer k, return the longest "valid" substring,
     * where a substring is valid iff every character in the substring occurs
     * at least k times.
     * 
     * @param s The given String
     * @param k The minimum number of times all substring characters must occur
     * @return The length of the longest valid substring
     */
    public int longestSubstring(String s, int k) {

        // Call divide and conquer helper method
        return div(s, 0, s.length(), k);
    }
    
    /**
     * Determines the length of the longest valid substring.
     * 
     * We achieve this by recursively splitting the given String on characters
     * who do not occur at least k times (since they cannot be part of the
     * longest valid substring).
     * 
     * Note that the substring of the current recursion is always equivalent
     * to s.substring(start, end).  For space reasons, we don't ever actually
     * create a new substring.
     * 
     * @param s The given String
     * @param start The beginning of the substring, inclusive
     * @param end The end of the substring, exclusive
     * @param k The minimum number of times all substring characters must occur
     * @return The length of the longest valid substring
     */
    private int div(String s, int start, int end, int k) {
        
        /**
         * Base Case 1 of 2:
         * 
         * If this substring is shorter than k, then no characters in it
         * can be repeated k times, therefore this substring and all
         * substrings that could be formed from it are invalid,
         * therefore return 0.
         */
        if (end - start < k) return 0; /// XXX 剪枝/递归终点。
        
        /**
         * Count the frequency of characters in this substring.
         * 
         * We are guaranteed from the problem statement that the given String
         * can only contain lowercase (English?) characters, so we use a
         * table of length 26 to store the character counts.
         */
        int[] a = new int[26];
        for (int i = start; i < end; i++) {
            a[s.charAt(i)-'a']++;
        }
        
        // For every character in the above frequency table
        for (int i = 0; i < a.length; i++){
            
            /**
             * If this character occurs at least once, but fewer than k times
             * in this substring, we know:
             * (1) this character cannot be part of the longest valid substring,
             * (2) the current substring is not valid.
             * 
             * Hence, we will "split" this substring on this character,
             * wherever it occurs, and check the substrings formed by that split
             */
            if (a[i] > 0 && a[i] < k) {
                
                /**
                 * Look for each occurrence of this character (i + 'a')
                 * in this substring.
                 */
                for (int j = start; j < end; j++) {
                    if (s.charAt(j) == i + 'a') {
                        
                        // "Split" into two substrings to solve recursively
                        int l = div(s, start, j, k);
                        int r = div(s, j + 1, end, k);
                        return Math.max(l, r);
                    }
                }
            }
        }
        
        /**
         * Base Case 2 of 2:
         * 
         * If every character in this substring occurs at least k times,
         * then this is a valid substring, so return this substring's length.
         */
        return end - start;
    }
}
```

