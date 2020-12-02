# 1396. Design Underground System

> Implement the class `UndergroundSystem` that supports three methods:
>
> 1.` checkIn(int id, string stationName, int t)`
>
> - A customer with id card equal to `id`, gets in the station `stationName` at time `t`.
> - A customer can only be checked into one place at a time.
>
> 2.` checkOut(int id, string stationName, int t)`
>
> - A customer with id card equal to `id`, gets out from the station `stationName` at time `t`.
>
> \3. `getAverageTime(string startStation, string endStation)` 
>
> - Returns the average time to travel between the `startStation` and the `endStation`.
> - The average time is computed from all the previous traveling from `startStation` to `endStation` that happened **directly**.
> - Call to `getAverageTime` is always valid.
>
> You can assume all calls to `checkIn` and `checkOut` methods are consistent. That is, if a customer gets in at time **t1** at some station, then it gets out at time **t2** with **t2 > t1**. All events happen in chronological order.

1. Medium。

```cpp
// 因为题目保证了checkIn和checkOut是严格一一配对的，所以代码中就没做什么检查。
class UndergroundSystem {
    unordered_map<int, pair<string, int>> book;
    unordered_map<string, unordered_map<string, pair<int, int>>> avg;
public:
    UndergroundSystem() {
        
    }
    
    void checkIn(int id, string stationName, int t) {
        book[id] = {stationName, t}; // 可能被覆盖，这对连续多个checkIn(1)，后接多个checkOut(1)的序列是危险的。但测试中并没有出现这种情况，如果有的话，可以考虑再嵌入一个哈希表。 
    }
    
    void checkOut(int id, string stationName, int t) {
        avg[book[id].first][stationName].first += t-book[id].second;
        avg[book[id].first][stationName].second++;
    }
    
    double getAverageTime(string startStation, string endStation) {
        return 1.0*avg[startStation][endStation].first/avg[startStation][endStation].second;
    }
};

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * UndergroundSystem* obj = new UndergroundSystem();
 * obj->checkIn(id,stationName,t);
 * obj->checkOut(id,stationName,t);
 * double param_3 = obj->getAverageTime(startStation,endStation);
 */
```

