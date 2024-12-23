(define (over-or-under num1 num2)
    (cond 
        ((< num1 num2) -1)
        ((= num1 num2) 0)
        (else 1))
)

(define (make-adder num)
   (lambda (inc) (+ inc num))
)

(define (composed f g)
    (lambda (x) (f (g (x))))#lambda用法记得定义变量
)


(define (repeat f n)
    if (< n 1)
        (lambda (x) x) #n 小于 1 时，返回一个恒等函数 (lambda (x) x)
        (composed f (repeat f (- n 1)))) #composed先应用后面的函数，再应用前面的函数。
)

(define (max a b) (if (> a b) a b))  ;# 如果 a > b，则返回 a，否则返回 b
(define (min a b) (if (> a b) b a))  ;# 如果 a > b，则返回 b，否则返回 a

(define (gcd a b)
  (cond ((zero? a) b)  ; #如果 a 是 0，则最大公约数是 b(任何整数都可以整除 0)
        ((zero? b) a)  ; #如果 b 是 0，则最大公约数是 a
        ((=(modulo (max a b) (min a b)) 0) (min a b))  ; #如果 max(a, b) 能整除 min(a, b)，那么 min(a, b) 就是 GCD
        (else (gcd (min a b) (modulo (max a b) (min a b)))))) ; #否则，递归调用 gcd，传入 min(a, b) 和二者相除的余数
#