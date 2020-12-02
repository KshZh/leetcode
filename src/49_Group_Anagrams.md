# 49. Group Anagrams

> Given an array of strings, group anagrams together.
>
> **Example:**
>
> ```
> Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
> Output:
> [
>   ["ate","eat","tea"],
>   ["nat","tan"],
>   ["bat"]
> ]
> ```
>
> **Note:**
>
> - All inputs will be in lowercase.
> - The order of your output does not matter.

1. Medium。

```cpp
// Approach 1: Categorize by Sorted String
// Intuition
// Two strings are anagrams if and only if their sorted strings are equal.
// Time Complexity: O(NKlogK), where NN is the length of strs, and KK is the maximum length of a string in strs. The outer loop has complexity O(N) as we iterate through each string. Then, we sort each string in O(KlogK) time.
// Space Complexity: O(NK), the total information content stored in ans.
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> mp;
        for (string s : strs) {
            string t = s; 
            sort(t.begin(), t.end());
            mp[t].push_back(s);
        }
        vector<vector<string>> anagrams;
        for (auto& p : mp) { 
            anagrams.push_back(move(p.second)); // move，这样不必拷贝堆内存。
        }
        return anagrams;
    }
};
```

```cpp
// Approach 2: Categorize by Count
// Intuition
// Two strings are anagrams if and only if their character counts (respective number of occurrences of each character) are the same.
// Time Complexity: O(NK), where N is the length of strs, and K is the maximum length of a string in strs. Counting each string is linear in the size of the string, and we count every string.
// Space Complexity: O(NK), the total information content stored in ans.
class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        unordered_map<string, vector<string>> mp;
        for (string s : strs) {
            mp[sort(s)].push_back(s);
        }
        vector<vector<string>> anagrams;
        for (auto& p : mp) { 
            anagrams.push_back(move(p.second)); // move，这样不必拷贝堆内存。
        }
        return anagrams;
    }
    
    string sort(string& s) {
        vector<char> ret;
        int cnt[26]{0};
        for (int i=0; i<s.size(); i++)
            cnt[s[i]-'a']++;
        for (int i=0; i<26; i++) {
            while (cnt[i]) {
                ret.push_back('0'+cnt[i]%10);
                cnt[i]/=10;
            }
            ret.push_back('#');
        }
        return string(ret.begin(), ret.end());
    }
};
```

