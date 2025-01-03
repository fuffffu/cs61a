#我的思路有什么问题吗？请指正并引导我思考，不要直接给我答案。
(define (pow base exp)
    """(if (=exp 0)
        1
        (* base (pow base (- exp 1)))))
    普通写法递归的调用次数是和 exp 成正比的。计算 2^32 会递归调用32次。"""
(define (square n)(* n n))
(define (pow base exp)
    (cond ((=exp 0) 1)
          ((even?exp)(square(pow base (/ exp 2))))
          (else (* base (pow base (- exp 1))))))
#奇数一切正常，偶数传入一半阶乘再quare。其实奇数还可指数-1先变成偶数，再乘2
#(else (* base (squre (pow base (/ exp 2))))))

(define (repeatedly-cube n x)
    (if (zero? n)
        x
        (let
            (y (repeatedly-cube n-1 x))
            (* y y y))))
#这里设计的是后立方，而我想的先立方。后立方主要是先缩小问题的规模(n-1),在递归返回的时候进行操作。
#后立方递归最深层其实是最简单、问题规模最小的时候。针对这道题最深层0已经跳出了递归，返回x即2。而我们对2要进行什么操作也就是在递归下面的语句，即立方。递归结果不断返回，最上面的一层才是最后的答案，浮出水面。
#前立方适合那些不需要回溯时处理结果、并且在递归过程中希望不断更新操作状态的问题。典型的应用场景包括在每次递归过程中逐步累加或改变状态，如 Fibonacci 数列的累加。
#对内存要求较高,如果递归层数较深，前立方递归会因为不断产生新结果，内存占用和递归栈深度可能会增大。
#后立方适合那些需要在递归完成后再进行一些计算或操作的场景。例如，在处理递归树结构时，先递归处理左右子树，返回后再汇总操作结果的场景非常适合后递归。计算的实际结果会延迟到递归的最顶层，可能在某些场景下不直观。

(define (cddr s)
  (cdr (cdr s)))

(define (cadr s)
   (car(cdr(s)))
)

(define (caddr s)
    (car(cddr(s)))
)