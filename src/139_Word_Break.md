# 139. Word Break

> Given a **non-empty** string *s* and a dictionary *wordDict* containing a list of **non-empty** words, determine if *s* can be segmented into a space-separated sequence of one or more dictionary words.
>
> **Note:**
>
> - The same word in the dictionary may be reused multiple times in the segmentation.
> - You may assume the dictionary does not contain duplicate words.
>
> **Example 1:**
>
> ```
> Input: s = "leetcode", wordDict = ["leet", "code"]
> Output: true
> Explanation: Return true because "leetcode" can be segmented as "leet code".
> ```
>
> **Example 2:**
>
> ```
> Input: s = "applepenapple", wordDict = ["apple", "pen"]
> Output: true
> Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
>              Note that you are allowed to reuse a dictionary word.
> ```
>
> **Example 3:**
>
> ```
> Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
> Output: false
> ```

1. Medium，DP。
2. 对字典树的查找是O(N)，其中N是字符串集合中最长的字符串的长度。以空间换时间，适用于字符串集合很大且很频繁地在集合中查找某个字符串的情况。

```cpp
// O(N^3)
class Solution {
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        vector<bool> dp(s.size()+1, false); // dp[i]表示s[0:i)是否可被wordDict中的单词恰好分割。
        dp[0] = true; // 边界。
        int i, j;
        for (i=1; i<=s.size(); i++) {
            for (j=0; j<i; j++) {
                if (dp[j] && find(wordDict.begin(), wordDict.end(), s.substr(j, i-j)) != wordDict.end()) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[s.size()];
    }
};
```

```cpp
// O(N^2)
// 对字典树的查找是O(N)，其中N是字符串集合中最长的字符串的长度。以空间换时间，适用于字符串集合很大且很频繁地在集合中查找某个字符串的情况。
class Solution {
    struct TrieNode {
        bool isWord;
        vector<TrieNode*> branches;
        TrieNode(): branches(126, nullptr), isWord(false) {}
    };
    
    // O(N)
    void insertWord(const string& word, TrieNode* node) {
        for (char c: word) {
            if (node->branches[c] == nullptr)
                node->branches[c] = new TrieNode();
            node = node->branches[c];
        }
        node->isWord = true;
    }
public:
    bool wordBreak(string s, vector<string>& wordDict) {
        auto n = s.size();
        vector<bool> dp(n+1, false); // dp[i]表示s[i:n)是否可被wordDict中的单词恰好分割。
        dp[n] = true; // 边界。
        TrieNode root, *curr;
        for (const string& word: wordDict)
            insertWord(word, &root);
        int i, j;
        for (i=n-1; i>=0; i--) {
            curr = &root;
            // 尝试在字符串集合wordDict中查找s[j:]是否存在。
            for (j=i; curr && j<n; j++) {
                curr = curr->branches[s[j]];
                if (curr!=nullptr && curr->isWord && dp[j+1]) {
                    dp[i] = true;
                    break;
                }
            }
        }
        return dp[0];
    }
};
```



