#  1114. Print in Order

> Suppose we have a class:
>
> ```
> public class Foo {
>   public void first() { print("first"); }
>   public void second() { print("second"); }
>   public void third() { print("third"); }
> }
> ```
>
> The same instance of `Foo` will be passed to three different threads. Thread A will call `first()`, thread B will call `second()`, and thread C will call `third()`. Design a mechanism and modify the program to ensure that `second()` is executed after `first()`, and `third()` is executed after `second()`.
>
> **Example 1:**
>
> ```
> Input: [1,2,3]
> Output: "firstsecondthird"
> Explanation: There are three threads being fired asynchronously. The input [1,2,3] means thread A calls first(), thread B calls second(), and thread C calls third(). "firstsecondthird" is the correct output.
> ```
>
> **Example 2:**
>
> ```
> Input: [1,3,2]
> Output: "firstsecondthird"
> Explanation: The input [1,3,2] means thread A calls first(), thread B calls third(), and thread C calls second(). "firstsecondthird" is the correct output.
> ```
>
> **Note:**
>
> We do not know how the threads will be scheduled in the operating system, even though the numbers in the input seems to imply the ordering. The input format you see is mainly to ensure our tests' comprehensiveness.

1. Easy。

```java
class Foo {
    private volatile boolean firstFinished = false;
    private volatile boolean secondFinished = false;

    public Foo() {
        
    }

    public synchronized void first(Runnable printFirst) throws InterruptedException {
        
        // printFirst.run() outputs "first". Do not change or remove this line.
        printFirst.run();
        firstFinished = true;
        this.notifyAll();
    }

    public synchronized void second(Runnable printSecond) throws InterruptedException {
        while (!firstFinished) {
            this.wait();
        }
        
        // printSecond.run() outputs "second". Do not change or remove this line.
        printSecond.run();
        secondFinished = true;
        this.notify();
    }

    public synchronized void third(Runnable printThird) throws InterruptedException {
        while (!secondFinished) {
            this.wait();
        }
        
        // printThird.run() outputs "third". Do not change or remove this line.
        printThird.run();
    }
}
```

```cpp
// cpp版。
class Foo {
public:
    int count = 0;
    mutex mtx;
    condition_variable cv;
    Foo() {
        count = 1;
        //cv.notify_all();
    }

    void first(function<void()> printFirst) {
        
        unique_lock<mutex> lck(mtx);
		// No point of this wait as on start count will be 1, we need to make the other threads wait.
        // while(count != 1){
        //     cv.wait(lck);
        // }
        // printFirst() outputs "first". Do not change or remove this line.

        printFirst();
        count = 2;
        cv.notify_all();
    }

    void second(function<void()> printSecond) {
        unique_lock<mutex> lck(mtx);
        while(count != 2){
            cv.wait(lck);
        }
        // printSecond() outputs "second". Do not change or remove this line.
        printSecond();
        count = 3;
        cv.notify_all();
    }

    void third(function<void()> printThird) {
        unique_lock<mutex> lck(mtx);
        while(count != 3){
            cv.wait(lck);
        }
        // printThird() outputs "third". Do not change or remove this line.
        printThird();
    }
};
```

