# @property
# 继承,重写


class MyFirstClass(object):

    def __init__(self, a):
        self.a = a

    def sum(self, b):
        return self.a + b

    @classmethod
    # classmethod 修饰符对应的函数不需要实例化，不需要 self 参数
    # 但第一个参数需要是表示自身类的 cls 参数，可以来调用类的属性，类的方法，实例化对象等。
    def setA(cls, a):
        return cls(a)

    @staticmethod
    # 不用实例化，可以直接调用方法
    def add(a, b):
        return a + b

    @property
    # 方法转成属性
    def getProA(self):
        return self.a

    def getA(self):
        return self.a
    # 要实例化才能


if __name__ == '__main__':
    c1 = MyFirstClass(100)
    print(c1.sum(20))
    print(c1.getA() == c1.getProA)
    print(MyFirstClass.setA(10).sum(100) == c1.setA(10).sum(100))
    print(MyFirstClass.add(1, 20))
    print(MyFirstClass.add(2, 3))