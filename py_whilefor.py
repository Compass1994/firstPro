# python中的循环

# 写几个经典的简单例子

# 1.while实现九九乘法表
i = 1
while i <= 9:
    j = 1
    while j <= i:
        mut = j*i
        print("%d*%d=%d" % (i, j, mut), end="   ")
        j += 1
    print("")
    i += 1


# python冒泡排序
# range(n)表示在0到n之间取值
def mppx(li):
    maxa = 0
    for ad in range(len(li) - 1):
        for x in range(len(li) - 1 - ad):
            if li[x] > li[x + 1]:
                maxa = li[x]
                li[x] = li[x + 1]
                li[x + 1] = maxa
            else:
                maxa = li[x + 1]
    print(li)


mppx([41, 23344, 9353, 5554, 44, 7557, 6434, 500, 2000])

# 在python循环中照样可以使用break和continue
# 猜拳小游戏
import random

while 1:
    s = int(random.randint(1, 3))
    if s == 1:
        ind = "石头"
    elif s == 2:
        ind = "剪刀"
    elif s == 3:
        ind = "布"
    m = input("输入石头，剪刀，布，输入end结束游戏：")
    blist = ["石头", "剪刀", "布"]
    if (m not in blist) and (m != 'end'):
        print("输入错误，重试")
    elif (m == 'end') and (m not in blist):
        print(ind)
        print("游戏结束")
        break
    elif m == ind:
        print("平")
    elif (m == '石头' and ind == '剪刀') or (m == '剪刀' and ind == '布') or (m == '布' and ind == '石头'):
        print('电脑出了' + ind + "; 您赢了")
    else:
        print('电脑出了' + ind + "; 您输了")

