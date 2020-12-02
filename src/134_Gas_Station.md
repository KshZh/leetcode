# 134. Gas Station

> There are *N* gas stations along a circular route, where the amount of gas at station *i* is `gas[i]`.
>
> You have a car with an unlimited gas tank and it costs `cost[i]` of gas to travel from station *i* to its next station (*i*+1). You begin the journey with an empty tank at one of the gas stations.
>
> Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.
>
> **Note:**
>
> - If there exists a solution, it is guaranteed to be unique.
> - Both input arrays are non-empty and have the same length.
> - Each element in the input arrays is a non-negative integer.
>
> **Example 1:**
>
> ```
> Input: 
> gas  = [1,2,3,4,5]
> cost = [3,4,5,1,2]
> 
> Output: 3
> 
> Explanation:
> Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
> Travel to station 4. Your tank = 4 - 1 + 5 = 8
> Travel to station 0. Your tank = 8 - 2 + 1 = 7
> Travel to station 1. Your tank = 7 - 3 + 2 = 6
> Travel to station 2. Your tank = 6 - 4 + 3 = 5
> Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
> Therefore, return 3 as the starting index.
> ```
>
> **Example 2:**
>
> ```
> Input: 
> gas  = [2,3,4]
> cost = [3,4,3]
> 
> Output: -1
> 
> Explanation:
> You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
> Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
> Travel to station 0. Your tank = 4 - 3 + 2 = 3
> Travel to station 1. Your tank = 3 - 3 + 3 = 3
> You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
> Therefore, you can't travel around the circuit once no matter where you start.
> ```

1. Medium，贪心。

```cpp
// 直接枚举所有起点，然后模拟尝试走`一圈。
class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        auto n = gas.size();
        int nleft, i, j, pos;
        for (i=0; i<n; i++) {
            if (gas[i] < cost[i]) // 第一个站都不够油，肯定不能作为起点。当然这里也可以不检查，放到下面一起检查。
                continue;
            nleft=0, pos=i;
            for (j=0; j<n; j++) {
                nleft += gas[pos]-cost[pos]; // 既然油箱大小无限，则总是加满油到下一个站。
                if (nleft < 0) break; // 不够油到下一个站。
                pos = (pos+1)%n;
            }
            if (j == n) return pos;
            // 如果知道一个性质：2. 如果start无法到i+1，那么start到i+1之间的站点都无法到i+1，所以起点重新考虑为i+1。
            // 那么就可以直接让i跳过pos走过的站点，使得该实现变为O(N)。
        }
        return -1;
    }
};
```

```cpp
// 1. 如果总剩余大于等于0，那么一定有解。
// 2. 如果start无法到i+1，那么start到i+1之间的站点都无法到i+1，所以起点重新考虑为i+1。
class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        auto n = gas.size();
        int nleft=0, i, start=0, totalLeft=0;
        for (i=0; i<n; i++) {
            nleft += gas[i]-cost[i];
            if (nleft < 0) {
                totalLeft += nleft;
                nleft = 0;
                start = i+1; // cost[i]是i到i+1的代价。
            }
        }
        return totalLeft+nleft>=0? start: -1;
    }
};
```

```cpp
class Solution {
public:
    int canCompleteCircuit(vector<int> &gas, vector<int> &cost) {

       int start = gas.size()-1;
       int end = 0;
       int sum = gas[start] - cost[start];
       while (start > end) {
          if (sum >= 0) {
             sum += gas[end] - cost[end];
             ++end;
          }
          else {
             --start;
             sum += gas[start] - cost[start];
          }
       }
       return sum >= 0 ? start : -1;
    }
};
```

