# 148. Sort List

> Sort a linked list in *O*(*n* log *n*) time using constant space complexity.
>
> **Example 1:**
>
> ```
> Input: 4->2->1->3
> Output: 1->2->3->4
> ```
>
> **Example 2:**
>
> ```
> Input: -1->5->3->4->0
> Output: -1->0->3->4->5
> ```

1. Medium。
2. 第一份是自己写的朴素实现，复杂度大概就是O(N^2)了，所以超时了。
3. 因为要求O(NlogN)，其实想一下各种经典排序算法里，符合这个时间复杂度的就归并排序、快速排序和堆排序。
4. 最后一份的迭代版的归并排序可以做到空间复杂度的为O(1)，堆排序只有在数组情况下，对输入数组从最后一个父结点开始调整为堆直到根结点，这样的空间复杂度才是O(1)。
5. 链表操作：**使用快慢指针等分链表**。
6. 最后两份代码值得好好学习。

```cpp
class Solution {
public:
    ListNode* sortList(ListNode* head) {
        ListNode sentry(-1);
        sentry.next = head;
        ListNode *p = &sentry, *q = head, *z;
        while (q != NULL) {
            if (p->val > q->val) {
                p->next = q->next;
                for (z = &sentry; z->next!=NULL && z->next->val<q->val; z=z->next)
                    ;
				// z指向第一个比q->val大的结点的前驱结点。
                q->next = z->next;
                z->next = q;
                q = p->next;
            } else {
                p = p->next;
                q = q->next;
            }
        }
        return sentry.next;
    }
};
```

```cpp
// 堆排序。
class Solution {
    // val大的结点优先级高，先出队，然后使用头插法建链表。
    static constexpr auto cmp = [](ListNode* a, ListNode* b){ return a->val<b->val; };
public:
    ListNode* sortList(ListNode* head) {
        priority_queue<ListNode*, vector<ListNode*>, decltype(cmp)> q(cmp);
        // O(NlogN)，但空间复杂度为O(N)。
        while (head) {
            q.push(head); // O(logN)
            head = head->next;
        }
        ListNode sentry(-1), *p;
        head = &sentry;
        while (!q.empty()) {
            p = q.top();
            q.pop();
            p->next = head->next;
            head->next = p;
        }
        return head->next;
    }
};
```

```cpp
// https://leetcode.com/problems/sort-list/discuss/46714/Java-merge-sort-solution
// 归并排序，空间复杂度O(N)。
class Solution {
public:
    ListNode* sortList(ListNode* head) {
		if (head==nullptr || head->next==nullptr)
			return head;
        
        // 使用快慢指针等分链表。
        ListNode *prev=nullptr, *slow=head, *fast=head;
        while (fast && fast->next) {
            prev = slow;
            slow = slow->next;
            fast = fast->next->next;
        }
        prev->next = nullptr;
        
        return merge(sortList(head), sortList(slow));
    }
                     
    ListNode* merge(ListNode* l1, ListNode* l2) {
        ListNode head(-1);
        ListNode* p = &head;
        while (l1 && l2) {
            if (l1->val < l2->val) {
                p->next = l1;
                l1 = l1->next;
            } else {
                p->next = l2;
                l2 = l2->next;
            }
            p = p->next;
        }
        if (l1) p->next = l1;
        if (l2) p->next = l2;
        return head.next;
    }
};
```

```cpp
// https://leetcode.com/problems/sort-list/discuss/46712/Bottom-to-up(not-recurring)-with-o(1)-space-complextity-and-o(nlgn)-time-complextity
// 迭代版归并排序，O(1)空间复杂度。
// 值得好好学习的代码。
class Solution {
public:
    ListNode* sortList(ListNode* head) {
        // 如果没有结点，则返回nullptr；如果只有一个结点，就返回这个结点的地址。
		if (head==nullptr || head->next==nullptr)
			return head;
        
        int N = 0;
        ListNode* curr = head;
        while (curr) {
            N++;
            curr = curr->next;
        }
        
        ListNode dummy(-1);
        dummy.next = head;
        ListNode *left, *right, *tail;
        for (int step=1; step<N; step*=2) { // step等于N是无意义的，因为这样一个block中的第二个链表就为空了。
            curr = dummy.next;
            tail = &dummy;
            // 遍历处理所有block，每个block大小<=2*step。
            while (curr) {
                left = curr;
                right = split(left, step);
                curr = split(right, step);
                tail = merge(left, right, tail);
            }
        }
        return dummy.next;
    }
                     
    // tail指向上一个block的最后一个结点。这样才能把一个个block连起来。
    ListNode* merge(ListNode* l1, ListNode* l2, ListNode* tail) {
        ListNode* p = tail;
        while (l1 && l2) {
            if (l1->val < l2->val) {
                p->next = l1;
                l1 = l1->next;
            } else {
                p->next = l2;
                l2 = l2->next;
            }
            p = p->next;
        }
        if (l1) p->next = l1;
        if (l2) p->next = l2;
        while (p->next)
            p = p->next;
        return p; // 返回指向这一个block的最后一个结点的指针。这样才能把一个个block连起来。
    }
    
    ListNode* split(ListNode* head, int N) {
        while (--N && head) { // 让head跳过N-1个结点，变成分隔的第二个链表的表头的前驱指针。
            head = head->next;
        }
        if (head == nullptr) return nullptr;
        ListNode* second = head->next;
        head->next = nullptr;
        return second;
    }
};
```

