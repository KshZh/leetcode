# 1395. Count Number of Teams

> There are `n` soldiers standing in a line. Each soldier is assigned a **unique** `rating` value.
>
> You have to form a team of 3 soldiers amongst them under the following rules:
>
> - Choose 3 soldiers with index (`i`, `j`, `k`) with rating (`rating[i]`, `rating[j]`, `rating[k]`).
> - A team is valid if: (`rating[i] < rating[j] < rating[k]`) or (`rating[i] > rating[j] > rating[k]`) where (`0 <= i < j < k < n`).
>
> Return the number of teams you can form given the conditions. (soldiers can be part of multiple teams).

1. Medium。

```cpp
// 乘法原理，达成一个目标需要多个步骤，那么达成目标的方法数就是每个步骤的方法数相乘。
// 比如步骤一有3种方法，步骤二有2种方法，那么步骤一的每种方法都可以和步骤二的2种方法组合。
int numTeams(vector<int>& rating) {
    auto n = rating.size();
    if (n < 3) return 0;
    int numLargerLeft, numLessLeft, numLargerRight, numLessRight;
    int sum = 0;
    // 枚举三元组的中点。
    for (int i=1; i<n-1; i++) {
        numLargerLeft = numLessLeft = numLargerRight = numLessRight = 0;
        for (int j=0; j<i; j++) {
            if (rating[j] < rating[i]) numLessLeft++;
            else if (rating[j] > rating[i]) numLargerLeft++;
        }
        for (int j=i+1; j<n; j++) {
            if (rating[i] > rating[j]) numLessRight++;
            else if (rating[i] < rating[j]) numLargerRight++;
        }
        sum += numLargerLeft*numLessRight + numLessLeft*numLargerRight;
    }
    return sum;
}
```

