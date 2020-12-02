# 138. Copy List with Random Pointer

> A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.
>
> Return a [**deep copy**](https://en.wikipedia.org/wiki/Object_copying#Deep_copy) of the list.
>
> The Linked List is represented in the input/output as a list of `n` nodes. Each node is represented as a pair of `[val, random_index]` where:
>
> - `val`: an integer representing `Node.val`
> - `random_index`: the index of the node (range from `0` to `n-1`) where random pointer points to, or `null` if it does not point to any node.
>
> **Example 1:**
>
> ![img](https://assets.leetcode.com/uploads/2019/12/18/e1.png)
>
> ```
> Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
> Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
> ```

1. 链表，Medium。

```cpp
/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/
class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (head == nullptr) {
            return head;
        }
        // 两个映射。
        unordered_map<Node*, int> idx;
        unordered_map<int, Node*> addr;
        Node* p = head;
        int i;
        for (i=0; p; p=p->next, i++) {
            idx[p] = i;
        }
        Node lst(-1);
        p = &lst;
        Node* temp = head;
        for (i=0; head; head=head->next, i++) {
            p->next = new Node(head->val);
            p = p->next;
            addr[i] = p;
        }
        p = lst.next;
        head = temp;
        for (i=0; head; head=head->next, i++) {
            if (idx.find(head->random) == idx.end()) {
                p->random = nullptr;
            } else {
                p->random = addr[idx[head->random]];
            }
            p = p->next;
        }
        return lst.next;
    }
};
```

```cpp
class Solution {
public:
    Node* copyRandomList(Node* head) {
        // first round
        // 在原链表上，每一个结点复制一个。
        Node* p = head;
        Node* next;
        while (p) {
            next = p->next;
            p->next = new Node(p->val);
            p->next->next = next;
            p = next;
        }
        // second round
        // 填充复制结点的random属性。
        p = head;
        while (p) {
            if (p->random) {
                p->next->random = p->random->next;
            }
            p = p->next->next;
        }
        // third round
        // 分离链表。
        Node lst(-1);
        p = &lst;
        while (head) {
            p->next = head->next;
            p = p->next;
            head->next = head->next->next;
            head = head->next;
        }
        return lst.next;
    }
};
```

