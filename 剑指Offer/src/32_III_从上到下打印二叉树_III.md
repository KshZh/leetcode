# 32 - III. 从上到下打印二叉树 III

> 请实现一个函数按照之字形顺序打印二叉树，即第一行按照从左到右的顺序打印，第二层按照从右到左的顺序打印，第三行再按照从左到右的顺序打印，其他行以此类推。

1. Medium。

```java
// 用逆序填充数组代替顺序填充后reverse()。
// 当然对于偶数层（从第一层开始）也可以用栈保存，之后弹出。
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        if (root == null) return res;
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        boolean flag = true;
        while (!q.isEmpty()) {
            // List<Integer> l = new ArrayList<>(q.size());
            // l.size()为0，这个构造函数的参数是容量不是大小。
            Integer[] l = new Integer[q.size()]; // 因为要使用Arrays.asList()，所以不能是int[]。
            for (int i=q.size()-1, j=0; i>=0; i--, j++) {
                TreeNode x = q.poll();
                // java.lang.IndexOutOfBoundsException: Index: 1, Size: 0
                // l.add((flag? j: i), x.val); 
                l[flag? j: i] = x.val; // XXX 顺序/逆序填充数组。
                if (x.left != null) q.offer(x.left);
                if (x.right != null) q.offer(x.right);
            }
            res.add(Arrays.asList(l));
            flag = !flag;
        }
        return res;
    }
}
```

