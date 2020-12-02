# 820. Short Encoding of Words

> Given a list of words, we may encode it by writing a reference string `S` and a list of indexes `A`.
>
> For example, if the list of words is `["time", "me", "bell"]`, we can write it as `S = "time#bell#"` and `indexes = [0, 2, 5]`.
>
> Then for each index, we will recover the word by reading from the reference string from that index until we reach a `"#"` character.
>
> What is the length of the shortest reference string S possible that encodes the given words?
>
> **Example:**
>
> ```
> Input: words = ["time", "me", "bell"]
> Output: 10
> Explanation: S = "time#bell#" and indexes = [0, 2, 5].
> ```

1. Medium。
2. 从题目可以看出，如果一个单词是另一个单词的后缀，那么这个单词就可以忽略。换个角度，也就是另一个更长的单词把与其后缀相同的单词删掉了。所以一个思路就是遍历每个单词，从容器中试图删去该单词的后缀词。
3. 字典树。

```cpp
// 时间复杂度O(NK^2)，空间复杂度O(NK)
class Solution {
public:
    int minimumLengthEncoding(vector<string>& words) {
        unordered_set<string> s(words.begin(), words.end());
        for (auto& word: words) { // O(N)。
            for (int i=1; i<word.size(); i++) { // O(K)，每次循环需要复制一个string。
                s.erase(word.substr(i)); // substr()需要O(K)。
            }
        }
        int n = 0;
        for (auto& word: s)
            n += word.size() + 1;
        return n;
    }
};
```

```cpp
struct TrieNode {
    vector<TrieNode*> branches;
    int count;
    TrieNode(): branches(26, nullptr), count(0) {}
    TrieNode* get(char c) {
        if (branches[c-'a'] == nullptr) {
            branches[c-'a'] = new TrieNode();
            count++;
        }
        return branches[c-'a'];
    }
};

class Solution {
public:
    int minimumLengthEncoding(vector<string>& words) {
        // 字典树中的一条边表示一个字符，单词words[i]从根出发，
        // 到达该单词的终点结点，m的键就是该终点结点的地址。
        unordered_map<TrieNode*, int> m;
        TrieNode root;
        TrieNode* curr;
        int i, j;
        for (i=0; i<words.size(); i++) {
            curr = &root;
            for (j=words[i].size()-1; j>=0; j--) { // 后缀。
                curr = curr->get(words[i][j]);
            }
            m[curr] = i;
        }
        int n = 0;
        for (const auto& p: m) {
            // 只有终点是叶子结点的单词，才需要考虑。
            // 如果终点不是叶子结点，那么该单词就是其它单词的后缀，忽略即可。
            if (p.first->count == 0)
                n += words[p.second].size() + 1;
        }
        return n;
    }
};
```

