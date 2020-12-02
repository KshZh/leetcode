# 36. Valid Sudoku

> Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated **according to the following rules**:
>
> 1. Each row must contain the digits `1-9` without repetition.
> 2. Each column must contain the digits `1-9` without repetition.
> 3. Each of the 9 `3x3` sub-boxes of the grid must contain the digits `1-9` without repetition.
>
> ![img](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png)
> A partially filled sudoku which is valid.
>
> The Sudoku board could be partially filled, where empty cells are filled with the character `'.'`.
>
> **Example 1:**
>
> ```
> Input:
> [
>   ["5","3",".",".","7",".",".",".","."],
>   ["6",".",".","1","9","5",".",".","."],
>   [".","9","8",".",".",".",".","6","."],
>   ["8",".",".",".","6",".",".",".","3"],
>   ["4",".",".","8",".","3",".",".","1"],
>   ["7",".",".",".","2",".",".",".","6"],
>   [".","6",".",".",".",".","2","8","."],
>   [".",".",".","4","1","9",".",".","5"],
>   [".",".",".",".","8",".",".","7","9"]
> ]
> Output: true
> ```
>
> **Example 2:**
>
> ```
> Input:
> [
>   ["8","3",".",".","7",".",".",".","."],
>   ["6",".",".","1","9","5",".",".","."],
>   [".","9","8",".",".",".",".","6","."],
>   ["8",".",".",".","6",".",".",".","3"],
>   ["4",".",".","8",".","3",".",".","1"],
>   ["7",".",".",".","2",".",".",".","6"],
>   [".","6",".",".",".",".","2","8","."],
>   [".",".",".","4","1","9",".",".","5"],
>   [".",".",".",".","8",".",".","7","9"]
> ]
> Output: false
> Explanation: Same as Example 1, except with the 5 in the top left corner being 
>     modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
> ```
>
> **Note:**
>
> - A Sudoku board (partially filled) could be valid but is not necessarily solvable.
> - Only the filled cells need to be validated according to the mentioned rules.
> - The given board contain only digits `1-9` and the character `'.'`.
> - The given board size is always `9x9`.

1. Medium。
2. 通过行号i和列号j计算格子下标k：`k=i/3*3+j/3`，一个格子有三行，所以`i/3`得到格子所在的行号（相对格子来说的行），范围是[0, 2]，因为一行（相对格子来说的行）有三个格子，故再`*3`，跑到格子所在的那一行。因为一个格子有三列，所以`j/3`，得到格子所在的列号，相加得到格子所在的下标。

```cpp
class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        // 多用几个容器，这样就能在一次双层遍历中检查三个维度了。
        // 如果每次只用一个容器，就得三次双层遍历。
        bool used1[9][9]={false}, used2[9][9]={false}, used3[9][9]={false};
        // 遍历每一个格子。
        for (int i=0; i<9; i++) {
            for (int j=0; j<9; j++) {
                if (board[i][j] == '.')
                    continue;
                int num=board[i][j]-'0'-1, k=i/3*3+j/3; // k是格子的下标，范围是[0, 8]。
                if (used1[i][num] || used2[j][num] || used3[k][num])
                    return false;
                used1[i][num] = used2[j][num] = used3[k][num] = true;
                // 表示i行有一个num，j列有一个num，格子k中有一个num，
                // 那么如果遍历到i行、j列、格子k再有一个num，说明这不可能是一个合法的数独。
            }
        }
        return true;
    }
};
```

