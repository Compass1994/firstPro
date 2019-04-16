# 迭代器
# 迭代器是一个可以记住遍历的位置的对象。
# 迭代器只能向前不能后退
# 迭代器有两个基本的方法：iter() 和 next()。
import sys

lists = [1, 2, 3, 4]
it = iter(lists)
print(next(it))
print(next(it))

# 使用for遍历迭代器
list1 = ['a', 'b', 'c', 'd']
it = iter(list1)
for i in it:
    print(i, end=" ")


# 使用的yield构建生成器，生成器返回的是迭代器
def scqddq(n):
    a, b, conter = 0, 1, 0
    while True:
        if conter > n:
            return
        yield a
        a, b = b, a+b
        conter += 1


print(" ")
dd = scqddq(10)
while True:
    try:
        print(next(dd), end=" ")
    except StopIteration:
        sys.exit()


# 使用next遍历迭代器
print("")
list2 = ['aa', 'bb', 'cc', 'dd']
it = iter(list2)
while 1:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()


