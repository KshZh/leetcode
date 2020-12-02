# 1116. Print Zero Even Odd

> Suppose you are given the following code:
>
> ```
> class ZeroEvenOdd {
>   public ZeroEvenOdd(int n) { ... }      // constructor
>   public void zero(printNumber) { ... }  // only output 0's
>   public void even(printNumber) { ... }  // only output even numbers
>   public void odd(printNumber) { ... }   // only output odd numbers
> }
> ```
>
> The same instance of `ZeroEvenOdd` will be passed to three different threads:
>
> 1. Thread A will call `zero()` which should only output 0's.
> 2. Thread B will call `even()` which should only ouput even numbers.
> 3. Thread C will call `odd()` which should only output odd numbers.
>
> Each of the threads is given a `printNumber` method to output an integer. Modify the given program to output the series `010203040506`... where the length of the series must be 2*n*.
>
>  
>
> **Example 1:**
>
> ```
> Input: n = 2
> Output: "0102"
> Explanation: There are three threads being fired asynchronously. One of them calls zero(), the other calls even(), and the last one calls odd(). "0102" is the correct output.
> ```
>
> **Example 2:**
>
> ```
> Input: n = 5
> Output: "0102030405"
> ```

1. Medium。

```java
class ZeroEvenOdd {
    private int n;
    private Semaphore zero = new Semaphore(1);
    private Semaphore even = new Semaphore(0);
    private Semaphore odd = new Semaphore(0);
    
    public ZeroEvenOdd(int n) {
        this.n = n;
    }

    // printNumber.accept(x) outputs "x", where x is an integer.
    public void zero(IntConsumer printNumber) throws InterruptedException {
        // 0会打印n次。
        for (int i=0; i<n; i++) {
            zero.acquire();
            printNumber.accept(0);
            if ((i&1) == 0) {
                odd.release();
            } else {
                even.release();
            }
        }
    }

    public void even(IntConsumer printNumber) throws InterruptedException {
        for (int i=2; i<=n; i+=2) {
            even.acquire();
            printNumber.accept(i);
            zero.release();
        }
    }

    public void odd(IntConsumer printNumber) throws InterruptedException {
        for (int i=1; i<=n; i+=2) {
            odd.acquire();
            printNumber.accept(i);
            zero.release();
        }
    }
}
```

