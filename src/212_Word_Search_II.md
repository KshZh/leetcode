# 212. Word Search II

> Given a 2D board and a list of words from the dictionary, find all words in the board.
>
> Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
>
> **Example:**
>
> ```
> Input: 
> board = [
>   ['o','a','a','n'],
>   ['e','t','a','e'],
>   ['i','h','k','r'],
>   ['i','f','l','v']
> ]
> words = ["oath","pea","eat","rain"]
> 
> Output: ["eat","oath"]
> ```
>
> **Note:**
>
> 1. All inputs are consist of lowercase letters `a-z`.
> 2. The values of `words` are distinct.

1. Hard。

```cpp
class Solution {
    struct Node {
        unordered_map<char, Node*> children;
        bool isEnd;
        Node(): isEnd(false) {}
    };
    
    Node root;
    void insert(const string& word) {
        Node* p = &root;
        for (char c: word) {
            if (p->children.find(c-'a') == p->children.end())
                p->children[c-'a'] = new Node();
            p = p->children[c-'a'];
        }
        p->isEnd = true;
    }
    
    size_t m, n;
    vector<char> path;
    unordered_set<string> ret;
    vector<vector<bool>> visited;
    
    int d[5] = {0, 1, 0, -1, 0};
public:
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        if (board.empty()) return {};
        for (string& word: words) {
            insert(word);
        }
        m=board.size(), n=board[0].size();
        visited = vector<vector<bool>>(m, vector<bool>(n));
        for (int i=0; i<m; i++) {
            for (int j=0; j<n; j++) {
                if (root.children.find(board[i][j]-'a') != root.children.end()) {
                    visited[i][j] = true;
                    path.push_back(board[i][j]);
                    dfs(board, i, j, root.children[board[i][j]-'a']);
                    path.pop_back();
                    visited[i][j] = false;
                }
            }
        }
        return vector<string>(ret.begin(), ret.end());
    }
    
    void dfs(vector<vector<char>>& board, int i, int j, Node* p) {
        if (p->isEnd)
            ret.insert(string(path.begin(), path.end()));
        if (p->children.empty())
            return;
        int x, y;
        for (int k=0; k<4; k++) {
            x = i+d[k];
            y = j+d[k+1];
            if (x<0 || x>=m || y<0 || y>=n) continue;
            if (!visited[x][y] && p->children.find(board[x][y]-'a')!=p->children.end()) {
                visited[x][y] = true;
                path.push_back(board[x][y]);
                dfs(board, x, y, p->children[board[x][y]-'a']);
                path.pop_back();
                visited[x][y] = false;
            }
        }
    }
};
```

