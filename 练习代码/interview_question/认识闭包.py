

#  闭包

# 我们有时候需要在函数外部得到函数内的局部变量。
# 但是，由于Python中作用域的搜索顺序（"链式作用域"结构（chain scope）：
# 子对象会一级一级地向上寻找所有父对象的变量），这一点通常是无法实现的。
# 定义：闭包就是能够读取外部函数内的变量的函数。（前面已经讲解过）
# 作用1：闭包是将外层函数内的局部变量和外层函数的外部连接起来的一座桥梁。（下一部分讲解）
# 作用2：将外层函数的变量持久地保存在内存中。（下一部分讲解）

# def f1():
#     n = 999
#
#     def f2():
#         print(n)
#
#     return f2
#
#
# result = f1()
# result()



def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())


# 打印结果如下
# 9
# 9
# 9
# 原因：在向列表中添加 func 的时候，i 的值没有固定到f的实例对象中，
# 而仅是将计算公式固定到了实例对象中。等到了调用f1()、f2()、f3()的时候才去取 i的值，
# 这时候循环已经结束，i 的值是3，所以结果都是9

def count2():
    fs= []
    def f(i):
        def g():
            return i*i
        return g

    for j in range(1, 4):
        fs.append(f(j))
    return fs


f4, f5, f6 = count2()
print(f4())
print(f5())
print(f6())

# 再创建一个函数，用该函数的参数绑定循环变量当前的值，
# 无论该循环变量后续如何更改，已绑定到函数参数的值不变

# 打印结果如下
# 1
# 4
# 9