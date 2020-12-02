#  211. Add and Search Word - Data structure design

> Design a data structure that supports the following two operations:
>
> ```
> void addWord(word)
> bool search(word)
> ```
>
> search(word) can search a literal word or a regular expression string containing only letters `a-z` or `.`. A `.` means it can represent any one letter.
>
> **Example:**
>
> ```
> addWord("bad")
> addWord("dad")
> addWord("mad")
> search("pad") -> false
> search("bad") -> true
> search(".ad") -> true
> search("b..") -> true
> ```
>
> **Note:**
> You may assume that all words are consist of lowercase letters `a-z`.

1. Medium。

```cpp
return p->isEnd; // XXX 注意这里不能直接返回true，如果p->isEnd为false，说明这个word只是集合中某个字符串的前缀而已，该集合中并不存在该word。
```

```cpp
class WordDictionary {
    struct Node {
        vector<Node*> children;
        bool isEnd;
        Node(): children(26), isEnd(false) {}
    };
    Node root;
    bool search(const char* word, Node* p) {
        for (int i=0; word[i]; i++) {
            if (word[i] != '.') {
                if (!p->children[word[i]-'a'])
                    return false;
                p = p->children[word[i]-'a'];
            } else {
                for (int j=0; j<26; j++) {
                    if (p->children[j] && search(word+i+1, p->children[j]))
                        return true;
                }
                return false;
            }
        }
        return p->isEnd; // XXX 注意这里不能直接返回true，如果p->isEnd为false，说明这个word只是集合中某个字符串的前缀而已，该集合中并不存在该word。
    }
public:
    /** Initialize your data structure here. */
    WordDictionary() {
        
    }
    
    /** Adds a word into the data structure. */
    void addWord(string word) {
        Node* p = &root;
        for (char c: word) {
            if (p->children[c-'a'] == nullptr) {
                p->children[c-'a'] = new Node();
            }
            p = p->children[c-'a'];
        }
        p->isEnd = true;
    }
    
    /** Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter. */
    bool search(string word) {
        return search(word.c_str(), &root);
    }
};

/**
 * Your WordDictionary object will be instantiated and called as such:
 * WordDictionary* obj = new WordDictionary();
 * obj->addWord(word);
 * bool param_2 = obj->search(word);
 */
```

