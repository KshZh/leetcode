# 176. Second Highest Salary

> Write a SQL query to get the second highest salary from the `Employee` table.
>
> ```
> +----+--------+
> | Id | Salary |
> +----+--------+
> | 1  | 100    |
> | 2  | 200    |
> | 3  | 300    |
> +----+--------+
> ```
>
> For example, given the above Employee table, the query should return `200` as the second highest salary. If there is no second highest salary, then the query should return `null`.
>
> ```
> +---------------------+
> | SecondHighestSalary |
> +---------------------+
> | 200                 |
> +---------------------+
> ```

1. Easy。
2. 注意投影部分是最后执行的，也就是先筛选出期望的tuple。

```sql
SELECT DISTINCT
    Salary AS SecondHighestSalary
FROM
    Employee
ORDER BY Salary DESC
LIMIT 1 OFFSET 1
```

```sql
-- However, this solution will be judged as 'Wrong Answer' if there is no such second highest salary since there might be only one record in this table. To overcome this issue, we can take this as a temp table.
SELECT
    (SELECT DISTINCT
            Salary
        FROM
            Employee
        ORDER BY Salary DESC
        LIMIT 1 OFFSET 1) AS SecondHighestSalary
;
```

```sql
-- Another way to solve the 'NULL' problem is to use IFNULL funtion as below.
SELECT
    IFNULL(
      (SELECT DISTINCT Salary
       FROM Employee
       ORDER BY Salary DESC
        LIMIT 1 OFFSET 1),
    NULL) AS SecondHighestSalary
```

```sql
select max(Salary) as SecondHighestSalary from Employee where Salary not in (select max(Salary) from Employee);
-- 注意投影部分是最后执行的，也就是先筛选出期望的tuple。
-- 如果需要查第3大、第4大等，这条语句就不好扩展。
```

