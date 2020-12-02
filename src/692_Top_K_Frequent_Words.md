# 692. Top K Frequent Words

> Given a non-empty list of words, return the *k* most frequent elements.
>
> Your answer should be sorted by frequency from highest to lowest. If two words have the same frequency, then the word with the lower alphabetical order comes first.
>
> **Example 1:**
>
> ```
> Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
> Output: ["i", "love"]
> Explanation: "i" and "love" are the two most frequent words.
>     Note that "i" comes before "love" due to a lower alphabetical order.
> ```
>
> **Example 2:**
>
> ```
> Input: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
> Output: ["the", "is", "sunny", "day"]
> Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
>     with the number of occurrence being 4, 3, 2 and 1 respectively.
> ```
>
> **Note:**
>
> 1. You may assume *k* is always valid, 1 ≤ *k* ≤ number of unique elements.
> 2. Input words contain only lowercase letters.
>
> **Follow up:**
>
> 1. Try to solve it in *O*(*n* log *k*) time and *O*(*n*) extra space.

1. Medium。
2. 类似题目[347. Top K Frequent Elements](./347_Top_K_Frequent_Elements.md)。

```cpp
// 也可以用哈希表统计完后，存到数组中来排序，取前k个。
auto cmp = [](pair<string, int>& a, pair<string, int>& b) {
    if (a.second == b.second) return a.first<b.first; // 字典序大的先输出，之后逆序。
    return a.second>b.second; // 淘汰频率小的。
};

class Solution {
public:
    vector<string> topKFrequent(vector<string>& words, int k) {
        unordered_map<string, int> frequency;
        for (string& word: words) frequency[word]++;
        priority_queue<pair<string, int>, vector<pair<string, int>>, decltype(cmp)> q(cmp);
        for (auto& p: frequency) {
            q.push(p);
            if (q.size() > k)
                q.pop();
        }
        vector<string> ans(k);
        for (int i=0; i<k; i++) {
            ans[i] = q.top().first;
            q.pop();
        }
        reverse(ans.begin(), ans.end());
        return ans;
    }
};
```

