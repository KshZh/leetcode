# 885. Spiral Matrix III

> **Example 1:**
>
> ```
> Input: R = 1, C = 4, r0 = 0, c0 = 0
> Output: [[0,0],[0,1],[0,2],[0,3]]
> ```
>
>  ![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/24/example_1.png)
>
> **Example 2:**
>
> ```
> Input: R = 5, C = 6, r0 = 1, c0 = 4
> Output: [[1,4],[1,5],[2,5],[2,4],[2,3],[1,3],[0,3],[0,4],[0,5],[3,5],[3,4],[3,3],[3,2],[2,2],[1,2],[0,2],[4,5],[4,4],[4,3],[4,2],[4,1],[3,1],[2,1],[1,1],[0,1],[4,0],[3,0],[2,0],[1,0],[0,0]]
> ```
>
> ![](https://s3-lc-upload.s3.amazonaws.com/uploads/2018/08/24/example_2.png)

1. 格式化，Medium。
2. [1,1,2,2,3,3 Steps](https://leetcode.com/problems/spiral-matrix-iii/discuss/158970/C%2B%2BJavaPython-112233-Steps)

```cpp
class Solution {
public:
    vector<vector<int>> spiralMatrixIII(int R, int C, int r, int c) {
        vector<vector<int>> res = {{r, c}};
        int dx = 0, dy = 1, tmp;
        for (int n = 0; res.size() < R * C; n++) {
            for (int i = 0; i < n / 2 + 1; i++) {
                r += dx, c += dy;
                if (0 <= r && r < R && 0 <= c && c < C)
                    res.push_back({r, c});
            }
            tmp = dx, dx = dy, dy = -tmp;
        }
        return res;
    }
};
```

