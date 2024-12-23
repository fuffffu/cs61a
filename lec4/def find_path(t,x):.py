def deep_map(f, s):
#如果元素是非列表的值（即基础类型，如整数），那么你可以直接应用函数 f。
#如果元素是一个列表，你就需要递归地对该列表中的每个元素继续应用相同的逻辑.遍历只能处理当前层,不能处理子列表，需要自己再写去遍历。
    for i in range(len(s)):
        if isinstance(s[i],list):#记住isinstance语法
            deep_map(f,s[i])
        else:
            s[i]=f(s[i])#有赋值，才能修改（原地）
    
#for i in s: i 只是当前列表中元素的一个副本，即 i 是指向该元素的一个值，而不是列表本身的元素。当你对 i 进行修改时，它不会影响到列表 s 中的原始元素，因为 i 并不是直接引用列表的某个位置。
#当你修改 i 的值时，它只是修改了 i 这个局部变量的内容，而不会修改原始列表 s。因此，列表 s 保持不变。
# for i in range(len(s)) 此时i是索引.这时你直接访问的是列表 s 中的特定位置，因此你可以修改该位置的内容。
# Python 中的列表是可变对象，这意味着列表本身可以被修改（如添加、删除元素）。但对于列表中的元素，如果是不可变对象（如整数、字符串、元组等），那么你不能直接修改这些元素。
#当你对不可变对象进行操作时，比如 i = i + 1，Python 实际上是创建了一个新的对象并将 i 绑定到这个新对象。这就是为什么直接通过元素遍历并不能修改列表中的值，因为你只是在操作副本，并没有修改原列表。
#通过索引访问列表中的元素时，确实可以直接修改列表中的内容。这是因为索引操作直接访问的是列表中某个位置的元素，而修改索引位置的元素会对列表本身产生影响。 
