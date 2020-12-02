# 133. Clone Graph

> Given a reference of a node in a **[connected](https://en.wikipedia.org/wiki/Connectivity_(graph_theory)#Connected_graph)** undirected graph, return a [**deep copy**](https://en.wikipedia.org/wiki/Object_copying#Deep_copy) (clone) of the graph. Each node in the graph contains a val (`int`) and a list (`List[Node]`) of its neighbors.
>
> ![img](https://assets.leetcode.com/uploads/2019/11/04/133_clone_graph_question.png)
>
> **Note:**
>
> 1. The number of nodes will be between 1 and 100.
> 2. The undirected graph is a [simple graph](https://en.wikipedia.org/wiki/Graph_(discrete_mathematics)#Simple_graph), which means no repeated edges and no self-loops in the graph.
> 3. Since the graph is undirected, if node *p* has node *q* as neighbor, then node *q* must have node *p* as neighbor too.
> 4. You must return the **copy of the given node** as a reference to the cloned graph.

1. 图，Medium。
2. dfs, bfs都可以，一般bfs代码更少，更简洁。

```cpp
/*
// Definition for a Node.
class Node {
public:
    int val;
    vector<Node*> neighbors;

    Node() {}

    Node(int _val, vector<Node*> _neighbors) {
        val = _val;
        neighbors = _neighbors;
    }
};
*/
class Solution {
private:
    unordered_map<Node*, Node*> book; // 原结点的地址和拷贝后的结点的地址的映射。
public:
    Node* cloneGraph(Node* node) {
        return dfs(node);
    }
    
    Node* dfs(Node* u) {
        if (book.find(u) != book.end()) { // 避免拷贝同一个结点多次。
            return book[u];
        }
        Node* x = new Node(u->val);
        book[u] = x;
        for (Node* neighbor: u->neighbors) {
            x->neighbors.push_back(dfs(neighbor));
        }
        return x;
    }
};
```

```cpp
class Solution {
private:
    unordered_map<Node*, Node*> book; // 原结点的地址和拷贝后的结点的地址的映射。
public:
    Node* cloneGraph(Node* node) {
        return bfs(node);
    }
    
    Node* bfs(Node* u) {
        Node* p;
        queue<Node*> q;
        q.push(u);
        book[u] = new Node(u->val);
        while (!q.empty()) {
            p = q.front();
            q.pop();
            for (Node* neighbor: p->neighbors) {
                if (book.find(neighbor) == book.end()) {
                    book[neighbor] = new Node(neighbor->val);
                    q.push(neighbor);
                }
                book[p]->neighbors.push_back(book[neighbor]);
            }
        }
        return book[u];
    }
};
```



