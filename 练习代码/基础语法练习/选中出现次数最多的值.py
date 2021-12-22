# class Human(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# class Student(object):
#
#     # __init__是一个特殊方法用于在创建对象时进行初始化操作
#     # 通过这个方法我们可以为学生对象绑定name和age两个属性
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def study(self, course_name):
#         print('%s正在学习%s.' % (self.name, course_name))
#
#     # PEP 8要求标识符的名字用全小写多个单词用下划线连接
#     # 但是部分程序员和公司更倾向于使用驼峰命名法(驼峰标识)
#     def watch_movie(self):
#         if self.age < 18:
#             print('%s只能观看《熊出没》.' % self.name)
#         else:
#             print('%s正在观看《海贼王》.' % self.name)
#
#
# def main():
#     student = Student("张胜德", 34)
#     student.study("数学")
#     student.watch_movue()
class Glass(object):
    def __init__(self,  color, capacity):
        self.color = color
        self.capacity = capacity
    def sell(self):
        if self.color == '黄色':
            print(f'{self.color}杯子的销量是100件')
        else:
            print(f"{self.color}杯子的销量是50件")

def main():
    glass = Glass("黄色", '100ml')
    glass.sell()




if __name__ == "__main__":
    main()
