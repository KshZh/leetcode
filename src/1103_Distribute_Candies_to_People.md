# 1103. Distribute Candies to People

> **Example 1:**
>
> ```
> Input: candies = 7, num_people = 4
> Output: [1,2,3,1]
> Explanation:
> On the first turn, ans[0] += 1, and the array is [1,0,0,0].
> On the second turn, ans[1] += 2, and the array is [1,2,0,0].
> On the third turn, ans[2] += 3, and the array is [1,2,3,0].
> On the fourth turn, ans[3] += 1 (because there is only one candy left), and the final array is [1,2,3,1].
> ```
>
> **Example 2:**
>
> ```
> Input: candies = 10, num_people = 3
> Output: [5,2,3]
> Explanation: 
> On the first turn, ans[0] += 1, and the array is [1,0,0].
> On the second turn, ans[1] += 2, and the array is [1,2,0].
> On the third turn, ans[2] += 3, and the array is [1,2,3].
> On the fourth turn, ans[0] += 4, and the final array is [5,2,3].
> ```

1. Easy。
2. 通过模运算绕圈。

```cpp
class Solution {
public:
    vector<int> distributeCandies(int candies, int num_people) {
        int given = 1, i=0, actual;
        vector<int> ans(num_people);
        while (candies) { // 直到糖果全分完。
            actual = min(given, candies);
            ans[i++] += actual;
            candies -= actual;
            given++;
            if (i == num_people)
                i = 0;
        }
        return ans;
    }
};
```

```cpp
// 观察第一份代码可以发现，每次循环，i和given的更新是一样的，且两者总是相差一，所以可以只用一个变量i。
// 另外再配合模运算来绕圈。
vector<int> distributeCandies(int candies, int n) {
    vector<int> res(n);
    for (int i = 0; candies > 0; ++i) {
        res[i % n] += min(candies, i + 1);
        candies -= i + 1;
    }
    return res;
}
```

