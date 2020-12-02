# 32 - II. 从上到下打印二叉树 II

> 从上到下按层打印二叉树，同一层的节点按从左到右的顺序打印，每一层打印到一行。

1. Medium。

```java
class Solution {
    public List<List<Integer>> levelOrder(TreeNode root) {
        List<List<Integer>> res = new ArrayList<>();
        if (root == null) return res;
        Queue<TreeNode> q = new LinkedList<>();
        q.offer(root);
        while (!q.isEmpty()) {
            // int n = q.size();
            List<Integer> l = new ArrayList<>();
            // for (int i=0; i<n; i++) {
            for (int i=q.size()-1; i>=0; i--) {
                TreeNode x = q.poll();
                l.add(x.val);
                if (x.left != null) q.offer(x.left);
                if (x.right != null) q.offer(x.right);
            }
            res.add(l);
        }
        return res;
    }
}
```

