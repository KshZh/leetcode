# 179. Largest Number

> Given a list of non negative integers, arrange them such that they form the largest number.
>
> **Example 1:**
>
> ```
> Input: [10,2]
> Output: "210"
> ```
>
> **Example 2:**
>
> ```
> Input: [3,30,34,5,9]
> Output: "9534330"
> ```
>
> **Note:** The result may be very large, so you need to return a string instead of an integer.

1. Medium。

```cpp
class Solution {
public:
    string largestNumber(vector<int>& nums) {
        vector<string> v;
        for (int num: nums) {
            v.push_back(std::to_string(num));
        }
        std::sort(v.begin(), v.end(),
                  [](const string& s1, const string& s2) {
                      return s1+s2>s2+s1;
                  });
        
        // If, after being sorted, the largest number is `0`, the entire number
        // is zero.
        if (v[0] == "0") {
            return "0";
        }
        
        string ret;
        for (string& s: v) {
            ret += s;
        }
        return ret;
    }
};
```

