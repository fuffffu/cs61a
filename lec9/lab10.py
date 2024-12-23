def calc_eval(exp):
    """
    >>> calc_eval(Pair("define", Pair("a", Pair(1, nil))))
    'a'
    >>> calc_eval("a")
    1
    >>> calc_eval(Pair("+", Pair(1, Pair(2, nil))))
    3
    """
    if isinstance(exp, Pair):
        operator = exp.fisrt # UPDATE THIS FOR Q2
        operands = exp.rest # UPDATE THIS FOR Q2
        if operator == 'and': # and expressions
            return eval_and(operands)
        elif operator == 'define': # define expressions
            return eval_define(operands)
        else: # Call expressions
            return calc_apply(calc_eval(operator), operands.map(calc_eval)) # UPDATE THIS FOR Q2
    elif exp in OPERATORS:   # Looking up procedures
        return OPERATORS[exp]
    elif isinstance(exp, int) or isinstance(exp, bool):   # Numbers and booleans
        return exp
    elif exp in bindings: # CHANGE THIS CONDITION FOR Q4
        return bindings[exp]# UPDATE THIS FOR Q4

def floor_div(args):
    """
    >>> floor_div(Pair(100, Pair(10, nil)))
    10
    >>> floor_div(Pair(5, Pair(3, nil)))
    1
    >>> floor_div(Pair(1, Pair(1, nil)))
    1
    >>> floor_div(Pair(5, Pair(2, nil)))
    2
    >>> floor_div(Pair(23, Pair(2, Pair(5, nil))))
    2
    >>> calc_eval(Pair("//", Pair(4, Pair(2, nil))))
    2
    >>> calc_eval(Pair("//", Pair(100, Pair(2, Pair(2, Pair(2, Pair(2, Pair(2, nil))))))))
    3
    >>> calc_eval(Pair("//", Pair(100, Pair(Pair("+", Pair(2, Pair(3, nil))), nil))))
    20
    """
    (let ((a (car args))#Scheme中，赋值是使用define或let而不是等号（=）
          (b (cdr args)))
    (if (null? b) 
               a
               (floor_div (/ a (car b)))
    ))
     

scheme_t = True   # Scheme's #t
scheme_f = False  # Scheme's #f

def eval_and(expressions):
    """
    >>> calc_eval(Pair("and", Pair(1, nil)))
    1
    >>> calc_eval(Pair("and", Pair(False, Pair("1", nil))))
    False
    >>> calc_eval(Pair("and", Pair(1, Pair(Pair("//", Pair(5, Pair(2, nil))), nil))))
    2
    >>> calc_eval(Pair("and", Pair(Pair('+', Pair(1, Pair(1, nil))), Pair(3, nil))))
    3
    >>> calc_eval(Pair("and", Pair(Pair('-', Pair(1, Pair(0, nil))), Pair(Pair('/', Pair(5, Pair(2, nil))), nil))))
    2.5
    >>> calc_eval(Pair("and", Pair(0, Pair(1, nil))))
    1
    >>> calc_eval(Pair("and", nil))
    True
    """
    #我的初步构想
    #if  expressions is nil:
    #   return True  #空and的逻辑单元是true
    #else:
    #    val=calc_eval(expressions.first)
    #    if not val:
     #       return False
     #   return eval_and(expressions.rest)
    #问题:只提取first和second,如果存在嵌套会丢失掉剩余表达式
    #我采用先递归的思想，但是问题是and运算中关键是顺序，必须先处理表达式.这会更加有效率
    #"and"通过求值函数来决定
    #需要返回递归结果的情况：当你依赖递归调用的结果来完成当前层的逻辑时。例如，求和、查找、逻辑运算等场景，需要逐层将结果传递回去。
    #不需要返回递归结果的情况：当你递归的目的是执行某种操作，而不需要依赖下一层的返回值。例如，遍历、打印、或修改全局状态等操作。

    #呵呵递归已经是改良版本，但是对于列表来说迭代更安全。
    curr,val=expressions,rest
    while curr is not nil:
        val=calc_eval(curr.first)
        if val is False:
            return False
        curr=curr.rest
    return val
    


bindings = {}

def eval_define(expressions):
    """
    >>> eval_define(Pair("a", Pair(1, nil)))
    'a'
    >>> eval_define(Pair("b", Pair(3, nil)))
    'b'
    >>> eval_define(Pair("c", Pair("a", nil)))
    'c'
    >>> calc_eval("c")
    1
    >>> calc_eval(Pair("define", Pair("d", Pair("//", nil))))
    'd'
    >>> calc_eval(Pair("d", Pair(4, Pair(2, nil))))
    2
    """
    "*** YOUR CODE HERE ***"
    symbol = expressions.first
    if expressions.rest is nil:
        value = None
    else:
        value = calc_eval(expressions.rest.first)
    bindings[symbol]=value 
    return symbol
        

