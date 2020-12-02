# 119. Pascal's Triangle II

> Given a non-negative index *k* where *k* ≤ 33, return the *k*th index row of the Pascal's triangle.
>
> Note that the row index starts from 0.
>
> ![img](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)
> In Pascal's triangle, each number is the sum of the two numbers directly above it.
>
> **Example:**
>
> ```
> Input: 3
> Output: [1,3,3,1]
> ```
>
> **Follow up:**
>
> Could you optimize your algorithm to use only *O*(*k*) extra space?

1. Easy。

```cpp
class Solution {
public:
    vector<int> getRow(int rowIndex) {
        // 如果从第0行开始，那么第i行就有i+1个元素。
        // 使用滚动数组使得不必使用二维数组。
        vector<int> row(rowIndex+1, 1);
        for (int i=0; i<=rowIndex; i++) {
            // 第i行有i+1个元素，最后一个元素下标为i，最后第二个元素下标则为i-1。
            for (int j=i-1; j>0; j--) { // 要逆着来，不然会先覆盖了上一行的旧值。
                row[j] = row[j-1]+row[j]; // 注意赋值表达式中的row是上一行的值。
            }
        }
        return row;
    }
};
```

