# 175. Combine Two Tables

> Table: `Person`
>
> ```
> +-------------+---------+
> | Column Name | Type    |
> +-------------+---------+
> | PersonId    | int     |
> | FirstName   | varchar |
> | LastName    | varchar |
> +-------------+---------+
> PersonId is the primary key column for this table.
> ```
>
> Table: `Address`
>
> ```
> +-------------+---------+
> | Column Name | Type    |
> +-------------+---------+
> | AddressId   | int     |
> | PersonId    | int     |
> | City        | varchar |
> | State       | varchar |
> +-------------+---------+
> AddressId is the primary key column for this table.
> ```
>
> Write a SQL query for a report that provides the following information for each person in the Person table, regardless if there is an address for each of those people:
>
> ```
> FirstName, LastName, City, State
> ```

1. Easy。

https://stackoverflow.com/questions/3308122/how-do-i-decide-when-to-use-right-joins-left-joins-or-inner-joins-or-how-to-dete/3308153#3308153

![](../img/Visual_SQL_JOINS_orig.jpg)

```sql
-- 题目中要求就算某个人没有地址相关的记录，也要把它输出，所以需要用left join，而不是默认的inner join。
select FirstName, LastName, City, State
from Person left join Address
on Person.PersonId = Address.PersonId
;
```