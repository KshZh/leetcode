# 17. Letter Combinations of a Phone Number

> Given a string containing digits from `2-9` inclusive, return all possible letter combinations that the number could represent.
>
> A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
>
> ![img](http://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png)
>
> **Example:**
>
> ```
> Input: "23"
> Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
> ```
>
> **Note:**
>
> Although the above answer is in lexicographical order, your answer could be in any order you want.

1. Medium，递归，回溯。

**Complexity Analysis**

- Time complexity : O(3^*N*×4^*M*) where `N` is the number of digits in the input that maps to 3 letters (*e.g.* `2, 3, 4, 5, 6, 8`) and `M` is the number of digits in the input that maps to 4 letters (*e.g.* `7, 9`), and `N+M` is the total number digits in the input.
- Space complexity : O(3^*N*×4^*M*) since one has to keep 3^*N*×4^*M* solutions.

```cpp
class Solution {
    unordered_map<char, string> letters{
        {'2', "abc"},
        {'3', "def"},
        {'4', "ghi"},
        {'5', "jkl"},
        {'6', "mno"},
        {'7', "pqrs"},
        {'8', "tuv"},
        {'9', "wxyz"}
    };
public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) return {};
        vector<string> ans;
        auto temp = letterCombinations(digits.substr(1)); // 从宏观上看待递归函数的输入输出。
        if (temp.empty()) temp = {""};
        for (char letter: letters[digits[0]]) {
            for (const string& s: temp) {
                ans.push_back(letter + s);
            }
        }
        return ans;
    }
};
```

```cpp
class Solution {
    unordered_map<char, string> letters{
        {'2', "abc"},
        {'3', "def"},
        {'4', "ghi"},
        {'5', "jkl"},
        {'6', "mno"},
        {'7', "pqrs"},
        {'8', "tuv"},
        {'9', "wxyz"}
    };
public:
    vector<string> letterCombinations(string digits) {
        if (digits.empty()) return {};
        vector<string> ans;
        vector<char> path;
        dfs(digits, 0, ans, path);
        return ans;
    }
    
    void dfs(const string& digits, int i, vector<string>& ans, vector<char> path) {
        if (i == digits.size()) {
            // 边界。
            string s;
            for (char c: path) s+=c;
            ans.push_back(s);
            return;
        }
        for (char letter: letters[digits[i]]) {
            path.push_back(letter);
            dfs(digits, i+1, ans, path); // `i+1`因为同一个按键不能按两次。
            path.pop_back();
        }
    }
};
```

