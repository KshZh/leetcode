# 1451. Rearrange Words in a Sentence

> Given a sentence `text` (A *sentence* is a string of space-separated words) in the following format:
>
> - First letter is in upper case.
> - Each word in `text` are separated by a single space.
>
> Your task is to rearrange the words in text such that all words are rearranged in an increasing order of their lengths. If two words have the same length, arrange them in their original order.
>
> Return the new text following the format shown above.
>
> 
>
> **Example 1:**
>
> ```
> Input: text = "Leetcode is cool"
> Output: "Is cool leetcode"
> Explanation: There are 3 words, "Leetcode" of length 8, "is" of length 2 and "cool" of length 4.
> Output is ordered by length and the new first word starts with capital letter.
> ```
>
> **Example 2:**
>
> ```
> Input: text = "Keep calm and code on"
> Output: "On and keep calm code"
> Explanation: Output is ordered as follows:
> "On" 2 letters.
> "and" 3 letters.
> "keep" 4 letters in case of tie order by position in original text.
> "calm" 4 letters.
> "code" 4 letters.
> ```

```cpp
class Solution {
public:
    string arrangeWords(string text) {
        text[0] += ('a'-'A');
        istringstream in(text);
        vector<string> v;
        string s;
        while (in >> s) {
            v.push_back(std::move(s));
        }
        // 如果长度相等，保持原顺序。
        // 可以直接用cpp的std::stable_sort。
        std::stable_sort(v.begin(), v.end(), [](const string& a, const string& b){
            return a.size() < b.size();
        });
        string res(v.front());
        for (int i=1; i<v.size(); i++) {
            res += " " + v[i];
        }
        res[0] -= ('a'-'A');
        return res;
    }
};
```

```java
class Solution {
    public String arrangeWords(String text) {
        String[] words = text.toLowerCase().split(" ");
        int n = words.length;
        Integer[] idx = new Integer[n];
        int[] len = new int[n];
        for (int i=0; i<n; i++) {
            idx[i] = i;
            len[i] = words[i].length();
        }
        // 对下标根据单词长度做排序。如果单词长度相等，则下标相对顺序保持不变。
        Arrays.sort(idx, (Integer a, Integer b)->{ // 不允许int，必须是类。
           if (len[a] == len[b])
               // 若a-b<=0，说明a<=b，则a排前面，否则a排后面。
               // 若写成b-a，则若b-a<=0，但在外部看来，是第一个参数a-b<=0，即a<=b，会把a排前面，即虽然a较大，但a排前面，从而构成降序。
               // 只需记住升序就第一个参数减第二个参数，降序反过来即可。
               return a-b;
            return len[a]-len[b];
        });
        StringBuilder sb = new StringBuilder();
        for (int i=0; i<n; i++) {
            sb.append(words[idx[i]]).append(" ");
        }
        sb.deleteCharAt(sb.length()-1);
        sb.setCharAt(0, Character.toUpperCase(sb.charAt(0)));
        return sb.toString();
    }
}
```

```java
public String arrangeWords(String text) {
    String []s = text.toLowerCase().split(" ");
    Arrays.sort(s, (a,b) ->  a.length() - b.length()); // 如果返回0，表示两个元素相等，则保持相对顺序不变。
    String ans = String.join(" ", s);
    return Character.toUpperCase(ans.charAt(0)) + ans.substring(1);
}
```

