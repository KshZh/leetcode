# 1115. Print FooBar Alternately

> Suppose you are given the following code:
>
> ```
> class FooBar {
>   public void foo() {
>     for (int i = 0; i < n; i++) {
>       print("foo");
>     }
>   }
> 
>   public void bar() {
>     for (int i = 0; i < n; i++) {
>       print("bar");
>     }
>   }
> }
> ```
>
> The same instance of `FooBar` will be passed to two different threads. Thread A will call `foo()` while thread B will call `bar()`. Modify the given program to output "foobar" *n* times.
>
>  
>
> **Example 1:**
>
> ```
> Input: n = 1
> Output: "foobar"
> Explanation: There are two threads being fired asynchronously. One of them calls foo(), while the other calls bar(). "foobar" is being output 1 time.
> ```
>
> **Example 2:**
>
> ```
> Input: n = 2
> Output: "foobarfoobar"
> Explanation: "foobar" is being output 2 times.
> ```

1. Medium。

```java
// 因为信号量计数为0时，递减会阻塞。
// 所以一般对于计数器+条件变量的场景，可以直接用计数信号量代替，代码会简单一些。
// 信号量一般用来同步对资源访问，当前是否可执行也可以算是一种资源。
class FooBar {
    private int n;
    private Semaphore fooStart = new Semaphore(1);
    private Semaphore barStart = new Semaphore(0);

    public FooBar(int n) {
        this.n = n;
    }

    public void foo(Runnable printFoo) throws InterruptedException {
        
        for (int i = 0; i < n; i++) {
            fooStart.acquire();
        	// printFoo.run() outputs "foo". Do not change or remove this line.
        	printFoo.run();
            barStart.release();
        }
    }

    public void bar(Runnable printBar) throws InterruptedException {
        
        for (int i = 0; i < n; i++) {
            barStart.acquire();
            // printBar.run() outputs "bar". Do not change or remove this line.
        	printBar.run();
            fooStart.release();
        }
    }
}
```

```java
// 用条件变量则麻烦一点。
class FooBar {

    private int n;
    //flag 0->foo to be print  1->foo has been printed
    private int flag=0;
    ReentrantLock reentrantLock= new ReentrantLock();
    Condition fooPrintedCondition=reentrantLock.newCondition();
    Condition barPrintedCondition=reentrantLock.newCondition();

    public FooBar(int n) {
        this.n = n;
    }

    public void foo(Runnable printFoo) throws InterruptedException {
        
        for (int i = 0; i < n; i++) {
            try {
                reentrantLock.lock();
                while (flag ==1){
                    barPrintedCondition.await();
                }
                // printFoo.run() outputs "foo". Do not change or remove this line.
                printFoo.run();
                flag=1;
                fooPrintedCondition.signalAll();
            } catch (InterruptedException e) {
                e.printStackTrace();
            } finally {
                reentrantLock.unlock();
            }
        }
    }

    public void bar(Runnable printBar) throws InterruptedException {
        
        for (int i = 0; i < n; i++) {
            reentrantLock.lock();
            while (flag==0){
                fooPrintedCondition.await();
            }
            // printBar.run() outputs "bar". Do not change or remove this line.
        	printBar.run();
            flag=0;
        	barPrintedCondition.signalAll();
        	reentrantLock.unlock();
        }
    }
}
```

