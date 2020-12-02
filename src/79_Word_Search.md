# 79. Word Search

> Given a 2D board and a word, find if the word exists in the grid.
>
> The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
>
> **Example:**
>
> ```
> board =
> [
>   ['A','B','C','E'],
>   ['S','F','C','S'],
>   ['A','D','E','E']
> ]
> 
> Given word = "ABCCED", return true.
> Given word = "SEE", return true.
> Given word = "ABCB", return false.
> ```

1. Medium。

```cpp
// 搜索题要注意不要走回头路和绕圈。
class Solution {
    private int[] d = {0, 1, 0, -1, 0};
    private boolean[][] visited;
    // 为了过下面这样的测试，不要走回头路。
    // [["a","a"]]
    // "aaa"
    
    public boolean exist(char[][] board, String word) {
        visited = new boolean[board.length][board[0].length];
        for (int i=0; i<board.length; i++) {
            for (int j=0; j<board[0].length; j++) {
                if (board[i][j] == word.charAt(0)) { // 可以调用前检查，也可以调用后再检查。
                    visited[i][j] = true;
                    // 实参wpos为1，因为word[0]已经在这里检查了。
                    if (dfs(board, word, i, j, 1))
                        return true;
                    visited[i][j] = false;
                }
            }
        }
        return false;
    }
    
    private boolean dfs(char[][] board, String word, int i, int j, int wpos) {
        if (wpos == word.length()) return true; // 合法路径，在矩阵中找到了word。
        int x, y;
        char c;
        for (int k=0; k<4; k++) {
            x = i+d[k];
            y = j+d[k+1];
            if (x<0 || x>=board.length || y<0 || y>=board[0].length) continue;
            if (!visited[x][y] && board[x][y] == word.charAt(wpos)) {
                visited[x][y] = true;
                if (dfs(board, word, x, y, wpos+1))
                    return true;
                visited[x][y] = false;
            }
        }
        return false;
    }
}
```

```cpp
// 简洁一些的代码。
public boolean exist(char[][] board, String word) {
    char[] w = word.toCharArray();
    for (int y=0; y<board.length; y++) {
    	for (int x=0; x<board[y].length; x++) {
    		if (exist(board, y, x, w, 0)) return true;
    	}
    }
    return false;
}

private boolean exist(char[][] board, int y, int x, char[] word, int i) {
    // 统一调用后再检查，就可以使得调用方比较容易使用搜索。
	if (i == word.length) return true;
	if (y<0 || x<0 || y == board.length || x == board[y].length) return false;
	if (board[y][x] != word[i]) return false;
	board[y][x] ^= 256;
	boolean exist = exist(board, y, x+1, word, i+1)
		|| exist(board, y, x-1, word, i+1)
		|| exist(board, y+1, x, word, i+1)
		|| exist(board, y-1, x, word, i+1);
	board[y][x] ^= 256;
	return exist;
}
```

