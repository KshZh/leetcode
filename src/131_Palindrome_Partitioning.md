# 131. Palindrome Partitioning

> Given a string *s*, partition *s* such that every substring of the partition is a palindrome.
>
> Return all possible palindrome partitioning of *s*.
>
> **Example:**
>
> ```
> Input: "aab"
> Output:
> [
>   ["aa","b"],
>   ["a","a","b"]
> ]
> ```

1. Medium，回溯剪枝。

```cpp
class Solution {
public:
    vector<vector<string>> partition(string s) {
        vector<vector<string>> res;
        vector<int> path;
        dfs(s, 0, path, res);
        return res;
    }
    
    void dfs(const string& s, int start, vector<int>& path, vector<vector<string>>& res) {
        if (start == s.size()) {
            vector<string> x;
            for (int i=0; i<path.size()-1; i++) {
                x.push_back(s.substr(path[i], path[i+1]-path[i]));
            }
            x.push_back(s.substr(path.back()));
            res.push_back(move(x));
            return;
        }
        // 遍历s[start, ]所有可能的子串。
        for (int i=start; i<s.size(); i++) {
            if (isPalindrome(s, start, i)) { // 仅当这个子串是回文子串时才进入递归，否则剪掉。
                path.push_back(start);
                dfs(s, i+1, path, res);
                path.pop_back();
            }
        }
    }
    
    bool isPalindrome(const string& s, int i, int j) {
        while (i < j) {
            if (s[i++] != s[j--])
                return false;
        }
        return true;
    }
};
```

