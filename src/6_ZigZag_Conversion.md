# 6. ZigZag Conversion

> The string `"PAYPALISHIRING"` is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
>
> ```
> P   A   H   N
> A P L S I I G
> Y   I   R
> ```
>
> And then read line by line: `"PAHNAPLSIIGYIR"`
>
> Write the code that will take a string and make this conversion given a number of rows:
>
> ```
> string convert(string s, int numRows);
> ```
>
> **Example 1:**
>
> ```
> Input: s = "PAYPALISHIRING", numRows = 3
> Output: "PAHNAPLSIIGYIR"
> ```
>
> **Example 2:**
>
> ```
> Input: s = "PAYPALISHIRING", numRows = 4
> Output: "PINALSIGYAHRPI"
> Explanation:
> 
> P     I    N
> A   L S  I G
> Y A   H R
> P     I
> ```

1. Medium，格式化。

2. Visit all characters in row 0 first, then row 1, then row 2, and so on...

   For all whole numbers *k*,

   - Characters in row numRows−1 and 0 are located at indexes *k*(2⋅numRows−2)
   - Characters in inner row i*i* are located at indexes *k*(2⋅numRows−2)+*i* and (*k*+1)(2⋅numRows−2)−*i*.

```cpp
class Solution {
public:
    string convert(string s, int numRows) {
        if (numRows == 1) return s;
        // 注意min的使用，以应对s的长度小于numRows的边界情况。
        vector<string> rows(min(numRows, static_cast<int>(s.size())));
        int curRow = 0;
        bool goingDown = false;
        for (char c: s) {
            rows[curRow] += c;
            if (curRow==0 || curRow==numRows-1) goingDown=!goingDown;
            curRow += goingDown? 1: -1;
        }
        string ans;
        for (string& row: rows)
            ans += row;
        return ans;
    }
};
```

```cpp
// Approach 2: Visit by Row
class Solution {
public:
    string convert(string s, int numRows) {

        if (numRows == 1) return s;

        string ret;
        int n = s.size();
        int cycleLen = 2 * numRows - 2;

        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j + i < n; j += cycleLen) {
                ret += s[j + i];
                if (i != 0 && i != numRows - 1 && j + cycleLen - i < n)
                    ret += s[j + cycleLen - i];
            }
        }
        return ret;
    }
};
```

