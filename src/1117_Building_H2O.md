# 1117. Building H2O

> There are two kinds of threads, `oxygen` and `hydrogen`. Your goal is to group these threads to form water molecules. There is a barrier where each thread has to wait until a complete molecule can be formed. Hydrogen and oxygen threads will be given `releaseHydrogen` and `releaseOxygen` methods respectively, which will allow them to pass the barrier. These threads should pass the barrier in groups of three, and they must be able to immediately bond with each other to form a water molecule. You must guarantee that all the threads from one molecule bond *before* any other threads from the next molecule do.
>
> In other words:
>
> - If an oxygen thread arrives at the barrier when no hydrogen threads are present, it has to wait for two hydrogen threads.
> - If a hydrogen thread arrives at the barrier when no other threads are present, it has to wait for an oxygen thread and another hydrogen thread.
>
> We don’t have to worry about matching the threads up explicitly; that is, the threads do not necessarily know which other threads they are paired up with. The key is just that threads pass the barrier in complete sets; thus, if we examine the sequence of threads that bond and divide them into groups of three, each group should contain one oxygen and two hydrogen threads.
>
> Write synchronization code for oxygen and hydrogen molecules that enforces these constraints.
>
> **Example 1:**
>
> ```
> Input: "HOH"
> Output: "HHO"
> Explanation: "HOH" and "OHH" are also valid answers.
> ```
>
> **Example 2:**
>
> ```
> Input: "OOHHHH"
> Output: "HHOHHO"
> Explanation: "HOHHHO", "OHHHHO", "HHOHOH", "HOHHOH", "OHHHOH", "HHOOHH", "HOHOHH" and "OHHOHH" are also valid answers.
> ```
>
> **Constraints:**
>
> - Total length of input string will be 3*n*, where 1 ≤ *n* ≤ 20.
> - Total number of `H` will be 2*n* in the input string.
> - Total number of `O` will be *n* in the input string.

1. Medium。

```java
class H2O {
    
    Semaphore h, o;
    public H2O() {
        h = new Semaphore(2, true);
        o = new Semaphore(0, true);
    }

    public void hydrogen(Runnable releaseHydrogen) throws InterruptedException {
		h.acquire();
        releaseHydrogen.run();
        o.release();
        
    }

    public void oxygen(Runnable releaseOxygen) throws InterruptedException {
        o.acquire(2);
		releaseOxygen.run();
        h.release(2);
    }
}
```

> I think this solution will print correctly, but might relase O threads in wrong sequence. Example, if threads arrive as O1, O2, H1, H2, H3, H4 we should release O1 together with H1 and H2. Both O1 and O2 are locked at o.acquire(2), o.release(); was called twice (H1 and H2), scheduled can select either O1 or O2 to run I think.
>
> The Problem has this part "You must guarantee that all the threads from one molecule(分子) bond before any other threads from the next molecule do", which can be read as prohibiting to swap threads between molecules.

关于这一点，可以使用Semaphore的构造函数的第二个参数：

> `fair` - `true` if this semaphore will guarantee first-in first-out granting of permits under contention, else `false`