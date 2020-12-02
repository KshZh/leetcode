# 178. Rank Scores

> Write a SQL query to rank scores. If there is a tie between two scores, both should have the same ranking. Note that after a tie, the next ranking number should be the next consecutive integer value. In other words, there should be no "holes" between ranks.
>
> ```
> +----+-------+
> | Id | Score |
> +----+-------+
> | 1  | 3.50  |
> | 2  | 3.65  |
> | 3  | 4.00  |
> | 4  | 3.85  |
> | 5  | 4.00  |
> | 6  | 3.65  |
> +----+-------+
> ```
>
> For example, given the above `Scores` table, your query should generate the following report (order by highest score):
>
> ```
> +-------+------+
> | Score | Rank |
> +-------+------+
> | 4.00  | 1    |
> | 4.00  | 1    |
> | 3.85  | 2    |
> | 3.65  | 3    |
> | 3.65  | 3    |
> | 3.50  | 4    |
> +-------+------+
> ```

1. Medium。

![](https://assets.leetcode.com/users/sophiesu0827/image_1576871668.png)

```sql
SELECT S1.Score, COUNT(*) AS Rank FROM Scores S1,
(SELECT DISTINCT Score FROM Scores) S2
WHERE S1.Score<=S2.Score -- 一个Id通过join后可能产生多条相同Id的记录，这些记录中的Score大于等于Id的原Score。
GROUP BY S1.Id -- 按照Id分组，然后Count，可以得到有多少个成绩比Id的成绩高，得到Id的rank。
ORDER BY S1.Score DESC;
```

```sql
SELECT
  Score,
  @rank := @rank + (@prev <> (@prev := Score)) Rank -- 将布尔值转换为0或1。
FROM
  Scores,
  (SELECT @rank := 0, @prev := -1) init
ORDER BY Score desc; -- 这里依赖于先对表进行排序。
```

