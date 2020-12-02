# 22. Generate Parentheses

> Given *n* pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
>
> For example, given *n* = 3, a solution set is:
>
> ```
> [
>   "((()))",
>   "(()())",
>   "(())()",
>   "()(())",
>   "()()()"
> ]
> ```

1. Meidum，回溯，DP。

```cpp
class Solution {
public:
    vector<string> generateParenthesis(int n) {
        vector<string> ans;
        vector<char> path;
        backtracking(n, n, path, ans);
        return ans;
    }
    
    void backtracking(int numOpenLeft, int numCloseLeft, vector<char>& path, vector<string>& ans) {
        if (numCloseLeft == 0) {
            ans.emplace_back(path.begin(), path.end());
            return;
        }
        if (numOpenLeft > 0) {
            path.push_back('(');
            backtracking(numOpenLeft-1, numCloseLeft, path, ans);
            path.pop_back();
        }
        if (numCloseLeft > numOpenLeft) {
            path.push_back(')');
            backtracking(numOpenLeft, numCloseLeft-1, path, ans);
            path.pop_back();
        }
    }
};
```

```cpp
class Solution {
public:
    vector<string> generateParenthesis(int n) {
        // dp[i]是i对括号的合法组合的集合。
        vector<vector<string>> dp{{""}, {"()"}};
        for (int i=2; i<=n; i++) {
            vector<string> list;
            for (int j=0; j<i; j++) {
                for (string& first: dp[j]) {
                    for (string& second: dp[i-j-1]) {
                        list.push_back("("+first+")"+second);
                    }
                }
            }
            dp.push_back(list);
        }
        return dp.back();
    }
};
```

