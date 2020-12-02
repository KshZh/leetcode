# 155. Min Stack

> Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
>
> - push(x) -- Push element x onto stack.
> - pop() -- Removes the element on top of the stack.
> - top() -- Get the top element.
> - getMin() -- Retrieve the minimum element in the stack.
>
>  
>
> **Example:**
>
> ```
> MinStack minStack = new MinStack();
> minStack.push(-2);
> minStack.push(0);
> minStack.push(-3);
> minStack.getMin();   --> Returns -3.
> minStack.pop();
> minStack.top();      --> Returns 0.
> minStack.getMin();   --> Returns -2.
> ```

1. Easy。
2. 也可以用栈+最小堆，但这样的话入栈和出栈都变成了O(logN)。

```cpp
class MinStack {
    stack<int> s;
    int min = INT_MAX;
public:
    /** initialize your data structure here. */
    MinStack() {
        
    }
    
    void push(int x) {
        if (x <= min) {
            s.push(min); // 把旧的min入栈，再入栈新的min。
            min = x;
        }
        s.push(x);
    }
    
    void pop() {
        if (s.top() == min) { // 当前min被弹出了，那就再弹出相邻的旧的min。
            s.pop();
            min = s.top();
        }
        s.pop();
    }
    
    int top() {
        return s.top();
    }
    
    int getMin() {
        return min;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(x);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */
```

```cpp
class MinStack {
private:
    stack<int> s1;
    stack<int> s2; // 保持入栈过程中看到的所有min。
public:
    void push(int x) {
	    s1.push(x);
	    if (s2.empty() || x <= getMin())  s2.push(x);	    
    }
    void pop() {
	    if (s1.top() == getMin())  s2.pop();
	    s1.pop();
    }
    int top() {
	    return s1.top();
    }
    int getMin() {
	    return s2.top();
    }
};
```

```cpp
// 自己用单链表实现。
// 用单链表实现栈，栈顶必须设置在表头，这样入栈和出栈才都是O(1)。
class MinStack {
    private Node head;
    
    public void push(int x) {
        if(head == null) 
            head = new Node(x, x);
        else 
            head = new Node(x, Math.min(x, head.min), head);
    }

    public void pop() {
        head = head.next;
    }

    public int top() {
        return head.val;
    }

    public int getMin() {
        return head.min;
    }
    
    private class Node {
        int val;
        int min;
        Node next;
        
        private Node(int val, int min) {
            this(val, min, null);
        }
        
        private Node(int val, int min, Node next) {
            this.val = val;
            this.min = min;
            this.next = next;
        }
    }
}
```

