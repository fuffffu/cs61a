(define (curry-cook formals body)
    (if (null? formals)
        body
    '(lambda (,(car formals) ,(curry-look (cdr formals) body))
)
#curry-cook 的功能是把一个多参数函数进行 柯里化（currying），也就是把一个接受多个参数的函数转化为一系列嵌套的单参数函数。当所有的参数都处理完了，也就是 formals 为空时，应该返回的就是最原始的 body.
#如果没有括号和逗号，写成 (lambda car formals) 是不合法的，因为 lambda 的语法要求参数是列表格式，也就是形如 (lambda (参数列表) 函数体)
#在 Scheme 中，body 是作为函数的函数体内容直接插入的。如果你给 body 加上括号，例如 '(body)，就会将它视作一个 列表，而不是表达式。这样会破坏表达式的结构，导致它无法正常求值。

#柯里化函数的工作方式。一个接受多个参数的函数，例如 f(x, y, z)，会被转换成一系列函数链：f(x)(y)(z)。
#这意味着当你给柯里化函数传递一个参数时，它会返回一个新的函数，这个新函数等待下一个参数。

#通过这样做，本来需要传入n个参数的复杂、重复步骤。我们可以固定部分参数，剩余参数灵活传递。
"""(define (add x y)
  (+ x y))

(define add5 (curry add 5))  ; 固定第一个参数为 5

(add5 3)  ; 结果为 8"""
#通过柯里化，函数可以变得更加模块化和灵活。
"""(define (format-output format data)
  (string-append format data))
#string-append 是scheme里的内置函数 起到字符串连接作用

(define greeting-format (curry format-output "Hello, "))
(greeting-format "Alice")  ; 结果为 "Hello, Alice"
(greeting-format "Bob")    ; 结果为 "Hello, Bob""""

#curry-consume 的目标是：它接受两个输入：一个柯里化函数 curry 和一个参数列表 args。
#它要用 args 里的参数来调用 curry，如果参数不够，就返回一个部分应用的函数；如果参数正好用完了，返回计算的最终结果。
(define (curry-consume curry args)
    (if (null? args) curry))#列表判空
    (curry (car args)
    (curry-consume (curry (cdr args)))
)
#在 Scheme 中，else 其实是用在 cond 表达式里的，而不是 if 语句中。如果你使用 if 语句的话，应该直接写出第二个分支（false-branch），而不是用 else。

# expr 的求值结果和 options 里的值进行匹配。找到匹配的那个值后，执行它对应的表达式。
scm> (define-macro (switch expr options)
                   (switch-to-cond (list 'switch expr options))
     )
#switch 宏，它的作用是将 switch 表达式转换为 cond 表达式。

(define (switch-to-cond switch-expr)
  (cons 'cond
    (map
      (lambda (option) (cons '(euqal? ,(car(cdr(swith-expr))) ,(car option)) (cdr option)))
      (car (cdr (cdr switch-expr))))))
#这个3c是和map一起用的.(map <procedure> <list1> <list2> ...)遍历 options 列表，并且对每个option应用lambda
#在 switch-to-cond 中已经在用 map 来遍历 options，目的是将每个 option 逐个转换为 cond 中的条件判断表达式。
#通过 cons，你可以一步步构建出一个符合 cond 格式的列表。
#(car(cad..)从内到外哒
"""效果图
scm> (switch-to-cond `(switch (+ 1 1) ((1 2) (2 4) (3 6))))
(cond ((equal? (+ 1 1) 1) 2) ((equal? (+ 1 1) 2) 4) ((equal? (+ 1 1) 3) 6))"""
#简单的数字 2、4、6 也是表达式