# 451. Sort Characters By Frequency

> Given a string, sort it in decreasing order based on the frequency of characters.
>
> **Example 1:**
>
> ```
> Input:
> "tree"
> 
> Output:
> "eert"
> 
> Explanation:
> 'e' appears twice while 'r' and 't' both appear once.
> So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
> ```
>
> **Example 2:**
>
> ```
> Input:
> "cccaaa"
> 
> Output:
> "cccaaa"
> 
> Explanation:
> Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
> Note that "cacaca" is incorrect, as the same characters must be together.
> ```
>
> **Example 3:**
>
> ```
> Input:
> "Aabb"
> 
> Output:
> "bbAa"
> 
> Explanation:
> "bbaA" is also a valid answer, but "Aabb" is incorrect.
> Note that 'A' and 'a' are treated as two different characters.
> ```

1. Medium。

```cpp
class Solution {
public:
    string frequencySort(string s) {
        int counts[256]{0};
        for (char ch : s)
            counts[ch]++;
        sort(s.begin(), s.end(), [&](char a, char b) { 
            return counts[a] > counts[b] || (counts[a] == counts[b] && a < b); 
        });
        return s;
    }
};
```

```cpp
auto cmp = [](pair<char, int>& a, pair<char, int>& b) {
    if (a.second == b.second) return a.first>b.first;
    return a.second<b.second; // 小于，那反过来，大的会先出来。
};

class Solution {
public:
    string frequencySort(string s) {
        unordered_map<char, int> frequency;
        for (char c: s) frequency[c]++;
        priority_queue<pair<char, int>, vector<pair<char, int>>, decltype(cmp)> q(cmp);
        for (auto& p: frequency) {
            q.push(p);
        }
        string ans(s.size(), 0);
        int i=0, j;
        while (!q.empty()) {
            for (j=0; j<q.top().second; j++)
                ans[i++] = q.top().first;
            q.pop();
        }
        return ans;
    }
};
```

