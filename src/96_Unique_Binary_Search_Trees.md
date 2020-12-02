# 96. Unique Binary Search Trees

> Given *n*, how many structurally unique **BST's** (binary search trees) that store values 1 ... *n*?
>
> **Example:**
>
> ```
> Input: 3
> Output: 5
> Explanation:
> Given n = 3, there are a total of 5 unique BST's:
> 
>    1         3     3      2      1
>     \       /     /      / \      \
>      3     2     1      1   3      2
>     /     /       \                 \
>    2     1         2                 3
> ```

1. Medium，dp。

```cpp
/*
https://leetcode.com/problems/unique-binary-search-trees/discuss/31666/DP-Solution-in-6-lines-with-explanation.-F(i-n)-G(i-1)-*-G(n-i)

Hope it will help you to understand :
    
    n = 0;     null   
    
    count[0] = 1
    
    
    n = 1;      1       
    
    count[1] = 1 
    
    
    n = 2;    1__       			 __2     
    		      \					/                 
    		     count[1]	   	count[1]	
    
    count[2] = 1 + 1 = 2
    
    
    
    n = 3;    1__				      __2__	                   __3
    		      \		            /       \			      /		
    		  count[2]		  count[1]    count[1]		count[2]
    
    count[3] = 2 + 1 + 2  = 5
    
    
    
    n = 4;    1__  					__2__					   ___3___                  
    		      \				 /        \					  /		  \			
    		  count[3]		 count[1]    count[2]		  count[2]   count[1]
    
                 __4				
               /
           count[3]   
    
    count[4] = 5 + 2 + 2 + 5 = 14
    
    
    
    n = 5;    1__  					__2__					   ___3___                  
                 \				 /         \				/	       \			
            count[4]		count[1]      count[3]	    count[2]         count[2]    

                     __4__				__5__
                   /      \            /
            count[3]    count[1]   count[4] 
    
    count[5] = 14 + 5 + 4 + 5 + 14 = 42
    

And  so on...
*/
class Solution {
public:
    int numTrees(int n) {
        vector<int> dp(n+1); // dp[i]表示长度为i的序列可以有多少中唯一的二叉树。
        // 边界。
        dp[0] = dp[1] = 1; // 长度为0的序列只有一棵唯一的空树。
        for (int i=2; i<=n; i++) {
            for (int j=1; j<=i; j++) {
                // 枚举根。
                dp[i] += dp[j-1]*dp[i-j];
            }
        }
        return dp[n];
    }
};
```

