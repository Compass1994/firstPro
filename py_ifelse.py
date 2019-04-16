# python条件控制

num1 = 0
# 1相当于true，0相当于false
print("不做任何比较的情况下判断")
if num1:
    print("true,说明条件是true")
else:
    print('条件是0，或者是false')

# python中是没有switch – case的，多重条件判断使用以下写法
age = int(input("请输入你的年龄"))
print("")
if age < 0:
    print("are you kiding me!")
elif 0 < age <= 18:  # 很人性化的写法
    print("未成年！")
elif 18 < age <= 55:  # 还算强壮
    print("青壮年")
elif 55 < age <= 100:  # 你老了
    print("你老了")
else:
    print("祝长寿")
