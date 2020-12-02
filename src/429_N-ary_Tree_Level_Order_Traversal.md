# 429. N-ary Tree Level Order Traversal

> Given an n-ary tree, return the *level order* traversal of its nodes' values.
>
> *Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the null value (See examples).*
>
> **Example 1:**
>
> <img src="https://assets.leetcode.com/uploads/2018/10/12/narytreeexample.png" alt="img" style="zoom: 33%;" />
>
> ```
> Input: root = [1,null,3,2,4,null,5,6]
> Output: [[1],[3,2,4],[5,6]]
> ```
>
> **Example 2:**
>
> <img src="https://assets.leetcode.com/uploads/2019/11/08/sample_4_964.png" alt="img" style="zoom:33%;" />
>
> ```
> Input: root = [1,null,2,3,4,5,null,null,6,7,null,8,null,9,10,null,null,11,null,12,null,13,null,null,14]
> Output: [[1],[2,3,4,5],[6,7,8,9,10],[11,12,13],[14]]
> ```
>
> **Constraints:**
>
> - The height of the n-ary tree is less than or equal to `1000`
> - The total number of nodes is between `[0, 10^4]`

1. Medium。

```cpp
vector<vector<int>> levelOrder(Node* root) {
    if (!root) return {};
    vector<vector<int>> ret;
    queue<Node*> q;
    q.push(root);
    Node* x;
    while (!q.empty()) {
        auto n = q.size();
        vector<int> v;
        v.reserve(n);
        for (int i=0; i<n; i++) {
            x = q.front();
            q.pop();
            v.push_back(x->val);
            for (Node* child: x->children)
                q.push(child); // 这里如果要更安全一点，就要判断child是否为nullptr。
        }
        ret.push_back(std::move(v));
    }
    return ret;
}
```

```python
class Solution(object):
    def levelOrder(self, root):
        q, ret = [root], []
        while any(q):
            ret.append([node.val for node in q])
            q = [child for node in q for child in node.children if child]
        return ret
```

```java
public List<List<Integer>> levelOrder(Node root) {
    List<List<Integer>> ret = new LinkedList<>();

    if (root == null) return ret;

    Queue<Node> queue = new LinkedList<>();

    queue.offer(root);

    while (!queue.isEmpty()) {
        List<Integer> curLevel = new LinkedList<>();
        int len = queue.size();
        for (int i = 0; i < len; i++) {
            Node curr = queue.poll();
            curLevel.add(curr.val);
            for (Node c : curr.children)
                queue.offer(c);
        }
        ret.add(curLevel); // java有GC，这里只是拷贝了容器的地址，并没有拷贝整个容器。
    }

    return ret;
}
```

