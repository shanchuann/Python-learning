class Player(object):
    numbers = 0  # 类属性
    all_age = []  # 类属性

    def __init__(self,name,age,city):  # 初始化函数
        self.name = name  # 实例属性
        self.age = age
        self.city = city
        Player.numbers += 1  # 类属性自增1
        Player.all_age.append(age)  # 将年龄添加到类属性中

    def show(self):  # 实例方法
        print('name:',self.name)
        print('age:',self.age)
        print('city:',self.city)
        print('numbers:',Player.numbers)

    @classmethod
    def get_player_numbers(cls):  # 类方法
        print('numbers is:',cls.numbers)

    @classmethod
    def get_max_age(cls):
        max_damage = 0
        for i in cls.all_age:
            if i > max_damage:
                max_damage = i
        return max_damage

    @staticmethod
    def isvalid(**kwargs):
        if kwargs['age'] < 18:
            return False
        return True

infos = {'name':'Tom','age':18,'city':'Shanghai'}
if Player.isvalid(**infos):
    Tom = Player('Tom',18,'Shanghai')
else:
    print('No valid')