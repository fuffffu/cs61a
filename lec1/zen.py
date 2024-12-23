from urllib.request import urlopen
import re
def shakesoeare():
    shakespeare = urlopen('http://inst.eecs.berkeley.edu/~cs61a/fa11/shakespeare.txt')
    text = shakespeare.read().decode()
    words=set(re.findall(r'^\w+$',text.lower()))
    print({w for w in words if len(w) >= 5 and w[::-1] in words})
#urlopen从网上获取数据，但是是二进制。read读取decode进行解码
#set用于去重,findall找到所有匹配模式并返回一个列表。\b是单词边界，\w+匹配所有字母、数字、下划线