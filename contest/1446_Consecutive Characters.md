# 1446. Consecutive Characters

> Given a string `s`, the power of the string is the maximum length of a non-empty substring that contains only one unique character.
>
> Return *the power* of the string.
>
> 
>
> **Example 1:**
>
> ```
> Input: s = "leetcode"
> Output: 2
> Explanation: The substring "ee" is of length 2 with the character 'e' only.
> ```
>
> **Example 2:**
>
> ```
> Input: s = "abbcccddddeeeeedcba"
> Output: 5
> Explanation: The substring "eeeee" is of length 5 with the character 'e' only.
> ```

```java
class Solution {
    public int maxPower(String s) {
        int n = s.length();
        int max=1, i, j;
        for (i=1, j=0; i<n; i++) {
            if (s.charAt(i) != s.charAt(j)) {
                max = Math.max(max, i-j);
                j = i;
            }
        }
        // 注意循环外还要再处理一次，因为当i==n时，来不及处理就退出循环了。
        // 如果大意没有在循环外继续处理，则测试用例"cc"的结果就是1，是错误的。
        max = Math.max(max, i-j);
        return max;
    }
}
```

