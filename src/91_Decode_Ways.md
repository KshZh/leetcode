# 91. Decode Ways

> A message containing letters from `A-Z` is being encoded to numbers using the following mapping:
>
> ```
> 'A' -> 1
> 'B' -> 2
> ...
> 'Z' -> 26
> ```
>
> Given a **non-empty** string containing only digits, determine the total number of ways to decode it.
>
> **Example 1:**
>
> ```
> Input: "12"
> Output: 2
> Explanation: It could be decoded as "AB" (1 2) or "L" (12).
> ```
>
> **Example 2:**
>
> ```
> Input: "226"
> Output: 3
> Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
> ```

1. Medium。

```cpp
// 没有做缓存的搜索，会重复计算子问题。
class Solution {
public:
    int numDecodings(string s) {
        int cnt = 0;
        dfs(s, 0, cnt);
        return cnt;
    }
    
    void dfs(string& s, int i, int& cnt) {
        if (s[i] == '0') return; // 没有字母编码为0，这是一条不合法的路径。
        if (i == s.size()) { // 合法的路径。
            cnt++;
            return;
        }
        dfs(s, i+1, cnt);
        // if (s[i]<='2' && i+1<s.size() && s[i+1]<='6')
        // "17"无法通过该断言。
        if (i+1<s.size() && s[i]*27+s[i+1]<='2'*27+'6')
            dfs(s, i+2, cnt);
    }
};
```

```cpp
// 从问题出发的dp/记忆化搜索，一般这种搜索不要用参数返回值，不好处理。
class Solution {
    unordered_map<int, int> cache;
public:
    int numDecodings(string s) {
        return dfs(s, 0);
    }
    
    int dfs(string& s, int i) {
        if (s[i] == '0') return 0; // 没有字母编码为0，这是一条不合法的路径。
        if (i == s.size()) return 1; // 合法的路径。
        if (cache.find(i) != cache.end()) return cache[i];
        
        int cnt = dfs(s, i+1);
        // if (s[i]<='2' && i+1<s.size() && s[i+1]<='6')
        // "17"无法通过该断言。
        // if (i+1<s.size() && s[i]*27+s[i+1]<='2'*27+'6')  // 最大为26，所以是27进制。
        if (i+1<s.size() && (s[i]=='1' || (s[i]=='2' && s[i+1]<='6'))) // 也可以。
            cnt += dfs(s, i+2);
        
        cache[i] = cnt;
        return cnt;
    }
};
```

```cpp
// 因为一个dp[i]只依赖于前两个dp，那么可以用两个变量，达到常数空间复杂度。
class Solution {
    unordered_map<int, int> cache;
public:
    int numDecodings(string s) {
        auto n = s.size();
        // dp[i]表示s的前i个字符有几种解码组合。
        vector<int> dp(n+1);
        // 边界。
        dp[0] = 1; // 空字符串无法解码。但是……
        dp[1] = s[0]=='0'? 0: 1;
        for (int i=2; i<=n; i++) {
            if (s[i-1] != '0') dp[i]+=dp[i-1]; // 注意前1个字符是s[0]。
            if (s[i-2]=='1' || (s[i-2]=='2' && s[i-1]<='6')) dp[i]+=dp[i-2];
        }
        return dp[n];
    }
};
```

