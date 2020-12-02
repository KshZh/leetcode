# 566. Reshape the Matrix

> **Example 1:**
>
> ```
> Input: 
> nums = 
> [[1,2],
>  [3,4]]
> r = 1, c = 4
> Output: 
> [[1,2,3,4]]
> Explanation:The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.
> ```

1. Easy。
2. **M\[i\]\[j\]=M\[n\*i+j\] , where n is the number of cols. This is the one way of converting 2-d indices into one 1-d index.**
3. **Try to use division and modulus to convert 1-d index into 2-d indices**.

```cpp
class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& nums, int r, int c) {
        auto originR = nums.size();
        auto originC = nums[0].size();
        if (r*c != originR*originC)
            return nums;
        int i, j, rp=0, cp=0;
        vector<vector<int>> res(r);
        for (i=0; i<r; i++) {
            res[i].resize(c);
            for (j=0; j<c; j++) {
                res[i][j] = nums[rp][cp++];
                if (cp == originC) {
                    rp++;
                    cp = 0;
                }
            }
        }
        return res;
    }
};
```

```cpp
class Solution {
public:
    vector<vector<int>> matrixReshape(vector<vector<int>>& nums, int r, int c) {
        auto originR = nums.size();
        auto originC = nums[0].size();
        if (r*c != originR*originC)
            return nums;
        int i, j, count=0;
        vector<vector<int>> res(r);
        for (i=0; i<r; i++) {
            res[i].resize(c);
            for (j=0; j<c; j++) {
                res[i][j] = nums[count/originC][count%originC]; // 除法和模运算。
                count++;
            }
        }
        return res;
    }
};
```

