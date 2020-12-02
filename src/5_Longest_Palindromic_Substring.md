# 5. Longest Palindromic Substring

> Given a string **s**, find the longest palindromic substring in **s**. You may assume that the maximum length of **s** is 1000.
>
> **Example 1:**
>
> ```
> Input: "babad"
> Output: "bab"
> Note: "aba" is also a valid answer.
> ```
>
> **Example 2:**
>
> ```
> Input: "cbbd"
> Output: "bb"
> ```

1. Medium，dp。

#### Approach 1: Longest Common Substring

**Common mistake**

> For example, S*S* = "caba", S'*S*′ = "abac".
>
> The longest common substring between S*S* and S'*S*′ is "aba", which is the answer.
>
> Let’s try another example: S*S* = "abacdfgdcaba", S'*S*′ = "abacdgfdcaba".
>
> The longest common substring between S*S* and S'*S*′ is "abacd". Clearly, this is not a valid palindrome.

#### Approach 5: Manacher's Algorithm

```cpp
// 时间和空间复杂度都是O(N^2)。
class Solution {
public:
    string longestPalindrome(string s) {
		int i, x, j, len=s.size(), ansLeft=0, ansLen=1;
        vector<vector<bool>> dp(len, vector<bool>(len)); // dp[i][j]表示s[i, j]是否是回文字符串。
        // 边界：
		for (i=0; i<len; i++) {
			dp[i][i] = true;
			if (i<len && s[i]==s[i+1]) {
				dp[i][i+1] = true;
				ansLeft = i;
				ansLen = 2;
			}
		}
		for (x=3; x<=len; x++) {
            // 左闭加区间长度等于右开，所以可以`<=len`。
			for (i=0; i+x<=len; i++) { // 注意不是`i+=x`。
                j = i+x-1; // 右闭端点。
				if (s[i] == s[j] && dp[i+1][j-1]) {
					dp[i][j] = true;
					ansLeft = i;
					ansLen = x;
				}
			}
		}
		return s.substr(ansLeft, ansLen);
    }
};
```

```cpp
// 时间复杂度是O(N^2)，空间复杂度是O(1)。
class Solution {
public:
    string longestPalindrome(string s) {
		int i, len, len1, len2, ansLeft, ansLen=0;
		// 枚举中心点i。
		for (i=0; i<s.size(); i++) {
			// XXX 中心可以是s[i]，也可以是s[i]和s[i+1]之间。
			len1 = expandAroundCenter(s, i, i);
			len2 = expandAroundCenter(s, i, i+1); // 因为palindromeLength()会进行判断以避免越界，所以caller可以不判断。
			len = max(len1, len2);
			if (len > ansLen) {
				ansLeft = i-(len-1)/2; // 注意i或i的左边是回文串的中心点，而不是回文串的起点。至于为什么是`len-1`，代入具体值计算一下就得到了。
				ansLen = len;
			}
		}
		return s.substr(ansLeft, ansLen);
    }
	
	// 从中心扩展出去，计算回文串的长度。
	int expandAroundCenter(const string&s, int left, int right) {
		// 注意不能用一个计数器来递增，因为可能初始时`left==right`，这样就需要分两种情况，一种+1，一种+2。
		// XXX 直接在循环结束后用区间端点来算出区间长度即可。
		while (left>=0 && right<s.size() && s[left] == s[right]) {
			left--;
			right++;
		}
		return right-left-1; // 左右开计算区间长度。注意不是左右闭，注意循环退出的条件。
	}
};
```

