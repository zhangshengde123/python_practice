


"""
#面对对象进阶：对python中的面对对象编程进行更为深入的了解
#装饰器作用：由于python中熟悉和方法访问权限的问题，虽然我们不建议价格熟悉设置为私有，但是如果直接将属性暴露给外界也是有问题的，不然我们没有办法
办法检查赋给熟悉的值是否有效。我们之前的建议是将属性命名已单下划线开头，通过这种方式来按时属性是受保护的，不建议外界直接访问，
那么如果想访问属性可以通过属性的getter和setter方法进行对应的操作。如果要做到这段，就可以考虑使用@property包装器来包装getter和setter
方法，使得对属性的访问既安全又方便



"""
"""1.property装饰器"""

# class Person(object):
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#
#     @property
#     def name(self):
#         return self._name
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, age):
#         self._age = age
#     def watch(self, book):
#         if self._age >14:
#             print(f'{self._name}可以在看{book}')
#         else:
#             print(f'{self._name}不能看{book}')

# def main():
#     person = Person('王大锤', 12)
#     person.watch("西游记")
#     person.age = 22
#     person.watch("西游记")
#
# if __name__ == '__main__':
#     main()


"""  2. __slot__魔法"""

# class Person(object):
#
#     # 限定Person对象只能绑定_name, _age和_gender属性
#     __slots__ = ("_name", '_age', '_gender')
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#
#     @property
#     def name(self):
#         return self._name
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, age):
#         self._age = age
#     def watch(self, book):
#         if self._age >14:
#             print(f'{self._name}可以在看{book}')
#         else:
#             print(f'{self._name}不能看{book}')
#
# def main():
#     person = Person('王大锤', 12)
#     person.watch("西游记")
#     person.age = 22
#     person.watch("西游记")
#     person._gender = '男'
#     person._from = '北京'
#
# if __name__ == '__main__':
#     main()
"""           3.   静态方法 
     之前，我们在类中定义的方法都是对象方法，也就是说这些方法都是发送给对象的消息。
     实际上，我们写在类中的方法并不需要都是对象方法，例如我们定义一个“三角形”类，通过传入三条边长来构造三角形，
     并提供计算周长和面积的方法，但是传入的三条边长未必能构造出三角形对象，因此我们可以先写一个方法来验证三条边长是否可以构成三角形，
     这个方法很显然就不是对象方法，因为在调用这个方法时三角形对象尚未创建出来（因为都不知道三条边能不能构成三角形）
     ，所以这个方法是属于三角形类而并不属于三角形对象的。我们可以使用静态方法来解决这类问题，代码如下所示。                 
"""

#1
# from math import sqrt
# class Triangle(object):
#     def __init__(self, a, b, c):
#         self._a = a
#         self._b = b
#         self._c = c
#     @staticmethod
#     def is_valid(a, b, c):
#         return a + b > c and a + c > b and b + c > a
#
#     def perimeter(self):
#         return self._a + self._b + self._c
#     def area(self):
#         half = self.perimeter()/2
#         return sqrt(half*(half - self._a) * (half - self._b) * (half - self._c))
#
# def main():
#     a, b, c = 3, 4, 5
#     # 静态方法和类方法都是通过给类发消息来调用的
#     if Triangle.is_valid(a, b, c):
#         t = Triangle(a, b, c)
#         print(t.perimeter())
#         # 也可以通过给类发消息来调用对象方法但是要传入接收消息的对象作为参数
#         # print(Triangle.perimeter(t))
#         print(t.area())
#         # print(Triangle.area(t))
#     else:
#         print('无法构成三角形.')
#
#
# if __name__ == '__main__':
#     main()


# from time import time,sleep,localtime
#
#
# class Clock(object):
#     """定义一个数字时钟类"""
#     def __init__(self, hour=0, minute=0, second=0):
#         self._hour = hour
#         self._minute = minute
#         self._second = second
#     @classmethod
#     def nowtime(cls):
#         ctime = localtime(time())
#         return cls(ctime.tm_hour, ctime.tm_min, ctime.tm_sec)
#
#
#     def run(self):
#         """展示时间"""
#         self._second += 1
#         if self._second == 60:
#             self._second = 0
#             self._minute += 1
#             if self._minute == 60:
#                 self._minute = 0
#                 self._hour += 1
#                 if self._hour == 24:
#                     self._hour = 0
#
#     def showtime(self):
#         return '%02d:%02d:%02d' % \
#                (self._hour, self._minute, self._second)
#
# def main():
#     clock = Clock.nowtime()
#     while True:
#         print(clock.showtime())
#         sleep(1)
#         clock.run()
#
# if __name__ == '__main__':
#     main()

"""  4. 继承与多态
在已有类的基础上创建新类，这其中的一种做法就是让一个类从另一个类那里将属性和方法直接继承下来，
从而减少重复代码的编写。提供继承信息的我们称之为父类，也叫超类或基类；得到继承信息的我们称之为子类，也叫派生类或衍生类。
子类除了继承父类提供的属性和方法，还可以定义自己特有的属性和方法，
所以子类比父类拥有的更多的能力，在实际开发中，我们经常会用子类对象去替换掉一个父类对象，
这是面向对象编程中一个常见的行为，对应的原则称之为里氏替换原则
"""
# class Person(object):
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#
#     @property
#     def name(self):
#         return self._name
#
#     @property
#     def age(self):
#         return self._age
#
#     @age.setter
#     def age(self, age):
#         self._age = age
#     def watch(self, book):
#         if self._age >14:
#             print(f'{self._name}可以在看{book}')
#         else:
#             print(f'{self._name}不能看{book}')
#
#
# class Student(Person):
#     def __init__(self,name, age, score):
#         super().__init__( name, age)
#         self._score = score
#
#     @property
#     def score(self):
#         return self.score
#     @score.setter
#     def score(self, score):
#         self._score = score
#
#     def study(self,course):
#         print(f"{self._score}分的{self.name}正在学习{course}")
#
#
#
# def main():
#     student1 = Student('王大锤', 12, 90)
#     student1.study("高等数学")
#     student1._score = 60
#     student1.study("高等数学")
#
# if __name__ == '__main__':
#     main()


"""
子类在继承了父类的方法后，可以对父类已有的方法给出新的实现版本，
这个动作称之为方法重写（override）。通过方法重写我们可以让父类的同一个行为在子类中拥有不同的实现版本，
当我们调用这个经过子类重写的方法时，不同的子类对象会表现出不同的行为，这个就是多态（poly-morphism）。
"""
# from abc import abstractmethod,ABCMeta
#
#
# class Pet(object, metaclass=ABCMeta):
#
#     def __init__(self, nickname):
#         self.nickname = nickname
#
#     @abstractmethod
#     def make_voice(self):
#         print(f'{self.nickname}: 呜呜呜')
#
#
# class Dog(Pet):
#
#
#     def make_voice(self):
#         print(f'{self.nickname}: 汪汪汪')
#
#
# def main():
#     dog = Dog("小七")
#     dog.make_voice()
#
# if __name__ == '__main__':
#     main()
"""                                       案例1                                   """

from abc import ABCMeta,abstractmethod
from random import randint,randrange

class Fighter(object, metaclass=ABCMeta):

    __slots__ = ('_name', '_hp', '_mp')
    def __init__(self, name, hp):
        self._name = name
        self._hp = hp
    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @name.setter
    def name(self, name):
        self._name = name

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp >= 0 else 0

    @property
    def alive(self):
        return self._hp > 0

    @abstractmethod
    def attack(self,other):
        """攻击"""
        pass

class Ulterman(Fighter):
    """凹凸曼"""
    def __init__(self, name, hp, mp):
        """初始化"""
        super().__init__(name, hp)
        self._mp = mp

    def attack(self, other):
        other.hp -= randint(10, 15)

    def huge_attack(self,other):
        if self._mp >= 50:
            self._mp -= 50
            injury = other.hp * 3//4
            injury = injury if injury >= 50 else 50
            other.hp -= injury
            return True
        else:
            self.attack(other)
            return False

    def magic_attack(self, ohters):
        """范围性魔法攻击"""
        if self._mp >= 20:
            self._mp -= 20
            for temp in ohters:
                if temp.alive:
                    temp.hp -= randint(10, 15)
            return True
        else:
            return False

    def resume(self):
        inc_point = 20
        self._mp += inc_point
        return self._mp

    def __str__(self):
        return '%s凹凸曼 \n' % self._name + \
            '生命值:%d\n' % self._hp + \
            '魔法值:%d\n' % self._mp


class Monster(Fighter):
    __slots__ = ('_name','_hp')

    def attack(self, other):
        other.hp -= randint(10, 20)

    def __str__(self):
        return '~~~%s小怪兽~~~\n' % self._name + \
            '生命值: %d\n' % self._hp

def is_any_alive(monsters):
    for monster in monsters:
        if monster.alive >0:
            return True
    return False

def select_alive_one(monsters):
    monsters_len = len(monsters)
    while True:
        index = randrange(monsters_len)
        monster = monsters[index]
        if monster.alive > 0:
            return monster

def display_info(ulterman, monsters):
    """显示凹凸曼和怪兽信息"""
    print(ulterman)
    for monster in monsters:
        print(monster, end=" ")




def main():
    u = Ulterman('迪迦', 1200, 300)
    m1 = Monster('鳄鱼',300)
    m2 = Monster('鸟人',300)
    m3 = Monster('大笨熊',300)
    ms = [m1, m2, m3]
    fight_round = 1
    while u.alive and is_any_alive(ms):
        print('========第%02d回合========' % fight_round)
        m = select_alive_one(ms)  # 选中一只小怪兽
        skill = randint(1, 10)  # 通过随机数选择使用哪种技能
        if skill <= 6:  # 60%的概率使用普通攻击
            print('%s使用普通攻击打了%s.' % (u.name, m.name))
            u.attack(m)
            print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
        elif skill <= 9:  # 30%的概率使用魔法攻击(可能因魔法值不足而失败)
            if u.magic_attack(ms):
                print('%s使用了魔法攻击.' % u.name)
            else:
                print('%s使用魔法失败.' % u.name)
        else:  # 10%的概率使用究极必杀技(如果魔法值不足则使用普通攻击)
            if u.huge_attack(m):
                print('%s使用究极必杀技虐了%s.' % (u.name, m.name))
            else:
                print('%s使用普通攻击打了%s.' % (u.name, m.name))
                print('%s的魔法值恢复了%d点.' % (u.name, u.resume()))
        if m.alive > 0:  # 如果选中的小怪兽没有死就回击奥特曼
            print('%s回击了%s.' % (m.name, u.name))
            m.attack(u)
        display_info(u, ms)  # 每个回合结束后显示奥特曼和小怪兽的信息
        fight_round += 1
    print('\n========战斗结束!========\n')
    if u.alive > 0:
        print('%s奥特曼胜利!' % u.name)
    else:
        print('小怪兽胜利!')


if __name__ == '__main__':
    main()






    



















