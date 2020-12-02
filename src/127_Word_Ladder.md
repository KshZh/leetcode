# 127. Word Ladder

> Given two words (*beginWord* and *endWord*), and a dictionary's word list, find the length of shortest transformation sequence from *beginWord* to *endWord*, such that:
>
> 1. Only one letter can be changed at a time.
> 2. Each transformed word must exist in the word list. Note that *beginWord* is *not* a transformed word.
>
> **Note:**
>
> - Return 0 if there is no such transformation sequence.
> - All words have the same length.
> - All words contain only lowercase alphabetic characters.
> - You may assume no duplicates in the word list.
> - You may assume *beginWord* and *endWord* are non-empty and are not the same.
>
> **Example 1:**
>
> ```
> Input:
> beginWord = "hit",
> endWord = "cog",
> wordList = ["hot","dot","dog","lot","log","cog"]
> 
> Output: 5
> 
> Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
> return its length 5.
> ```
>
> **Example 2:**
>
> ```
> Input:
> beginWord = "hit"
> endWord = "cog"
> wordList = ["hot","dot","dog","lot","log"]
> 
> Output: 0
> 
> Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
> ```

1. Medium。
2. 典型多路径搜索问题。多路径搜索，如果只是用嵌套循环的话，难以实现，但是如果把问题建模成树或图，然后用dfs/bfs进行搜索，这种思路往往更容易实现。
3. 即时计算邻接结点。

```cpp
class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        if (find(wordList.begin(), wordList.end(), endWord) == wordList.end())
            return 0;
        queue<int> q; // 存储下标，而不是string，节省空间。
        vector<bool> visited(wordList.size());
        getAdjacent(beginWord, wordList, visited, q);
        int x, last=q.back(), level=1;
        while (!q.empty()) {
            x = q.front();
            q.pop();
            if (wordList[x] == endWord) return level+1;
            getAdjacent(wordList[x], wordList, visited, q);
            if (x == last) {
                level++;
                if (!q.empty()) last=q.back();
            }
        }
        return 0;
    }
    
    void getAdjacent(const string& word, const vector<string>& wordList, vector<bool>& visited, queue<int>& q) {
        int i, j, cnt;
        auto n=wordList.size(), m=word.size();
        for (i=0; i<n; i++) {
            if (visited[i]) continue; // 避免走回头路/绕圈。
            if (wordList[i].size() == m) {
                for (j=cnt=0; cnt<=1 && j<m; j++) {
                    if (wordList[i][j] != word[j])
                        cnt++;
                }
                if (cnt <= 1) { // 若等于0，则这是在第一次调用的情况下，beginWord在WordList中。
                    q.push(i);
                    visited[i] = true;
                }
            }
        }
    }
};
```

