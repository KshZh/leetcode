# 341. Flatten Nested List Iterator

> Given a nested list of integers, implement an iterator to flatten it.
>
> Each element is either an integer, or a list -- whose elements may also be integers or other lists.
>
> **Example 1:**
>
> ```
> Input: [[1,1],2,[1,1]]
> Output: [1,1,2,1,1]
> Explanation: By calling next repeatedly until hasNext returns false, 
>              the order of elements returned by next should be: [1,1,2,1,1].
> ```
>
> **Example 2:**
>
> ```
> Input: [1,[4,[6]]]
> Output: [1,4,6]
> Explanation: By calling next repeatedly until hasNext returns false, 
>              the order of elements returned by next should be: [1,4,6].
> ```

1. Medium。

```cpp
/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *   public:
 *     // Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     bool isInteger() const;
 *
 *     // Return the single integer that this NestedInteger holds, if it holds a single integer
 *     // The result is undefined if this NestedInteger holds a nested list
 *     int getInteger() const;
 *
 *     // Return the nested list that this NestedInteger holds, if it holds a nested list
 *     // The result is undefined if this NestedInteger holds a single integer
 *     const vector<NestedInteger> &getList() const;
 * };
 */
class NestedIterator {
    vector<int> ints;
    int i = 0;
    void flat(vector<NestedInteger> &nestedList) {
        for (NestedInteger& nt: nestedList) {
            if (nt.isInteger()) ints.push_back(nt.getInteger());
            else flat(nt.getList());
        }
    }
public:
    // 一次性计算。
    NestedIterator(vector<NestedInteger> &nestedList) {
        flat(nestedList);
    }

    int next() {
        return ints[i++];
    }

    bool hasNext() {
        return i!=ints.size();
    }
};

/**
 * Your NestedIterator object will be instantiated and called as such:
 * NestedIterator i(nestedList);
 * while (i.hasNext()) cout << i.next();
 */
```

```cpp
// 按需计算。
class NestedIterator {
    stack<NestedInteger> s;
public:
    NestedIterator(vector<NestedInteger> &nestedList) {
        for (int i=nestedList.size()-1; i>=0; i--)
            s.push(move(nestedList[i]));
    }

    int next() {
        int ans = s.top().getInteger();
        s.pop();
        return ans;
    }

    bool hasNext() {
        while (!s.empty()) {
            NestedInteger curr = s.top();
            if (curr.isInteger()) return true;
            s.pop();
            auto v = curr.getList();
            for (int i=v.size()-1; i>=0; i--) {
                s.push(move(v[i]));
            }
        }
        return false;
    }
};
```

