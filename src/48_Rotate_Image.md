# 48. Rotate Image

> You are given an *n* x *n* 2D matrix representing an image.
>
> Rotate the image by 90 degrees (clockwise).
>
> **Note:**
>
> You have to rotate the image [**in-place**](https://en.wikipedia.org/wiki/In-place_algorithm), which means you have to modify the input 2D matrix directly. **DO NOT** allocate another 2D matrix and do the rotation.
>
> **Example 1:**
>
> ```
> Given input matrix = 
> [
>   [1,2,3],
>   [4,5,6],
>   [7,8,9]
> ],
> 
> rotate the input matrix in-place such that it becomes:
> [
>   [7,4,1],
>   [8,5,2],
>   [9,6,3]
> ]
> ```
>
> **Example 2:**
>
> ```
> Given input matrix =
> [
>   [ 5, 1, 9,11],
>   [ 2, 4, 8,10],
>   [13, 3, 6, 7],
>   [15,14,12,16]
> ], 
> 
> rotate the input matrix in-place such that it becomes:
> [
>   [15,13, 2, 5],
>   [14, 3, 4, 1],
>   [12, 6, 8, 9],
>   [16, 7,10,11]
> ]
> ```

1. Medium。

```cpp
/*
 * clockwise rotate
 * first reverse up to down, then swap the symmetry 
 * 1 2 3     7 8 9     7 4 1
 * 4 5 6  => 4 5 6  => 8 5 2
 * 7 8 9     1 2 3     9 6 3
*/
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        std::reverse(matrix.begin(), matrix.end()); // 按行逆序。
        for (int i=0; i<matrix.size(); i++) {
            for (int j=i+1; j<matrix[0].size(); j++) {
                std::swap(matrix[i][j], matrix[j][i]); // 对角线交换。
            }
        }
    }
};
```

```cpp
class Solution {
public:
    void rotate(vector<vector<int>>& matrix) {
        int n = matrix.size();
        int a = 0;
        int b = n-1;
        while(a<b){
            // 下面的for将当前这一圈的元素调整到恰当的位置。
            // 有b-a列就需要调整b-a次，一次调整4个点。
            for(int i=0;i<(b-a);++i){
                // 起点固定在行a，调整一次后从列a往右走，
                // 第二个点固定在列b，调整一次后从行a往下走，
                // 第三个点固定在行b，调整一次后从列b往左走，
                // 第4个点固定在列a，调整一次后从行b往上走。
                // 观察样例可以写出计算下标的表达式。
                swap(matrix[a][a+i], matrix[a+i][b]);
                swap(matrix[a][a+i], matrix[b][b-i]);
                swap(matrix[a][a+i], matrix[b-i][a]);
            }
            ++a; // 缩小这个圈到下一个圈进行调整。
            --b;
        }
    }
};
```



