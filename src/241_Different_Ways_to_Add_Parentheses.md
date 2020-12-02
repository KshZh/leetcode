# 241. Different Ways to Add Parentheses

> Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators. The valid operators are `+`, `-` and `*`.
>
> **Example 1:**
>
> ```
> Input: "2-1-1"
> Output: [0, 2]
> Explanation: 
> ((2-1)-1) = 0 
> (2-(1-1)) = 2
> ```
>
> **Example 2:**
>
> ```
> Input: "2*3-4*5"
> Output: [-34, -14, -10, -10, 10]
> Explanation: 
> (2*(3-(4*5))) = -34 
> ((2*3)-(4*5)) = -14 
> ((2*(3-4))*5) = -10 
> (2*((3-4)*5)) = -10 
> (((2*3)-4)*5) = 10
> ```

1. Meidum，分治策略。

```cpp
// 可以考虑用一个缓存，缓存的key可以是子字符串，也可以是begin*input.size()+end。
class Solution {
    unordered_map<char, function<int(int, int)>> f{
        {'+', [](int a, int b){ return a+b; }},
        {'-', [](int a, int b){ return a-b; }},
        {'*', [](int a, int b){ return a*b; }},
        {'/', [](int a, int b){ return a/b; }},
    };
public:
    vector<int> diffWaysToCompute(string input) {
        vector<int> res;
        return dv(input, 0, input.size());
    }
    
    vector<int> dv(string& input, int begin, int end) {
        vector<int> res;
        int num = 0;
        for (int i=begin; i<end; i++) {
            if (input[i]=='+' || input[i]=='-' || input[i]=='*' || input[i]=='/') {
                vector<int> v1 = dv(input, begin, i);
                vector<int> v2 = dv(input, i+1, end);
                for (int x1: v1) {
                    for (int x2: v2) {
                        res.push_back(f[input[i]](x1, x2));
                    }
                }
            } else {
                num = num*10+(input[i]-'0');
            }
        }
        if (res.empty())
            res.push_back(num);
        return res;
    }
};
```

