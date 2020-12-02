# 381. Insert Delete GetRandom O(1) - Duplicates allowed

> Design a data structure that supports all following operations in *average* **O(1)** time.
>
> **Note: Duplicate elements are allowed.**
>
> 1. `insert(val)`: Inserts an item val to the collection.
> 2. `remove(val)`: Removes an item val from the collection if present.
> 3. `getRandom`: Returns a random element from current collection of elements. The probability of each element being returned is **linearly related** to the number of same value the collection contains.
>
> **Example:**
>
> ```
> // Init an empty collection.
> RandomizedCollection collection = new RandomizedCollection();
> 
> // Inserts 1 to the collection. Returns true as the collection did not contain 1.
> collection.insert(1);
> 
> // Inserts another 1 to the collection. Returns false as the collection contained 1. Collection now contains [1,1].
> collection.insert(1);
> 
> // Inserts 2 to the collection, returns true. Collection now contains [1,1,2].
> collection.insert(2);
> 
> // getRandom should return 1 with the probability 2/3, and returns 2 with the probability 1/3.
> collection.getRandom();
> 
> // Removes 1 from the collection, returns true. Collection now contains [1,2].
> collection.remove(1);
> 
> // getRandom should return 1 and 2 both equally likely.
> collection.getRandom();
> ```

1. Medium。
2. 类似380，不过允许插入重复元素，那么需要用哈希表存储多个下标，那么删除下标也需要O(1)时间复杂度，这里直接取最后一个下标删除即可。

> https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/discuss/85541/C%2B%2B-128m-Solution-Real-O(1)-Solution
>
> [@mshete](https://leetcode.com/mshete) That's not the problem I mentioned above. `std::rand()` will generate random number between `0` and `RAND_MAX` inclusive (i.e. `[0, RAND_MAX]`). When `(RAND_MAX + 1) % (y - x + 1) != 0`, the result is biased.
>
> For example, let's assume `RAND_MAX = 9`, and we want to generate number between 2 and 5 inclusive.
>
> ```
>                        rand()  0 1 2 3 4 5 6 7 8 9
>     std::rand() % (5 - 2 + 1)  0 1 2 3 0 1 2 3 0 1
> 2 + std::rand() % (5 - 2 + 1)  2 3 4 5 2 3 4 5 2 3
> ```
>
> It is easy to see that the chance for each possible number between 2 and 5 inclusive is not equal.
>
> P(2)=P(3)=3/10 P(4)=P(5)=2/10

```cpp
class RandomizedCollection {
public:
    /** Initialize your data structure here. */
    RandomizedCollection() {}
    
    /** Inserts a value to the collection. Returns true if the collection did not already contain the specified element. */
    bool insert(int val) {
        bool ret = locations.find(val)==locations.end();
        nums.push_back({val, locations[val].size()});
        locations[val].push_back(nums.size()-1);
        return ret;
    }
    
    /** Removes a value from the collection. Returns true if the collection contained the specified element. */
    bool remove(int val) {
        if (locations.find(val)==locations.end()) return false;
        auto last = nums.back();
        locations[last.first][last.second] = locations[val].back(); // 直接删除locations[val]最后一个下标。
        nums[locations[val].back()] = last;
        nums.pop_back();
        locations[val].pop_back();
        if (locations[val].empty()) locations.erase(val);
        return true;
    }
    
    /** Get a random element from the collection. */
    int getRandom() {
        return nums[std::rand() % nums.size()].first;
    }
private:
    vector<pair<int, int>> nums;
    unordered_map<int, vector<int>> locations;
};

/**
 * Your RandomizedCollection object will be instantiated and called as such:
 * RandomizedCollection* obj = new RandomizedCollection();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */
```

