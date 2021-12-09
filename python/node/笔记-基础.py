# -----------文件备份-------------

"""
一. 接收用户输入的文件名
二. 处理文件名, 进行拆分 --> abc.txt  --> 新文件名 abc[复件].txt
三. 打开旧文件 --> 读取旧文件内容 --> 创建新文件 --> 写入新文件
"""
f = open("../python.txt", 'x')
f.close()

# 一. 接收用户输入的文件名
old_file_name = input("请输入要复制的文件名:")

# 二. 处理文件名, 进行拆分 --> abc.txt  --> 新文件名 abc[复件].txt
# 2.1 先查找小数点的索引位置
index = old_file_name.rfind('.')
print(index)

# 2.2 拆分文件名
first_name = old_file_name[:index]
last_name = old_file_name[index:]

# 2.3 拼接新的文件名
new_file_name = first_name + '[副本]' + last_name
print(new_file_name)

# 三. 打开旧文件 --> 读取旧文件内容 --> 创建新文件 --> 写入新文件
with open(old_file_name, 'r') as old_file:
    content = old_file.read()
    with open(new_file_name, 'w') as new_file:
        new_file.write(content)

"""
1. 实现任意格式的文件备份
2. 不能占用过高的内存
"""

# 一. 接收用户输入的文件名
# old_file_name = input("请输入要复制的文件名:")
#
# # 二. 处理文件名, 进行拆分 --> abc.txt  --> 新文件名 abc[复件].txt
# index = old_file_name.rfind('.')
# first_name = old_file_name[:index]
# last_name = old_file_name[index:]
# new_file_name = first_name + '[复件]' + last_name
# print(new_file_name)
#
# # 三. 打开旧文件 --> 读取旧文件内容 --> 创建新文件 --> 写入新文件
# with open(old_file_name, 'rb') as old_file:
#
#     # 希望分批读取 --> 循环读取--> 设置一定大小的读取的字符数
#     # 3.1 设置循环
#     while True:
#
#         # 3.2 每次读取小片的数据
#         content = old_file.read(1024)
#
#         # 3.3 判断是否获取了内容
#         if content:
#
#             # 3.4 读取到了就写入
#             with open(new_file_name, 'ab') as new_file:
#                 new_file.write(content)
#         else:
#             # 3.5 如果没有内容就终止
#             break
old_file_name = input("请输入要复制的文件名:")
index = old_file_name.rfind('.')
first_name = old_file_name[:index]
last_name = old_file_name[index:]
new_file_name = first_name + '[复件]' + last_name
print(new_file_name)
with open(old_file_name, 'rb') as old_file:
    while True:
        content = old_file.read(1024)
        if content:
            with open(new_file_name, 'ab') as new_file:
                new_file.write(content)
        else:
            break

# --------------文件相关操作-------------

# 导入模块，只需导入一次即可
import os
import shutil

"""1. 文件重命名"""
# 语法格式：os.rename(旧的文件名，新的文件名)
# os.rename('zhubo.txt', 'huizhubo.txt')

"""2. 删除文件"""
# 语法格式：os.remove(待删除的文件名)
# os.remove('huizhubo.txt')

"""3. 创建文件夹"""
# 语法格式：os.mkdir(文件夹的名字)
# os.mkdir('python')

"""4. 删除空文件夹"""
# 语法格式：os.rmdir(待删除文件夹的名字)
# os.rmdir('python')

"""5. 获取当前目录"""
# 语法格式：路径变量 = os.getcwd()
# c: current w: working d: dir
print(os.getcwd())

"""6. 改变默认目录"""
# 语法格式：os.chdir(改变的路径)
# ch:change
# 相当于图像化界面的双击进入文件夹 --> 切换路径
os.chdir('test')
print(os.getcwd())

"""7. 获取目录列表"""
# 语法格式：目录列表变量 = os.listdir(指定某个目录)
# 如果不指定目录，默认当前路径
# 以.开头的都是隐藏文件/文件夹  .idea: 项目创建后自动产生的工程的配置文件
# 以后注意当前路径所在位置, 然后再去获取目录列表
print(os.listdir('..'))
print(os.listdir('../..'))

"""8. 判断文件是否存在"""
# 语法格式：os.path.exists(需要判断的文件)
# 如果文件存在返回True，如果文件不存在返回False
if os.path.exists('demo'):
    print('存在demo目录')
else:
    print('不存在demo目录')

"""9. 强制删除"""
shutil.rmtree('demo')

# -----------文件批量重命名-------------
"""
1. 先创建一个文件夹
2. 循环创建一堆文件
3. 批量修改文件名
"""
import os
import shutil

# 0. 强制删除demo文件夹. 为了调试方便
if os.path.exists("demo"):
    shutil.rmtree("demo")

# 1. 先创建一个文件夹
os.mkdir("demo")

# 2. 切换路径
print(os.getcwd())
os.chdir('demo')
print(os.getcwd())

# 3. 循环创建一堆文件
for i in range(3):
    file_name = str(i + 1) + ".txt"
    with open(file_name, 'w'):
        pass

# 4. 批量修改文件名
# 4.1 获取目录下所有的文件名
dir_list = os.listdir()
print(dir_list)

# 4.2 循环重命名
for old_file_name in dir_list:
    new_file_name = '[黑马出品]-' + old_file_name
    print(old_file_name, new_file_name)
    os.rename(old_file_name, new_file_name)

# --------------字符串和列表相互转换--------------------

"""将列表保存到文件"""
# 列表
user_list = [{'name': 'mike', 'age': 34, 'tel': 110},
             {'name': 'yoyo', 'age': 30, 'tel': 120}]

"""将列表转换为字符串"""
with open('stu.db', 'w') as f:
    f.write(str(user_list))

"""将字符串转换为列表"""
# eval eval( 字符串内容 )	返回传入字符串内容的结果，字符串里面看到像是什么，就转换成什么
# 简单理解为:去掉字符串的引号, 然后根据实际内容推导类型

with open('stu.db', 'r') as f:
    content = f.read()
    print(type(content), content)

    # content = list(content)  # 不能使用list()来转换字符串.
    content = eval(content)
    print(type(content), content)

# ---------------类-----------------
"""
需求:
1. 在调用方法时, 能够打印谁能吃/喝  --> 需要在方法中获取自己的属性值
2. 在调用其中1个方法时, 能嵌套调用另一方方法

self作用：为了区分不同对象的属性和方法
self是什么: 就相当于 调用时的那个对象. --> 谁调用, 就是谁
"""

"""定义类"""


class Dog(object):
    def eat(self):
        self.drink()  # 嵌套调用另一个方法
        print(f'{self.name}能吃')

    def drink(self):
        print(f'{self.name}能喝')


dog = Dog()
dog.name = '旺财'
dog.age = 18
dog.eat()

dog2 = Dog()
dog2.name = '大黄'
dog2.age = 20
dog2.eat()


# # 定义类
class Dog(object):
    def print_info(self):
        print('测试self', id(self))


# # 创建对象1
dog1 = Dog()
#
# # 打印dog1的id
print("调用方法前", id(dog1))
#
# # dog1调用print_info, print_info的self就是dog1
# # 底层调用：print_info(dog1)， 解释器自动把dog1传给方法中的self
dog1.print_info()
#
print("调用方法后", id(dog1))

print('=' * 30)
# 创建对象2
dog2 = Dog()

print("调用方法前", id(dog2))
dog2.print_info()
print("调用方法后", id(dog2))

# --------------__init__参数的使用--------------
"""
init带参数的使用.
让创建对象和属性赋值合为一行, 并灵活的设置属性
"""


class Dog(object):
    def __init__(self, type='巨型犬', name='', age=0, house=''):
        """在init方法里, 设置一些公有属性和一些默认值属性"""
        self.type = type
        self.name = name
        self.age = age
        self.house = house

    def __str__(self):
        """在这里只需要写1次格式化的操作. 以后所有的对象使用会非常方便"""
        return f'类型是{self.type}, 姓名是{self.name}, 年龄是{self.age}, 地址是{self.house}'


# dog = Dog()
# dog.name = '旺财'
# dog.age = 18
# dog.house = '航都路18号'

dog = Dog('小型犬', '旺财', 18, '航都路18号')
print(dog.type, dog.name, dog.age, dog.house)

dog = Dog('小型犬', '旺财', house='航都路18号')
print(dog.type, dog.name, dog.age, dog.house)

"""
为了方便观察对象的属性值, 可以实现__str__方法
在print打印一个对象时, 会自动调用此方法
"""

dog = Dog('小型犬', '旺财', 18, '航都路18号')
print(dog)

dog2 = Dog('大型犬', '大黄', 18, '航都路18号')
print(dog2)

# -------------------案例:烤地瓜---------------------

"""
类: 由属性(变量) 方法(函数)

类名: 地瓜类 SweetPotato

属性:1. 状态 state  默认生的  --> 初始化方法中进行设置
    2. 烧烤总时间 cooked_time 默认0    --> 初始化方法中进行设置


方法:1. 烧烤 cook(self, time):
            # 累加时间
            self.cooked_time += time

            # 根据累加后的时间进行判断, 更改状态
            if [0, 3):
                state = "生的"
            elif [3,6):
                state = "半生不熟"
            elif [6,8):
                state = "熟了"
            elif [8,):
                state = "烤糊了"

    2. __str__:展示地瓜的状态和烧烤的总时间
    3. __init__:进行初始化的属性设置
"""

"""
地瓜可以添加佐料,如 盐、孜然、辣酱等
输出地瓜信息时，可以显示地瓜的状态、烧烤总时间、以及添加过的所有佐料

1. 添加 condiments 属性
2. 修改__str__()方法，在方法中使用condiments属性显示已添加的佐料
3. 定义add_condiments()方法
"""

"""定义地瓜类"""


class SweetPotato(object):

    def __init__(self):
        """init设置属性初始值"""
        self.state = '生的'
        self.cooked_time = 0
        # 1. 添加 condiments 属性
        self.condiments = []  # 空列表, 可以增加多种佐料

    def __str__(self):
        # 2. 修改__str__()方法，在方法中使用condiments属性显示已添加的佐料
        condiments_str = '、'.join(self.condiments)
        return f'地瓜的烧烤时间是{self.cooked_time}, 地瓜的状态是{self.state}, 添加的佐料是{condiments_str}'

    def add_condiments(self, condiment):
        # 3. 定义add_condiments()方法
        self.condiments.append(condiment)

    def cook(self, time):
        """根据烧烤时间的累加值, 进行状态的变化"""
        if time <= 0:
            print('烧烤时间不对')
            return

        self.cooked_time += time

        if 0 <= self.cooked_time < 3:
            self.state = '生的'
        elif 3 <= self.cooked_time < 6:
            self.state = '半生不熟'
        elif 6 <= self.cooked_time < 8:
            self.state = '熟了'
        else:
            self.state = '烤糊了'


"""测试地瓜类"""
sp = SweetPotato()
print(sp)

sp.cook(2)
sp.add_condiments('孜然')
print(sp)

sp.cook(2)
sp.add_condiments('辣酱')
print(sp)

sp.cook(2)
sp.add_condiments('奥力给')
print(sp)

sp.cook(2)
sp.add_condiments('芝士')
print(sp)

sp.cook(-2)
print(sp)

"""
家具类
    属性: 类型
         面积

    方法:  init: 设置属性
          str: 打印对象

房子类
    属性: 地址
         面积
         剩余面积

    方法: init: 设置属性
         str: 打印对象
         添加家具: 能添加就添加, 否则提示失败
"""

"""
需求：输出房子时，显示包含的所有家具的类型

1. Home类中添加 item_type_list 属性(家具类型列表)，用于记录所有家具对象

2. Home类的 __str__ 方法中, 打印家具的类型

3. Home类的 add_item 方法中, 将添加成功的 家具类型 添加到 item_type_list 中
"""

"""家具类"""


class Item(object):
    def __init__(self, type='', area=0):
        self.type = type  # 家具类型
        self.area = area  # 家具面积

    def __str__(self):
        return f'家具的类型是{self.type}, 家具的面积是{self.area}'


"""房子类"""


class House(object):
    def __init__(self, address, area):
        self.address = address  # 房子地址
        self.area = area  # 房子面积
        self.free_area = area  # 剩余面积 = 房子面积
        # 1. Home类中添加 item_list 属性(家具类型列表)，用于记录所有家具对象
        self.item_list = []  # 保存添加的家具对象

    def __str__(self):
        # 2. Home类的 __str__ 方法中, 打印家具的类型
        item_type_list = [item.type + str(item.area) for item in self.item_list]
        item_str = '、'.join(item_type_list)
        return f'房子的地址是{self.address}, 房子的面积是{self.area}, 房子的剩余面积是{self.free_area}, 添加的家具有{item_str}'

    def add_item(self, item):
        # 房子剩余面积 > 家具的面积, 能添加就减少剩余面积
        if self.free_area >= item.area:
            print('添加成功')
            # 3. Home类的 add_item 方法中, 将添加成功的 家具类型 添加到 item_list 中
            self.item_list.append(item)
            self.free_area -= item.area
        else:
            print('添加失败, 剩余面积不足')


"""测试"""
house = House('航都路18号', 200)
print(house)

item = Item('椅子', 1)
print(item)

item2 = Item('桌子', 150)
print(item2)

item3 = Item('双人床', 50)
print(item3)

house.add_item(item)  # 让房子添加家具, 添加成功, 剩余面积会减少
house.add_item(item2)  # 让房子添加家具, 添加成功, 剩余面积会减少
house.add_item(item3)  # 让房子添加家具, 添加成功, 剩余面积会减少
print(house)

# -----------------私有属性----------------------

"""
如果在属性名前面加了2个下划线'__'，则表明该属性是私有属性，否则为公有属性
私有属性只能在类的内部访问
"""

"""
需求: 
定义一个Dog类, 能记录小狗数量, 以及能生小狗, 生完小狗休息三个月
"""


class Dog(object):
    def __init__(self):
        # baby_count: 狗宝宝的数量
        # 外界不需要修改狗宝宝的数量, 因此我们可以把它变成私有属性
        self.__baby_count = 0

    def birth(self):
        """生小狗的方法"""
        self.__baby_count += 1

        # 类的内部可以访问私有属性
        print(self.__baby_count)
        # 类的内部可以访问私有方法
        self.__leave()

    def __leave(self):
        """休产假的方法"""
        print("休息三个月")


dog = Dog()
dog.birth()
dog.birth()
# dog.__leave()  # 类的外部无法访问私有方法
# dog.__baby_count()  # 类的外部无法访问私有属性


"""扩展: 如何获取私有属性和方法"""
"""
Python没有绝对的私有, 只是系统把属性和方法名, 加了前缀(_类名)进行区分. 
所以如果非要获取私有, 是可以实现的. 实际开发中不要这么干
"""
print(dog._Dog__baby_count)
dog._Dog__leave()

# -----------------继承----------------

"""
单继承：子类只继承一个父类
多继承: 子类有多个父类(实际开发中, 多继承用的不多)

多层继承：继承关系为多层传递，如生活中的爷爷、父亲、儿子. 可以通过多层继承来间接实现多继承(Java就是这样的方式)
        一脉单传, 每一层都是单继承, 实现多层就是多层继承



多继承的语法格式：

class 子类名(父类1, 父类2, ……)：
    pass
"""

"""单继承"""


# 定义一个父类， Animal
class Animal(object):
    def eat(self):
        print('吃东西')


# 定义一个子类，只有一个父类
class Dog(Animal):
    pass


# 创建一个子类对象
dog1 = Dog()
dog1.eat()
print('*' * 50)

"""多继承"""


# 定义2个类，它们没有继承关系，是平级的
class SmallDog(object):
    def eat(self):
        print('吃小东西')


# 再定义一个类
class BigDog(object):
    def drink(self):
        print('大口喝水')


# 定义一个子类，多继承于上面2个父类
class SuperDog(SmallDog, BigDog):
    pass


# 定义子类对象，调用方法
sd = SuperDog()
sd.eat()
sd.drink()
print('*' * 50)

"""多层继承"""


# 定义一个爷爷类， Animal
class Animal(object):
    def eat(self):
        print('吃东西')


# 定义一个父亲类
class Dog(Animal):
    def drink(self):
        print('喝东西')


# 定义一个儿子类
class SuperDog(Dog):
    pass


# 创建对象
sd = SuperDog()
sd.eat()
sd.drink()

"""
子类重写父类同名方法
父类的方法不能满足子类的需要，可以对父类的方法重写，重写父类方法的目的是为了给他扩展功能
在子类中定义了一个和父类同名的方法(参数也一样)，即为对父类的方法重写
子类调用同名方法，默认只会调用子类的

方法重写后, 左侧会有重写的提示. 对代码没有任何影响, 仅仅是个提示
"""


class Father(object):
    def __init__(self):
        self.money = 999999999

    def play(self):
        print("打麻将")


class Son(Father):
    def play(self):
        """
        父类的方法不能满足子类的需要，可以对父类的方法重写，
        子类调用同名方法，默认只会调用子类的
        """
        print('打王者')


son = Son()
son.play()

"""
继承的三种情况
1. 完全继承 --> 继承
2. 全部不要 --> 重写
3. 不完全满足 --> 先调用父类, 再进行扩展

子类调用父类同名方法：
父类名.同名方法(self, 形参1, ……)
super(子类名, self).同名方法(形参1, ……)
super().同名方法(形参1, ……)：是方法 2 的简写，推荐的写法
"""


class Father(object):
    def __init__(self):
        self.money = 99999999

    def play(self):
        print("打麻将")
        print('抽烟')
        print('喝酒')
        print('烫头')


class Son(Father):
    def play(self):
        """子类调用父类同名方法"""
        print('唱KTV')

        # 1. 父类名.同名方法(self, 形参1, ……)
        # Father.play(self)

        # 2. super(子类名, self).同名方法(形参1, ……)  看似复杂, 实际上借助智能提示即可
        # super(Son, self).play()

        # 3. super().同名方法(形参1, ……)：是方法 2 的简写，推荐的写法"""
        super().play()

        print('打王者')


son = Son()
son.play()

"""
1. 重写__init__时, 一定要调用父类的__init__, 否则父类中定义的属性值会丢失
2. __init__可以传参, 父类的__init__要传参, 那么子类的__init__也需要传参
"""


class Father(object):
    def __init__(self, money, house, car):
        self.money = money
        self.house = house
        self.car = car

    def play(self):
        print("打麻将")
        print('抽烟')
        print('喝酒')
        print('烫头')


"""
1. 子类要想扩展属性, 可以重写init, 同时一定要注意需要先调用父类的init, 避免属性丢失. 
如果先扩展属性后调用父类的init, 可能会因为同名导致子类的属性添加不成功
"""

"""
2. __init__可以传参, 父类的__init__要传参, 那么子类的__init__也需要传参.
然后可以根据情况, 再针对子类进行属性的扩展
"""


class Son(Father):
    def __init__(self, money, house, car, dog):
        super().__init__(money, house, car)
        self.dog = dog

    def play(self):
        print('唱KTV')
        super().play()
        print('打王者')


son = Son(10, '公寓', '自行车', '小白')
print(son.money, son.house, son.car, son.dog)


# 定义2个类，它们没有继承关系，是平级的

class SmallDog(object):
    def eat(self, name):
        print(name + '吃小东西')

    def drink(self, name):
        print(name + '喝小口水')


# 再定义一个类
class BigDog(object):
    def eat(self, name):
        print(name + '啃大骨头')

    def drink(self, name):
        print(name + '喝大口水')


"""多继承中解决调用问题: 1. 先重写同名方法 2. 指定父类的实现方式"""


# 定义一个子类，多继承于上面2个父类
class SuperDog(BigDog, SmallDog):
    def eat(self, name):
        """
        在重写的父类方法中, 指定父类的调用方法
        """
        """1.父类名.同名方法(self, 形参1, ……)：调用指定的父类 推荐记忆"""
        # 默认找Big, 手动指定Small
        SmallDog.eat(self, name)

        """2. super(子类名, self).同名方法(形参1, ……)：调用继承顺序中类名的下一个类的同名方法"""
        # super(BigDog, self).eat(name)

        """3. super().同名方法(形参1, ……)：调用先继承父类的同名方法"""
        # super().eat(name)  # 这种方式没有办法实现指定父类, 只能根据继承类找上一个父类.


# 定义子类对象，调用方法
sd = SuperDog()
sd.eat("超级狗")  # 默认先调用先继承的父类，即 SmallDog
sd.drink("超级狗")

# 查看继承链--> 了解
# 类名.__mro__: 可以查看继承链关系
print(SuperDog.__mro__)

# ----------------多态------------------
"""
1. 多态：多种形态，调用同一个函数，不同表现. 多态的好处是方便扩展程序的功能, 而对原有逻辑代码不更改

2. 常规的实现多态的步骤:
  1. 实现继承关系  --> 为了有同名方法
  2. 子类重写父类方法  --> 不同的类有不同的实现
  3. 通过对象调用该方法  --> 调用同名方法

在Python中多态的体现并不明显. 不需要有继承关系, 只需要有同名方法, 既可以实现多态
Python是动态语言, 不会去做过多的类型检测. 只是在运行时, 强制调用方法, 如果能调用成功, 就可以执行该方法
"""


# 定义一个父类， Animal
class Animal(object):
    def eat(self):
        print('吃东西')


# 定义一个子类Dog，继承于Animal
class Dog(object):
    def eat(self):
        """重写父类方法"""
        print('啃骨头')


# 定义一个子类Cat，继承于Animal
class Cat(object):
    def eat(self):
        """重写父类方法"""
        print('吃小鱼')


# 定义一个子类Mouse, 继承与Animal
class Mouse(object):
    def eat(self):
        print('吃大米')


"""多态的好处: 是方便扩展程序的功能
    调用接口是完全不需要变化的
    程序开发尽可能不要因为扩展功能, 而对原有代码做出影响
"""


# if temp = '猫类':
#     调用猫的方法
# elif temp = '狗类':
#     调用狗的方法
# elif temp = '鼠类'
#     调用鼠的方法

# 定义一个函数，用于测试多态
def func(temp):
    temp.eat()


# 创建子类对象
d = Dog()
c = Cat()
m = Mouse()

# 调用同一个函数，不同表现
# 传递d参数，调用Dog的eat()
# 传递c参数，调用Cat的eat()
func(d)  # 啃骨头
func(c)  # 吃小鱼
func(m)  # 吃大米

"""
1. 多态：多种形态，调用同一个函数，不同表现

2. 实现多态的步骤:
  1. 实现继承关系  --> 为了有同名方法
  2. 子类重写父类方法  --> 不同的类有不同的实现
  3. 通过对象调用该方法  --> 调用同名方法

Python中的多态, 不需要有继承关系, 只需要有同名方法, 就可以实现多态
Python是动态语言, 不会去做过多的类型检测. 只
是在运行时, 强制调用方法, 如果能调用成功, 就可以执行该方法
"""

"""
多态的好处是方便程序功能的扩展

微信支付\支付宝支付, 后续会增加百度支付 --> 为了方便扩展可以使用多态的特性, 让它们拥有同名方法
"""


class WXPay(object):
    def pay(self):
        print('微信支付')


class AliPay(object):
    def pay(self):
        print('支付宝支付')


class BDPay(object):
    def pay(self):
        print('百度支付')


# 支付的公共接口
def func_pay(obj):
    """只要传入的对象, 能够实现pay方法, 那么这个函数就不用发生任何变化"""
    obj.pay()


wx_pay = WXPay()
ali_pay = AliPay()
bd_pay = BDPay()

func_pay(wx_pay)
func_pay(ali_pay)
func_pay(bd_pay)

"""
通过类创建的对象 又称为 实例对象，对象属性 又称为 实例属性
类本身也是一个对象，执行class语句时会被创建，称为 类对象，为了和实例对象区分开来，我们习惯叫类

实例属性
通过在__init__方法里面给实例对象添加的属性
在类的外面，直接通过实例对象添加的属性
实例属性必须通过实例对象才能访问

类属性
类属性就是 类对象 所拥有的属性，它被 该类的所有实例对象 所共有。
定义在类里面，类方法外面的变量就是类属性
类属性可以使用 类名 或 实例对象 访问，推荐使用类名访问
"""


class Dog(object):
    # 定义类属性
    color = '黄'

    # 定义实例属性
    def __init__(self, name=''):
        self.name = name


dog = Dog('旺财')
"""获取实例属性, 需要通过实例对象获取"""
print(dog.name)

"""获取类属性, 可以通过类对象或实例对象获取"""
print(Dog.color)  # 类对象.类属性
print(dog.color)  # 实例对象.类属性

"""
结论: 类属性的获取有2种方式, 类属性的修改只有1种方式

类属性只能通过类对象修改，不能通过实例对象修改
"""

"""类属性修改，只能通过类名修改，不能通过对象名修改"""


class Dog(object):
    # 类属性
    count = 0


# 通过类名修改
Dog.count = 1
print(Dog.count)

print('=' * 30)
# 对象名.变量 = 数据 默认操作给实例对象添加实例属性，已经不能操作类属性
# 如果类属性名字和实例属性名字相同，实例对象名只能操作实例属性
d1 = Dog()
d1.count = 250  # 这句代码实际上是在d1的内存地址上, 产生了一个同名的count变量. 存在了d1的内存地址里, 和类的属性没有任何关系

print(Dog.count, d1.count)

"""
私有类属性
类属性也可以设置为 私有，前边添加两个下划线__

如何修改私有属性呢?
"""


class Dog(object):
    # 类属性
    __count = 0


print(Dog.__count)  # 类的外面，不能直接访问私有类属性，err

"""
如何获取类属性: 类名.类属性 or 实例对象.类属性 ?
如何更改类属性: 类名.类属性修改 ?
"""

# ----------------类方法和静态方法------------------

"""
实例方法、类方法和静态方法
学习目标：能够区分实例方法、类方法和静态方法
"""

"""
实例方法：属于实例对象的方法，第一个形参是self，只能通过实例对象进行调用，self形参就是实例对象
"""


class Dog(object):
    """狗类"""

    def __init__(self, _name, _age):
        self.name = _name
        self.age = _age

    # 实例方法：只能通过实例对象进行调用
    def show_info(self):
        print(f'我的名字：{self.name}, 年龄：{self.age}')


print('======================= 示例1 =======================')
# 创建一个 Dog 对象
dog1 = Dog('小黄', 1)
dog1.show_info()

"""
类方法：属于类对象(类)的方法，可以通过类名或实例对象名进行调用

作用：用于对一类事物进行操作，和具体的某个实例对象没有直接关联关系，若类中的方法方法在逻辑上采用
类本身来调用更合理，那么这个方法就可以定义为类方法

需求：在类中提供一个方法，展示一共有多少只狗

定义：
    class 类名(object):
        @classmethod
        def 类方法名(cls):
            pass

注意：类方法必须有一个形参，一般叫 cls，调用类方法是 cls 形参不用传递，python解释器会自动传递
"""


class Dog(object):
    # 类属性
    count = 0

    def __init__(self, _name, _age):
        # 实例属性
        self.name = _name
        self.age = _age

        # 只要__init__调用，就说明创建了一个对象，类属性 count 就加1
        Dog.count += 1

    # 实例方法：只能通过实例对象进行调用
    def show_info(self):
        print(f'我的名字：{self.name}, 年龄：{self.age}')

    # 需求：提供一个显示一共有多少只狗的方法
    @classmethod
    def show_dog_count(cls):
        # print('测试 cls：', id(cls))
        print(f'现在一共有{cls.count}只狗')


print('======================= 示例2 =======================')

print(id(Dog))

# 调用类方法：推荐【类名.类方法名()】 进行调用
Dog.show_dog_count()

# 结论：调用类方法时，第一个参数 cls 不需要传递，cls 就是调用这个的方法类(类名)

dog1 = Dog('小黄', 1)
dog2 = Dog('大黄', 2)
dog3 = Dog('小白', 3)
Dog.show_dog_count()

"""
静态方法：主要是用来存放逻辑性的代码，逻辑上属于类，但是和类本身没有关系，也就是说在静态方法中，
不会涉及到类中的属性和方法的操作。可以理解为，静态方法是个独立的、单纯的函数，它仅仅托管于某个
类中，便于使用和维护。

定义：
    class 类名(object):
        @staticmethod
        def 静态方法名():
            pass
            
注意：静态方法不需要有 self 或 cls 参数
"""


class SysManager(object):
    """管理系统类"""

    # 需求：提供一个显示菜单的方法
    @staticmethod
    def show_menu():
        """显示菜单"""
        print('=' * 20)
        print('1. 新增一个学生')
        print('2. 查询所有学生')
        print('3. 查询指定学生')
        print('4. ...')
        print('=' * 20)


print('======================= 示例3 =======================')

# 静态方法的调用：推荐【类名.静态方法名()】进行调用
SysManager.show_menu()

# ----------------------异常-------------------------


# -------------------捕获异常信息---------------------
"""
语法格式：

try:
    可能发生异常的代码
except:
      # 处理异常的代码
    1. 如果try里面发生异常
    2. 自动跳转到except里面

把可能出现问题的代码，放在try中
把处理异常的代码，放在except中
except后面没有指定异常类型，可以捕获任意类型的异常
"""

"""1 try...except..."""
# try:
#     open("xxx.txt", "r")
# except:
#     print("捕获到了异常, 文件不存在, 请检查文件名")


"""2. 捕获指定异常"""
# try:
#     # open("xxx.txt", "r")
#     10 / 0
# except FileNotFoundError:
#     print("捕获到了异常, 文件不存在, 请检查文件名")


"""3 except捕获指定多个异常"""
# try:
#     open("xxx.txt", "w")
#     10 / 0
# except (FileNotFoundError,ZeroDivisionError):
#     print("捕获到了异常, 文件不存在, 或者除数为0")

"""4 except捕获异常信息"""
try:
    open("zzz.txt", "r")
    10 / 0
except (FileNotFoundError, ZeroDivisionError) as error:
    # 捕获到异常信息后, 一方面可以给用户进行相关的提示
    # 另一方面应该写入程序日志中 log.txt, 便于程序员后续查看并挑错
    print(error)

# ----------------except捕获所有异常及信息-------------------
"""
下面多种写法, 重点记忆第5个即可.
语法格式：

try:
    可能发生异常的代码
except Exception as error:
    # 处理异常的代码
    1. 如果try里面发生异常
    2. 自动跳转到except里面
    3. 通过error对象获取错误原因

把可能出现问题的代码，放在try中
把处理异常的代码，放在except中
Exception可以捕获任意类型的异常
"""

"""1 try...except..."""
# try:
#     open("xxx.txt", "r")
# except:
#     print("捕获到了异常, 文件不存在, 请检查文件名")


"""2. 捕获指定异常"""
# try:
#     # open("xxx.txt", "r")
#     10 / 0
# except FileNotFoundError:
#     print("捕获到了异常, 文件不存在, 请检查文件名")


"""3 except捕获指定多个异常"""
# try:
#     open("xxx.txt", "w")
#     10 / 0
# except (FileNotFoundError,ZeroDivisionError):
#     print("捕获到了异常, 文件不存在, 或者除数为0")

"""4 except捕获异常信息"""
# try:
#     open("zzz.txt", "r")
#     10 / 0
# except (FileNotFoundError,ZeroDivisionError) as error:
#     # 捕获到异常信息后, 一方面可以给用户进行相关的提示
#     # 另一方面应该写入程序日志中 log.txt, 便于程序员后续查看并挑错
#     print(error)

"""5 except捕获所有异常及信息"""
try:
    # open("zzz.txt", "r")
    10 / 0
except Exception as error:
    # error 就是错误的对象, 内部重写了str方法, 所以直接打印对象可以显示错误的描述信息
    # 捕获到异常信息后, 一方面可以给用户进行相关的提示
    # 另一方面应该写入程序日志中 log.txt, 便于程序员后续查看并挑错
    print(error, type(error))

"""
语法格式：

try:
    可能发生异常的代码
except:
    处理异常的代码
else:
    没有发生异常，except不满足执行else
finally:
    不管有没有异常，最终都要执行
"""

f = open('yyy.txt', 'w')

try:
    # content = f.read()
    f.write('python')
except Exception as error:
    print(error)
else:
    print('没有异常')
finally:
    print('无论有没有异常, 都要关闭文件')
    f.close()

# -----------------------异常捕获的传递-----------------------

"""
异常传递特点
如果异常在内部产生，如果内部不捕获处理，这个异常会向外部传递

try嵌套时，如果内层try没有捕获处理该异常，就会向外层try进行传递
函数嵌套时，如果内层函数没有捕获处理该异常，就会向外层函数进行传递

根据异常传递的特点, 我们不一定非要在立即出错的地方加捕获, 只要在合适的位置增加捕获, 就可以避免程序崩溃
"""

"""异常嵌套"""
try:
    f = open('yyy.txt', 'w')

    # 内部语句执行完，才向外部传递异常
    try:
        # 前面只写方式打开文件，不能读文件，产生异常
        # 内部没有捕获处理异常
        ret = f.read()
        print(ret)
    finally:
        print('关闭文件')
        f.close()

except Exception as e:
    print('外层捕获异常：', e)

"""函数嵌套"""


# 定义1个函数，函数内部发生了异常 test01()，没有捕获处理
def test01():
    print('开始执行test0111111')
    print(num)
    print('结束执行test0111111')


# 定义另外一个函数 test02, 在函数内部调用test01
def test02():
    print('开始执行test02222222')
    test01()
    print('结束执行test02222222')


# 定义一个test03函数，函数内部调用test01，但是对test01做异常处理
def test03():
    print('开始执行test0333333')

    try:
        test01()
    except Exception as e:
        print('外层函数捕获异常：', e)

    print('结束执行test0333333')


# 调用test02()
# test02()
test03()

# -------------------自定义异常实现------------------

"""
语法格式：

# 1. 自定义异常类
class 自定义异常类名字(Exception):
    1.1 重新写__init__(self, 形参1， 形参2，……)
        # 建议调用父类的init，先做父类的初始化工作
        super().__init__()
        咱们自己写的代码

    1.2 重新写__str__()，返回提示信息

# 2. 抛出异常类
raise 自定义异常类名字(实参1， 实参2，……)
"""

"""
回顾一下系统是如何抛异常的:

open("xxx.txt", "r")
FileNotFoundError: [Errno 2] No such file or directory: 'xxx.txt'

1. 异常是可以传参的 --> xxx.txt --> 异常类实现了__init__(name)
2. 打印异常对象时, 实现了格式化字符串 --> 异常类重写了__str__
3. 系统抛出了异常 --> 我们如何抛出异常 --> raise 可以让程序崩溃
"""

"""
需求：
1. 自定义异常类，电话号码长度异常类
    1.1 __init__，添加2个属性，用户电话的长度，要求的长度
    1.2 __str__ 返回提示描述意思，如：用户电话长度为：xx位, 这边要求长度为：11位

2. 只要用户输入的手机号码不为11位，抛出自定义异常类
"""


# 1. 自定义异常类
class NumberError(Exception):
    def __init__(self, user_len, match_len=11):
        super().__init__()  # 注意, 为了避免丢掉父类的初始化代码, 一定要先调用父类
        self.user_len = user_len
        self.match_len = match_len

    def __str__(self):
        return f'用户电话长度为：{self.user_len} 位, 这边要求的长度为：{self.match_len} 位'


# 2. 只要用户输入的手机号码不为11位，抛出自定义异常类
raise NumberError(5)  # 抛出自定义异常类

# try:
#     num_str = input('请输入你的号码：')
#     if len(num_str) != 11:
#         raise NumberError(len(num_str))  # 抛出自定义异常类
# except NumberError as e:  # e 为 NumberError(len(num_str))实例对象 的别名
#     print('异常信息为：', e)


# TODO--------------------schedule模块用法-----------------------------
import os
import time
import schedule

os.system('calc.exe')
os.system('notepad.exe')
os.startfile('C:\\Program Files (x86)\\Tencent\\WeChat\\WeChat.exe')


def dance():
    for i in range(5):
        print("跳舞中...")
        time.sleep(1)


def sing():
    for i in range(5):
        print("唱歌中...")
        time.sleep(5)


schedule.every(10).seconds.do(sing)
while True:
    schedule.run_pending()
