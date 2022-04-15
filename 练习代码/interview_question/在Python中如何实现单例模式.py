"""
单例模式定义：为了不浪费系统资源，确保一个类只能生成一个实例

"""
# class A(object):
#     a = 1
#
#     def __init__(self, x=0):
#         self.x = x

# 方法1：使用装饰器


def single(cls):
    _instance = {}

    def _single(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
            return _instance[cls]
    return _single

def Singleton(cls):
    _instance = {}

    def _singleton(*args, **kargs):
        if cls not in _instance:
            _instance[cls] = cls(*args, **kargs)
        return _instance[cls]

    return _singleton


@Singleton
class A(object):
    a = 1

    def __init__(self, x=0):
        self.x = x



a1 = A(2)
a2 = A(3)
print(a1)
print(a2)
