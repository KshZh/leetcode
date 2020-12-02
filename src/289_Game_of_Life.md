# 289. Game of Life

> According to the [Wikipedia's article](https://en.wikipedia.org/wiki/Conway's_Game_of_Life): "The **Game of Life**, also known simply as **Life**, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
>
> Given a *board* with *m* by *n* cells, each cell has an initial state *live* (1) or *dead* (0). Each cell interacts with its [eight neighbors](https://en.wikipedia.org/wiki/Moore_neighborhood) (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):
>
> 1. Any live cell with fewer than two live neighbors dies, as if caused by under-population.
> 2. Any live cell with two or three live neighbors lives on to the next generation.
> 3. Any live cell with more than three live neighbors dies, as if by over-population..
> 4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
>
> Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.
>
> **Example:**
>
> ```
> Input: 
> [
>   [0,1,0],
>   [0,0,1],
>   [1,1,1],
>   [0,0,0]
> ]
> Output: 
> [
>   [0,0,0],
>   [1,0,1],
>   [0,1,1],
>   [0,1,0]
> ]
> ```
>
> **Follow up**:
>
> 1. Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
> 2. In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?

1. Medium。

#### Follow up 2 : Infinite Board

If the board becomes infinitely large, there are multiple problems our current solution would run into:

1. It would be computationally impossible to iterate a matrix that large.
2. It would not be possible to store that big a matrix entirely in memory. We have huge memory capacities these days i.e. of the order of hundreds of GBs. However, it still wouldn't be enough to store such a large matrix in memory.
3. We would be wasting a lot of space if such a huge board only has a few live cells and the rest of them are all dead. In such a case, we have an extremely sparse matrix and it wouldn't make sense to save the board as a "matrix".

Such open ended problems are better suited to design discussions during programming interviews and it's a good habit to take into consideration the scalability aspect of the problem since your interviewer might be interested in talking about such problems. The discussion section already does a great job at addressing this specific portion of the problem. We will briefly go over two different solutions that have been provided in the discussion sections, as they broadly cover two main scenarios of this problem.

One aspect of the problem is addressed by a great solution provided by [Stefan Pochmann](https://leetcode.com/stefanpochmann/). So as mentioned before, it's quite possible that we have a gigantic matrix with a very few live cells. In that case it would be stupidity to save the entire board as is.

> If we have an extremely sparse matrix, it would make much more sense to actually save the location of only the live cells and then apply the 4 rules accordingly using only these live cells.（如果对稀疏矩阵还是遍历每个cell，然后对每个cell遍历器周边，这样多了很多无意义的计数。而用这里的策略，则当矩阵稀疏时，计算量少，稠密时，计算量差不多）

```python
def gameOfLifeInfinite(self, live):
    # 注意这里计数的角度，后面的解法是遍历每个cell，然后遍历该cell的周边来计数该cell周边的1的个数；而这里是遍历每个为1的cell，然后增加其周边的cell的“周边为1的cell的个数的计数器”。
    ctr = collections.Counter((I, J)
                              for i, j in live
                              for I in range(i-1, i+2)
                              for J in range(j-1, j+2)
                              if I != i or J != j)
    return {ij
            for ij in ctr
            if ctr[ij] == 3 or ctr[ij] == 2 and ij in live} # 注意这里并没有排除超出矩阵大小的位置。
			# 注意and的优先级高于or。根据规则，如果一个cell周边有恰好3个为1，那么该cell无论原来是1还是0，都该变为1；若周边恰好有2个1，且该cell原本是1，则保持为1。

def gameOfLife(self, board):
    live = {(i, j) for i, row in enumerate(board) for j, live in enumerate(row) if live} # 这里live存储矩阵中为1的cell的位置。
    live = self.gameOfLifeInfinite(live) # 这里live存储矩阵在应用规则后，为1的cell的位置。
    for i, row in enumerate(board):
        for j in range(len(row)):
            row[j] = int((i, j) in live) # 由于这种遍历方式，所以不会使用到live中超出矩阵大小的位置。
```

The only problem with this solution would be when the entire board cannot fit into memory. If that is indeed the case, then we would have to approach this problem in a different way. For that scenario, we assume that the contents of the matrix are stored in a file, one row at a time.

> In order for us to update a particular cell, we only have to look at its 8 neighbors which essentially lie in the row above and below it. So, for updating the cells of a row, we just need the row above and the row below. Thus, we read one row at a time from the file and at max we will have 3 rows in memory. We will keep discarding rows that are processed and then we will keep reading new rows from the file, one at a time.

[@beagle's](https://leetcode.com/beagle/) solution revolves around this idea and you can refer to the code in the [discussion section](https://leetcode.com/problems/game-of-life/discuss/73217/Infinite-board-solution/201780) for the same. 

```python
#Game of Life
from copy import deepcopy

def findLives(live):
    count = collections.Counter()
    for i, j in live:
        for x in range(i-1, i+2):
            for y in range(j-1, j+2):
                if x == i and y == j: 
                    continue
                count[x, y] += 1
    result = {}
    for i, j in count:
        if count[i, j] == 3:
            result.add((i, j))
        elif count[i, j] == 2 and (i, j) in live:
            result.add((i, j))
    return result

def updateBoard(board):
    live = {(i, j) for i, row in enumerate(board) for j, v in enumerate(row) if v == 1}
    live = findLives(live)
    for r, row in enumerate(board):
        for c, v in enumerate(row):
            board[r][c] = int((r, c) in live)
    for row in board:
        print(" ".join(row))
            
with open("input.txt") as f1:
    prev = f1.readline()
    pointer = f1.readline()
    cur = next_ = None
    while pointer:
        if not cur:
            cur = pointer
            pointer = f1.readline()
            continue
        
        if next_ == None:
            next_ = pointer
            pointer = f1.readline()
        if prev == None:
            tmpBoard = [ cur, next_]
            nextStateBoard = updateBoard(tmpBoard)
        else:
            tmpBoard = [deepcopy(prev), cur, next_]
            nextStateBoard =  updateBoard(tmpBoard)
            
        prev = cur
        cur = next_
        next_ = None
```



下面是对问题的一般解法：

```cpp
// 时间和空间复杂度都为O(MN)。
class Solution {
    int neighbors[3] = {0, 1, -1};
public:
    void gameOfLife(vector<vector<int>>& board) {
        if (board.empty()) return;
        auto m=board.size(), n=board[0].size();
        vector<vector<int>> copyBoard(m, vector<int>(n));
        int row, col, i, j, r, c, numLive;
        for (row=0; row<m; row++) {
            for (col=0; col<n; col++) {
                copyBoard[row][col] = board[row][col];
            }
        }
        
        for (row=0; row<m; row++) {
            for (col=0; col<n; col++) {
                numLive = 0;
                
                for (i=0; i<3; i++) {
                    for (j=0; j<3; j++) {
                        if (i==0 && j==0) continue;
                        r = row + neighbors[i];
                        c = col + neighbors[j];
                        if (r>=0 && r<m && c>=0 && c<n && copyBoard[r][c]) {
                            numLive++;
                        }
                    }
                }
                if (copyBoard[row][col] && (numLive<2 || numLive>3))
                    board[row][col] = 0;
                if (!copyBoard[row][col] && numLive==3)
                    board[row][col] = 1;
            }
        }
    }
};
```

```cpp
// O(1)空间复杂度。
// 对状态转移进行编码。
class Solution {
    int neighbors[3] = {0, 1, -1};
public:
    void gameOfLife(vector<vector<int>>& board) {
        if (board.empty()) return;
        auto m=board.size(), n=board[0].size();
        int row, col, i, j, r, c, numLive;
        
        for (row=0; row<m; row++) {
            for (col=0; col<n; col++) {
                numLive = 0;
                
                for (i=0; i<3; i++) {
                    for (j=0; j<3; j++) {
                        if (i==0 && j==0) continue;
                        r = row + neighbors[i];
                        c = col + neighbors[j];
                        if (r>=0 && r<m && c>=0 && c<n && abs(board[r][c])==1) { // 注意abs，因为原本就是1，就要计数。只是我们用-1表示该cell现在变成了0。
                            numLive++;
                        }
                    }
                }
                if (board[row][col] && (numLive<2 || numLive>3))
                    board[row][col] = -1; // alive -> dead: -1
                if (!board[row][col] && numLive==3)
                    board[row][col] = 2; // dead -> alive: 2
            }
        }

        for (row=0; row<m; row++) {
            for (col=0; col<n; col++) {
                if (board[row][col] == -1) board[row][col] = 0;
                if (board[row][col] == 2) board[row][col] = 1;
            }
        }
    }
};
```

