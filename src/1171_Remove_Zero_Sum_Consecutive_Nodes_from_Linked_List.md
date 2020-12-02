# 1171. Remove Zero Sum Consecutive Nodes from Linked List

> Given the `head` of a linked list, we **repeatedly** delete consecutive sequences of nodes that sum to `0` until there are no such sequences.
>
> After doing so, return the head of the final linked list. You may return any such answer.
>
>  
>
> (Note that in the examples below, all sequences are serializations of `ListNode` objects.)
>
> **Example 1:**
>
> ```
> Input: head = [1,2,-3,3,1]
> Output: [3,1]
> Note: The answer [1,2,1] would also be accepted.
> ```
>
> **Example 2:**
>
> ```
> Input: head = [1,2,3,-3,4]
> Output: [1,2,4]
> ```
>
> **Example 3:**
>
> ```
> Input: head = [1,2,3,-3,-2]
> Output: [1]
> ```

1. Medium。
2. 注意读题，不是只删除一个连续和为0的子串就够了，要删除全部。
3. 找到序列中和为0的子序列的思路是，用前缀和哈希表，如果累加得到一个哈希表中已存在的前缀和，那么说明上一个得出该前缀和的位置到当前位置的这个子序列的和为0。

```cpp
class Solution {
public:
    ListNode* removeZeroSumSublists(ListNode* head) {
        ListNode dummy(0), *p=&dummy;
        p->next = head;
        int prefix = 0;
        unordered_map<int, ListNode*> m;
        for (; p; p=p->next)
            m[prefix+=p->val] = p; // 相同的前缀和会覆盖。
        prefix = 0;
        for (p=&dummy; p; p=p->next)
            // 如果当前prefix在整个序列中只出现一次，那么`m[prefix+=p->val]->next == p->next`，
            // 否则下面这个赋值语句会跳过和为0的子序列。
            // 注意有内存泄漏，可以通过循环walk一下来释放堆内存。
            p->next = m[prefix+=p->val]->next;
        return dummy.next;
    }
};
```

