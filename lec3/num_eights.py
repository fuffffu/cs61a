def num_eights(n):
    if n<8:
       return 0
    else:
        num = 1 if n%10 == 8 else 0 #不是8的因数而是余数是8
        return num + num_eights(n//10)
        
def digit_distance(n):
    if n>10:
        last=n%10
        second_last=(n//10)%10
        distance=abs(last-second_last)
        return distance+digit_distance(n//10)
    else:
        return 0
#你需要循环什么功能，就在return 里面递归什么功能，需要累加就前面加


def interleaved_sum(n, odd_func, even_func):
    if n<1:
         return 0
    elif n%2==0:
            return even_func(n)+interleaved_sum(n-1,odd_func,even_func)
    else:
        return odd_func(n)+interleaved_sum(n-1,odd_func,even_func)



def next_larger_dollar(bill):
    """Returns the next larger bill in order."""
    if bill == 1:
        return 5
    elif bill == 5:
        return 10
    elif bill == 10:
        return 20
    elif bill == 20:
        return 50
    elif bill == 50:
        return 100
    
def count_dollars_upward(total,bill=1):
    if total==0:
        return 1
    elif total<0 or bill is None:
        return 0

    return count_dollars_upward(total-bill,bill)+count_dollars_upward(total,next_larger_dollar(bill))

def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    if n==1:
        print_move(start,end)
    else:
        middle=6-start-end
        print_move(start,end)#这里n只剩下一个了，后续递归时先移动可以达成大的在小的之下的效果
        move_stack(n-1,middle,end)


from operator import sub, mul

def make_anonymous_factorial():
    fact=lambda n:1 if n==1 else mul(n,fact(sub(n,1)))
#一般都在缩小数据规模并要循环的地方加递归