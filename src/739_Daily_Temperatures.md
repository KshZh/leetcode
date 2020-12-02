# 739. Daily Temperatures

> Given a list of daily temperatures `T`, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put `0` instead.
>
> For example, given the list of temperatures `T = [73, 74, 75, 71, 69, 72, 76, 73]`, your output should be `[1, 1, 4, 2, 1, 1, 0, 0]`.
>
> **Note:** The length of `temperatures` will be in the range `[1, 30000]`. Each temperature will be an integer in the range `[30, 100]`.

1. Medium。
2. **注意读题，题目要求输出相对下标，而不是绝对下标**。如果我们写程序时用的是绝对下标，记得转换一下再存储。
3. 注意到题目中的Note，因为温度的范围比较小，所以可以考虑从这个点入手。第一份代码因此时间复杂度是O(NW)，而W较小，几乎等于O(N)。而不是直接扫描输入数组，这样当输入数组很大时，时间复杂度就接近于平方。所以说，**要选好遍历的对象**。
4. 第二份代码的思路是，首先只需要在一个元素后面找第一个比它大的元素，所以我们可以在遍历时，把每个元素保存起来，然后继续遍历，当找到第一个比它大的元素时，就设置那个元素对应的答案。另外根据直观理解，我们保存起来的序列，其中包含未确定答案的元素，那么**该序列一定是降序的**，那么当我拿到一个新的元素，我要先把它于该序列中的第一个元素还是最后一个元素比较呢？最后一个元素，即最小的那个，否则与最大的那个比较，发现比最大的那个小了，那就把当前元素也存起来，这是错误的，**因为比最大的元素小，未必就比最小的元素小，而比最小的元素还小，那么一定比更大的元素小**，我们的**目的是尽快（因为题目要求找到第一个）确定保存的序列中的元素的答案**。所以我们选择用栈保存，而不是队列保存。
5. **注意到，我们保存的是元素的下标，而不是元素，因为后面我们要用下标设置输出数组中对应的位置，而且有了下标，且有输入数组，自然能得到对应的元素**。
6. 第二份代码的时间和空间复杂度都是O(N)，如果从后往前扫描，可以让空间复杂度小一些，为O(W)。

```cpp
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& T) {
        auto N = T.size();
        int i, j, idx;
        vector<int> v(N);
        vector<int> next(101, INT_MAX);
        for (i=N-1; i>=0; i--) {
            idx = INT_MAX;
            for (j=T[i]+1; j<101; j++) {
                if (next[j] < idx) {
                    idx = next[j];
                }
            }
            v[i] = idx==INT_MAX? 0: idx-i;
            next[T[i]] = i;
        }
        return v;
    }
};
```

```cpp
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& T) {
        auto N = T.size();
        int i, j, idx;
        vector<int> v(N);
        vector<int> s;
        for (i=0; i<N; i++) {
            while (!s.empty() && T[i]>T[s.back()]) {
                v[s.back()] = i-s.back();
                s.pop_back();
            }
            s.push_back(i);
        }
        return v;
    }
};
```

```cpp
class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& T) {
        auto N = T.size();
        int i, j, idx;
        vector<int> v(N);
        stack<int> s;
        for (i=N-1; i>=0; i--) {
            // 这一个程序用栈保存一个已确定答案的升序序列（栈顶最小）。
            while (!s.empty() && T[i]>=T[s.top()]) {
                s.pop_back();
            }
            v[i] = s.empty()? 0: s.top()-i;
            s.push(i);
        }
        return v;
    }
};
```

