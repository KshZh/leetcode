# 59. Spiral Matrix II

> Given a positive integer *n*, generate a square matrix filled with elements from 1 to *n*2 in spiral order.
>
> **Example:**
>
> ```
> Input: 3
> Output:
> [
>  [ 1, 2, 3 ],
>  [ 8, 9, 4 ],
>  [ 7, 6, 5 ]
> ]
> ```

1. Medium，格式化。

```cpp
class Solution {
public:
    vector<vector<int>> generateMatrix(int n) {
        vector<vector<int>> buffer(n, vector<int>(n));
        int r1=0, r2=n-1, c1=0, c2=n-1, k=1;
        while (r1<=r2 && c1<=c2) {
            for (int c=c1; c<=c2; c++) buffer[r1][c] = k++;
            for (int r=r1+1; r<=r2; r++) buffer[r][c2] = k++;
            if (r1<r2 && c1<c2) { // 若是“一维”的情况(r1==r2 || c1==c2)，则不需要绕圈。
                // 注意不要写成`c>0`了。
                for (int c=c2-1; c>c1; c--) buffer[r2][c] = k++;
                for (int r=r2; r>r1; r--) buffer[r][c1] = k++;
            }
            r1++, r2--, c1++, c2--;
        }
        return buffer;
    }
};
```

