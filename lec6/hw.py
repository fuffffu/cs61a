class VendingMachine:
    def __init__(self,commodity,price):
      self.remainder=0
      self.balance=0
      self.commofity=commodity
      self.price=price

    def vend(self):
        if self.remainder==0:
           return("Nothing left to vend. Please restock.")
        
        difference=self.price-self.balance
        if difference>0:
           return(f"Please add ${difference} more funds")
        else:
            self.remainder-=1
            self.balance=0
            message=f'Here is your {self.commodity}'
            if difference==0:
                return(message)
            else:
                return(f"{message} and ${-difference} change")
   
    def add_funds(self,n):
        if self.stock == 0:
            return f'Nothing left to vend. Please restock. Here is your ${n}.'
        self.balance=self.balance+n
        return(f"Current balance: ${self.balance}")
      #这个money是客人放进去的，不是贩卖机自带的。贩卖机自带的只有balance
      #只用一次的变量，原：amount、money改成n就行
    def restock(self,n):
        self.remainder+=n
        print(f"Current {self.commodity} stock: {self.remainder}")
   


def store_digits(n):
    s=Link.empty#通过初始化 result = Link.empty，它能在一个循环中构造整个链表，不需要额外处理第一个节点。
    while n>0:
        s=Link(n%10,s)#第一个参数与第二个参数连起来，第一个在前，第二个在后
        n//=10
    return s
        

def deep_map_mut(func, lnk):
    if lnk is Link.empty:
        return #什么也不加表示递归终止的条件
    if isinstance(lnk.first,Link):#有可能会是列表套列表的情况
        deep_map_mut(func,lnk.rest)
    else:
        lnk.first=func(lnk.first)
    deep_map_mut(func,lnk.rest)


def two_list(vals, counts):
    s=Link.empty
    vals.reverse()
    counts.reverse()
    for _ in range(len(counts)):
        for _ in range(counts[i]):#整数for循环需要加上range
            s=Link(vals[i],s)#往列表里加节点，请记住    
    return s
#写法2for i in range(len(vals) - 1, -1, -1): 倒序遍历代替reverse
#range(start, stop, step) range(len(vals))-1意味着从列表的最后一个元素开始,stop=-1遍历到索引为0的元素，step=-1意味着向前遍历，正1向后遍历        