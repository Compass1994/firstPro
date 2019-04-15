# 本文件研究python的基础语法
import keyword
'''
这是多行注释的写法
'''
# python中的关键字
print(keyword.kwlist)
# 采用缩进构建代码结构，如下
if True:
    print('这是True的输出')
else:
    print("这是False的输出")
# 单行过长时使用 / 进行换行，但是在[],{},()中则不需要 / 换行
num_int = 0  # 整数(包括长整数)类型int
bool_tf = True  # 布尔类型bool
num_float = 1.2  # 浮点类型float
num_complex = 1 + 2j  # 复数类型complex
# print("num_int"+num_int+";bool_tf:"+bool_tf+";num_float:"+num_float+";num_complex:"+num_complex)
# 如果直接拼接会报错，数字和字符串数据类型不同，所以不能直接拼接(不像JS)
# 使用str()进行转换
print("num_int" + str(num_int) + ";bool_tf:" + str(bool_tf) +
      ";num_float:" + str(num_float) + ";num_complex:" + str(num_complex))
str_zf = "使用r可以将字符串中的转义字符不起作用\n"
print(str_zf)
print(r"使用r可以将字符串中的转义字符不起作用\n")
print("这是结尾，起查看换行效果的作用")
# 字符串的截取写法
czzf = "要截取此字符串中的字符abcdefgh"
print("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓字符串截取begin↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓")
print(czzf[2:-1])
print(czzf[0:6])
print(czzf[3])
print(czzf[3:])
print(czzf*2)
print("↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑字符串截取end↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑")
print("此输出不会换行", end="")
print("此输出不会换行", end="1")
# import 整个模块
# import 整个模块 from 函数1,函数2，函数3
# help为一个很有用可以查看帮助文档的方法
# help(max)
# python的多变量赋值 两种写法 如下
a = b = c = 0
e, f, g = 1, 1.2, "我是字符串"
print("\n")
# 可是实现多变量输出，同时sep定义分隔方式
print(a, b, c, sep="#")
print(e, f, g, sep="\n")

# 以下进行python3中数据类型的解释
print("↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓python数据类型begin↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓")
'''
python3中标准的数据类型有：数字(Number)，字符串(String)，列表(List)，集合(Set)，元组(Tuple)，字典(dictionary)
不可变数据：Number,String,Tuple
可变数据：List,Set,dictionary
Number:int bool float complex(复数)
'''
# 使用type()查看数据类型
sjlx_a, sjlx_b, sjlx_c, sjlx_d = 1, 2.23, True, 2+2j
print(type(sjlx_a), type(sjlx_d), type(sjlx_c), type(sjlx_d), sep=";")
# 使用isinstance来判断数据类型
# type不会认为子类是父类的一种类型
# isinstance会认为子类是父类的一种类型
print(isinstance(sjlx_a, int), isinstance(sjlx_b, float),
      isinstance(sjlx_c, bool), isinstance(sjlx_d, complex), sep="\n")
# del用于删除对象引用，在python中赋值是赋予的对象的引用，参考  python如何删除一个对象
# python中的运算
# 加法(+)，减法(-)，乘法(*)，除法(/)，乘方(**)，取余(%)，除法取整(//)，除法取浮点型(/)
# 在python的混合运算中会把整数转换为浮点数，同时python支持复数，复数的实部和虚部都是浮点型。
# python中的索引 0 表示正数第一个；-1 表示倒数第一个。
# python中的列表(list)，列表是可变的，如此格式n=[a,b,c,d,e,f],n[2:3]输出的为c,输出规则参考以下实例
str_sjlx = ['a', 'b', 'c', 'd', 'e', 'f']
print(str_sjlx[2:5])  # ['c', 'd', 'e']
print(str_sjlx[2:-1])  # ['c', 'd', 'e']
print(str_sjlx[2:])  # ['c', 'd', 'e', 'f']
print(str_sjlx[:3])  # ['a', 'b', 'c']
print(str_sjlx[:])  # ['a', 'b', 'c', 'd', 'e', 'f']
# list是可以改变的，格式参照str_sjlx[2:5] = ['n', 'm', 'z']
# list截取中有第三个参数，为截取步长，如下
# 步长的意思为步子大小，即一次截取的间隔。
print(str_sjlx[1:5:2])  # ['b', 'd']
# 元组(tuple)和list相似，但是元组是不可变的，但是元组中的对象是可变的，元组使用()表示
tuple_yz = ('abcd', '1234', 1+2j, 12, 2.33)
tup1 = ()  # 空元组
tup2 = (123,)  # 元组中一个元素时要带逗号
# string list tuple都属于序列
# 集合set
set1 = {'abc', 'efg', 'qaz', 'wsx', 'edc'}
set2 = {'abc', 'efg', 1, 2.2}
# set自带基本功能包括成员检测和删除重复项，如下
set_a = set('aaaaaaaabcde')
print(set_a)
print(set1 - set2)  # 差集
print(set1 | set2)  # 并集
print(set2 & set1)  # 交集
print(set1 ^ set2)  # 两个集合中不同时存在的元素，我取名非交集
# 字典(dictionary) 类似java中的map,即像键值对的形式，使用{}，以下介绍一些个人没见过的写法
dict1 = dict([('key1', 1), ('key2', 2), ('key3', 3)])
dict2 = dict(key1=1, key2=2, key=3)
dict3 = {x: x**2 for x in (1, 2, 3)}
print(dict1, dict2, dict3)
# 创建空字符串使用{ }
# python支持数据类型转换
print("↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑python数据类型end↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑↑")
# python中的逻辑运算符 and or not
# python中的成员运算符 in, not in
# id()获取python对象的内存地址
# is 和 ==的区别: is 表示两个变量的引用对象是否相同； == 表示变量引用值是否相同。
# 关于各数据类型中的内置函数参考菜鸟教程中对应的数据类型解释。
# 可以使用append()方法向列表中添加元素，如下
listapp = ['1111', '33wde', 3, 'asbcsd']
# 上一行代码会出现一个警告，在listapp后方加入listapp.append()方法就会报这个错，具体原因不清楚。
listapp.append(5)
print(listapp)
# 当元组中只用一个元素是需要在元素后面加一个逗号，作用如下
tup1 = ('abcdd')
tup2 = ('abcdd',)
print(type(tup1))
print(type(tup2))
# 创建空集合必须用set()而不能用{ },因为{ }是用来创建
# 集合的添加元素
setthis = set()
setthis.update((1, 2, 3, 4), "zfc", {1, 3, 1+2j})  # 这里如果使用int和float会报错，但是如果写在元组或者集合中则没有问题。
print(setthis)


