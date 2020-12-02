# 380. Insert Delete GetRandom O(1)

> Design a data structure that supports all following operations in *average* **O(1)** time.
>
> 1. `insert(val)`: Inserts an item val to the set if not already present.
> 2. `remove(val)`: Removes an item val from the set if present.
> 3. `getRandom`: Returns a random element from current set of elements. Each element must have the **same probability** of being returned.
>
> **Example:**
>
> ```
> // Init an empty set.
> RandomizedSet randomSet = new RandomizedSet();
> 
> // Inserts 1 to the set. Returns true as 1 was inserted successfully.
> randomSet.insert(1);
> 
> // Returns false as 2 does not exist in the set.
> randomSet.remove(2);
> 
> // Inserts 2 to the set, returns true. Set now contains [1,2].
> randomSet.insert(2);
> 
> // getRandom should return either 1 or 2 randomly.
> randomSet.getRandom();
> 
> // Removes 1 from the set, returns true. Set now contains [2].
> randomSet.remove(1);
> 
> // 2 was already in the set, so return false.
> randomSet.insert(2);
> 
> // Since 2 is the only number in the set, getRandom always return 2.
> randomSet.getRandom();
> ```

1. Medium。
2. 因为要O(1)查找，所以需要用哈希表，将一个元素映射到其在数组中的下标。
3. swap到数组末尾后再删除，这样就不用移动数组元素，达到O(1)时间复杂度。当然，并不需要真的交换，只需要把末尾元素的值覆盖要删除的元素即可。

```cpp
class RandomizedSet {
public:
    /** Initialize your data structure here. */
    RandomizedSet() {}
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    bool insert(int val) {
        if (location.find(val) != location.end()) return false;
        nums.emplace_back(val);
        location[val] = nums.size() - 1;
        return true;
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    bool remove(int val) {
        if (location.find(val) == location.end()) return false;
        int last = nums.back();
        location[last] = location[val];
        nums[location[val]] = last; // 不需要真的交换，只需要把末尾元素的值覆盖要删除的元素即可。
        nums.pop_back();
        location.erase(val);
        return true;
    }
    
    /** Get a random element from the set. */
    int getRandom() {
        return nums[rand() % nums.size()];
    }
private:
    vector<int> nums;
    unordered_map<int, int> location;
};
```

