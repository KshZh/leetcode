# 118. Pascal's Triangle

> Given a non-negative integer *numRows*, generate the first *numRows* of Pascal's triangle.
>
> ![img](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)
> In Pascal's triangle, each number is the sum of the two numbers directly above it.
>
> **Example:**
>
> ```
> Input: 5
> Output:
> [
>      [1],
>     [1,1],
>    [1,2,1],
>   [1,3,3,1],
>  [1,4,6,4,1]
> ]
> ```

1. Easy。

```cpp
class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        if (numRows == 0) return {};
        vector<vector<int>> ans{{1}};
        for (int i=1; i<numRows; i++) {
            vector<int> v(i+1, 1);
            for (int j=1; j<i; j++)
                v[j] = ans.back()[j-1] + ans.back()[j];
            ans.push_back(move(v));
        }
        return ans;
    }
};
```

