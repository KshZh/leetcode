# 208. Implement Trie (Prefix Tree)

> Implement a trie with `insert`, `search`, and `startsWith` methods.
>
> **Example:**
>
> ```
> Trie trie = new Trie();
> 
> trie.insert("apple");
> trie.search("apple");   // returns true
> trie.search("app");     // returns false
> trie.startsWith("app"); // returns true
> trie.insert("app");   
> trie.search("app");     // returns true
> ```
>
> **Note:**
>
> - You may assume that all inputs are consist of lowercase letters `a-z`.
> - All inputs are guaranteed to be non-empty strings.

1. Medium。
2. 使用字典树可以方便地在一个字符串集合中查找是否存在某一个字符串，时间复杂度是O(N)。

> Trie (we pronounce "try") or prefix tree is a tree data structure, which is used for retrieval of a key in a dataset of strings. There are various applications of this very efficient data structure such as :
>
> ##### 1. [Autocomplete](https://en.wikipedia.org/wiki/Autocomplete)
>
> ![Google Suggest](https://leetcode.com/media/original_images/208_GoogleSuggest.png)
>
> *Figure 1. Google Suggest in action.*
>
> ##### 2. [Spell checker](https://en.wikipedia.org/wiki/Spell_checker)
>
> ![Spell Checker](https://leetcode.com/media/original_images/208_SpellCheck.png)
>
> *Figure 2. A spell checker used in word processor.*
>
> ##### 3. [IP routing (Longest prefix matching)](https://en.wikipedia.org/wiki/Longest_prefix_match)
>
> ![IP Routing](https://leetcode.com/media/original_images/208_IPRouting.gif)
>
> *Figure 3. Longest prefix matching algorithm uses Tries in Internet Protocol (IP) routing to select an entry from a forwarding table.*
>
> ##### 4. [T9 predictive text](https://en.wikipedia.org/wiki/T9_(predictive_text))
>
> ![T9 Predictive Text](https://leetcode.com/media/original_images/208_T9.jpg)
>
> *Figure 4. T9 which stands for Text on 9 keys, was used on phones to input texts during the late 1990s.*
>
> ##### 5. [Solving word games](https://en.wikipedia.org/wiki/Boggle)
>
> ![Boggle](https://leetcode.com/media/original_images/208_Boggle.png)
>
> *Figure 5. Tries is used to solve Boggle efficiently by pruning the search space.*
>
> There are several other data structures, like balanced trees and hash tables, which give us the possibility to search for a word in a dataset of strings. Then why do we need trie? Although hash table has O(1)*O*(1) time complexity for looking for a key, it is not efficient in the following operations :
>
> - **Finding all keys with a common prefix.**
> - **Enumerating a dataset of strings in lexicographical order.**（哈希表在这方面的缺点就是字典树的优势）
>
> Another reason why trie outperforms hash table, is that as hash table increases in size, there are lots of hash collisions and the search time complexity could deteriorate to *O*(*n*), where *n* is the number of keys inserted. Trie could use less space compared to Hash Table **when storing many keys with the same prefix**. In this case using trie has only *O*(*m*) time complexity, where m*m* is the key length. Searching for a key in a balanced tree costs *O*(*m*log*n*) time complexity.

```cpp
// 插入和查找的时间空间复杂度都是O(m)，m是key的长度。
class Trie {
    struct Node {
        vector<Node*> children;
        bool isEnd;
        Node(): children(26), isEnd(false) {}
    };
    Node root;
    
    Node* searchPrefix(const string& s) {
        Node* p = &root;
        for (char c: s) {
            if (!p->children[c-'a'])
                return nullptr;
            p = p->children[c-'a'];
        }
        return p;
    }
public:
    /** Initialize your data structure here. */
    Trie() {
        
    }
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        Node* p = &root;
        for (char c: word) {
            if (p->children[c-'a'] == nullptr) {
                p->children[c-'a'] = new Node();
            }
            p = p->children[c-'a'];
        }
        p->isEnd = true;
    }
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        Node* p = searchPrefix(word);
        return p && p->isEnd;
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        return searchPrefix(prefix);
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */
```

