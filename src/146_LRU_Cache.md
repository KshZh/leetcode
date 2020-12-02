# 146. LRU Cache

>Design and implement a data structure for [Least Recently Used (LRU) cache](https://en.wikipedia.org/wiki/Cache_replacement_policies#LRU). It should support the following operations: `get` and `put`.
>
>`get(key)` - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
>`put(key, value)` - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
>
>The cache is initialized with a **positive** capacity.
>
>**Example:**
>
>```
>LRUCache cache = new LRUCache( 2 /* capacity */ );
>
>cache.put(1, 1);
>cache.put(2, 2);
>cache.get(1);       // returns 1
>cache.put(3, 3);    // evicts key 2
>cache.get(2);       // returns -1 (not found)
>cache.put(4, 4);    // evicts key 1
>cache.get(1);       // returns -1 (not found)
>cache.get(3);       // returns 3
>cache.get(4);       // returns 4
>```

1. Medium。
2. 模拟LRU置换策略，插入表头，淘汰表尾。
3. 如果要求手写链表的话，就定义一个Node结构，包含prev和next指针，一个双向链表定义一个头哨兵和尾哨兵，再定义insert(position), erase(position), push_front(), pop_back()即可。

```cpp
class LRUCache {
private:
	// 链表在任何位置插入和删除的复杂度都是O(1)，特别地，list有insert(), emplace(), erase()，
	// 而forward_list则是insert_after(), emplace_after(), erase_after()，毕竟单链表只有next指针，没有prev指针。
	// 然而，如果不是在头尾，那么遍历链表找到要插入和删除的位置是需要O(N)的，这时，可以结合哈希表，记录key在
	// 链表中的位置（指针/迭代器），这样我们就可以O(1)找到要处理的位置，再O(1)插入或删除，总复杂度为O(1)。
	// 而且，不能使用单向链表，因为即使知道要删除元素的位置（注意不是该元素的前驱结点的位置），删除该元素仍然需要O(N)时间复杂度。
	// 另外由于链表的存储结构和访问方式，即按结点存储元素，结点之间只能通过next或prev指针移动，即使这些结点连续存储，
	// 所以链表的迭代器在插入后，各迭代器不失效，删除后，只是指向被删除元素的迭代器失效。
	unordered_map<int, list<pair<int, int>>::iterator> position_;
	list<pair<int, int>> lst_;
	int capacity_;
public:
	LRUCache(int capacity): capacity_(capacity) {}

	int get(int key) {
		if (position_.find(key) == position_.end())
			return -1;
		int val = position_[key]->second;
		lst_.erase(position_[key]); // 最近访问过，放到表头。
		lst_.push_front(make_pair(key, val));
		position_[key] = lst_.begin();
		return val;
	}

	void put(int key, int value) {
		if (position_.find(key) != position_.end()) { // key已存在，新/同一个value。
			lst_.erase(position_[key]);
		} else if (lst_.size() == capacity_) { // 容量不足，evict。
			position_.erase(lst_.back().first); // 淘汰表尾，即最近最少使用的元素。
			lst_.pop_back();
		}
		lst_.push_front(make_pair(key, value)); // 插入表头。
		position_[key] = lst_.begin();
	}
};
```

