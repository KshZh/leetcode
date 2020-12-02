# 140. Word Break II

> Given a **non-empty** string *s* and a dictionary *wordDict* containing a list of **non-empty** words, add spaces in *s* to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.
>
> **Note:**
>
> - The same word in the dictionary may be reused multiple times in the segmentation.
> - You may assume the dictionary does not contain duplicate words.
>
> **Example 1:**
>
> ```
> Input:
> s = "catsanddog"
> wordDict = ["cat", "cats", "and", "sand", "dog"]
> Output:
> [
>   "cats and dog",
>   "cat sand dog"
> ]
> ```
>
> **Example 2:**
>
> ```
> Input:
> s = "pineapplepenapple"
> wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
> Output:
> [
>   "pine apple pen apple",
>   "pineapple pen apple",
>   "pine applepen apple"
> ]
> Explanation: Note that you are allowed to reuse a dictionary word.
> ```
>
> **Example 3:**
>
> ```
> Input:
> s = "catsandog"
> wordDict = ["cats", "dog", "sand", "and", "cat"]
> Output:
> []
> ```

1. Hard，DP，回溯。
2. 第一份代码只是回溯，并没有DP。

```cpp
class Solution {
    vector<string> res;
    vector<string> temp;
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        dfs(s, 0, wordDict);
        return res;
    }
    
    void dfs(const string& s, int idx, const vector<string>& wordDict) {
        if (idx == s.size()) {
            if (!temp.empty()) {
                string x = temp[0];
                for (int i=1; i<temp.size(); i++)
                    x += " " + temp[i];
                res.push_back(x);
            }
            return;
        }
        for (const string& word: wordDict) {
            if (word.size() <= s.size()-idx) { // 右开减左闭等于区间长度。
                int i;
                for (i=0; i<word.size() && word[i]==s[idx+i]; i++)
                    ;
                if (i == word.size()) {
                    temp.push_back(word);
                    dfs(s, idx+i, wordDict);
                    temp.pop_back();
                }
            }
        }
    }
};
```

```cpp
class Solution {
    unordered_map<string, vector<string>> m;

    vector<string> combine(string word, vector<string> prev){
        for(int i=0; i<prev.size(); ++i){
            prev[i] += " "+word;
        }
        return prev;
    }
public:
    vector<string> wordBreak(string s, vector<string>& wordDict) {
        if (m.find(s) != m.end()) return m[s];
        vector<string> result;
        if (find(wordDict.begin(), wordDict.end(), s) != wordDict.end()) {
            result.push_back(s);
        }
        for (int i=1; i<s.size(); ++i){
            string word = s.substr(i);
            if (find(wordDict.begin(), wordDict.end(), word) != wordDict.end()) {
                string remain = s.substr(0,i);
                vector<string> prev = combine(word, wordBreak(remain, wordDict));
                result.insert(result.end(), prev.begin(), prev.end());
            }
        }
        m[s] = result; // memorize
        return result;
    }
};
```

