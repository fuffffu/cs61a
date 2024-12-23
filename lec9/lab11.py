(define (if-program condition if-true if-false)
    '(if ,(condition) ,(if-true) ,(if-false))
)

(define (square n) (* n n))

(define (pow-expr base exp)
    (cond (= exp 0) 1)
          (= exp 1) '(,base 1))
          (= (% exp 2) 0) (list 'square(power-expr base (/ exp 2)))
          (else (list '(* base (list 'square(power-expr base (/ (- exp 1) 2)))))
#scheme中都好用于引号后面进行求值插入，这里是递归
#list用于动态地构造表达式，因为它生成的是一个数据结构。当没有list的时候，square以及后面的内容只是符号，他只会返回square而不会执行square函数
#如果使用List,因为它是一种数据结构，它会将传入的参数进行求值，并创造出一个包含这些值的列表。
(define-macro (repeat n expr)
  `(repeated-call ,n (lambda () ,expr)))

; Call zero-argument procedure f n times and return the final result.
(define (repeated-call n f)
  (if (= n 1) (f) (begin (f)repeat-call (- n 1) (f))))
#用括号包括函数名，表示调用该函数
#repeat-call前面不用加引号，因为我们是要调用函数，而不是作为符号。
#上一个square,是为了返回一个表达式，如果去掉引号会立即求值变成平方。上一个递归调用pow-exp也没有加引号，是为了让调用起作用。