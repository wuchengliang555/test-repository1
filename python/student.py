# --------------函数版学生管理系统--------------

"""显示菜单"""


def show_menu():
    """显示菜单功能"""
    print('=' * 20)
    print('=1,添加学生')
    print('=2,查询所有学生')
    print('=3,查询某个学生')
    print('=4,修改某个学生')
    print('=5,删除某个学生')
    print('=6,退出系统')
    print('=' * 20)


# 用户信息列表
user_dict_list = [{'name': 'mike', 'age': '18', 'tel': '123'},
                  {'name': 'lili', 'age': '25', 'tel': '187'}]

'''添加学生'''


def add_student():
    user_name = input("请输入你的名字:")
    user_age = input("请输入你的年龄:")
    user_tel = input("请输入你的电话")

    for user_dict in user_dict_list:
        if user_dict['name'] == user_name:
            print("该名字已经被注册!,请重新输入")
            start()
    else:
        user_dict = {'name': user_name, 'age': user_age, 'tel': user_tel}
        user_dict_list.append(user_dict)
        print(user_dict_list)


'''显示所有学生'''


def show_student():
    """显示所有学生"""
    # \n:换行   \t:制表符
    print('序号\t\t姓名\t\t年龄\t\t电话')
    for i, user_dict in enumerate(user_dict_list):
        print(i, user_dict['name'], user_dict['age'], user_dict['tel'], sep='\t\t')


'''显示指定学生'''


def show_one_student():
    user_name = input("请输入学生姓名:")

    for user_dict in user_dict_list:
        if user_dict['name'] == user_name:
            print('查找的用户信息如下:')
            print(f'姓名:{user_name}\n年龄:{user_dict["age"]}\n电话:{user_dict["tel"]}')
            break
    else:
        print("查找的学生不存在!")


'''修改某个学生'''


def update_student():
    user_name = input("请输入要修改的学生姓名:")
    for user_dict in user_dict_list:
        if user_name == user_dict['name']:
            update_name = input("请输入新的姓名:")
            update_age = input("请输入新的年龄:")
            update_tel = input("请输入新的电话:")

            user_dict['name'] = update_name
            user_dict['age'] = update_age
            user_dict['tel'] = update_tel
            break
    else:
        print("该学生信息不存在!")


'''删除学生'''


def delete_name():
    user_name = input("请输入要删除的学生姓名:")
    for user_dict in user_dict_list:
        if user_dict['name'] == user_name:
            user_dict_list.remove(user_dict)
            print("删除学生信息成功")
            break
    else:
        print("查找的学生不存在!")


'''入门函数'''


def start():
    while True:

        show_menu()

        cmd_num = int(input("请输入功能数字:"))

        if cmd_num == 1:
            print('添加学生')
            add_student()
        elif cmd_num == 2:
            print('查询所有学生')
            show_student()
        elif cmd_num == 3:
            print('查询某个学生')
            show_one_student()
        elif cmd_num == 4:
            print('修改某个学生')
            update_student()
        elif cmd_num == 5:
            print('删除某个学生')
            delete_name()
        elif cmd_num == 6:
            print('6')
            break
        else:
            print("输入有误,请重新输入")


if __name__ == '__main__':
    start()

# ------------------文件版学生管理系统----------------


"""
1. 在退出程序时, 保存文件 str(list)
2. 程序加载时, 读取文件  eval(str)
"""
import os

# 用户信息列表
user_dict_list = []

"""删除学生"""


def delete_student():
    """删除学生"""
    # 1. 输入要删除的姓名
    user_name = input('请输入要删除的姓名: ')

    # 2. 循环遍历查找
    for user_dict in user_dict_list:
        if user_dict['name'] == user_name:
            # 4. 找到了就直接删除字典信息
            user_dict_list.remove(user_dict)
            print('删除学生信息成功')
            break

    # 3. 查询不到就提示找不到
    else:
        print('该学生信息不存在')


"""修改学生"""


def update_student():
    """修改学生"""
    # 1. 输入要修改的姓名
    user_name = input('请输入要修改的姓名: ')

    # 2. 循环遍历查找
    for user_dict in user_dict_list:
        if user_dict['name'] == user_name:
            # 4. 找到了就提示重新输出3个信息, 并更新字典
            update_name = input('请输入新的姓名: ')
            update_age = input('请输入新的年龄: ')
            update_tel = input('请输入新的电话: ')  # 理论上这里还需要对电话在做判断

            # 更新字典
            user_dict['name'] = update_name
            user_dict['age'] = update_age
            user_dict['tel'] = update_tel
            print('修改学生信息成功')

            break

    # 3. 没有找到就提示未找到
    else:
        print('该学生信息不存在')


"""显示指定学生"""


def show_one_student():
    """显示指定学生"""
    user_name = input('请输入学生姓名: ')

    for user_dict in user_dict_list:
        if user_dict['name'] == user_name:
            print('询到的用户信息如下：')
            print(f'姓名: {user_name}\n年龄: {user_dict["age"]}\n电话: {user_dict["tel"]}')
            break
    else:
        print('查询的学生不存在')


"""显示所有学生"""


def show_all_student():
    """显示所有学生"""
    # \n: 换行 \t: 制表符 4个空格
    print('序号\t\t姓名\t\t年龄\t\t电话')
    for i, user_dict in enumerate(user_dict_list):
        print(i, user_dict['name'], user_dict['age'], user_dict['tel'], sep='\t\t')


"""添加学生"""


def add_student():
    """添加学生"""
    # 1. 提示输入电话\姓名\年龄
    user_tel = input('请输入电话: ')

    # 2. 针对电话进行循环遍历, 看是否有重复的电话
    for user_dict in user_dict_list:
        if user_dict['tel'] == user_tel:
            # 3. 有重复的提示已注册
            print('该手机号已经注册')
            break

    # 4. 没有重复的就将信息添加到数据中
    else:
        user_name = input('请输入姓名: ')
        user_age = input('请输入年龄: ')
        user_dict = {'tel': user_tel, 'name': user_name, 'age': user_age}
        user_dict_list.append(user_dict)
        print(user_dict_list)


"""显示菜单"""


def show_menu():
    """显示菜单功能"""
    print('=' * 20)
    print('= 1. 添加学生')
    print('= 2. 查询所有学生')
    print('= 3. 查询某个学生')
    print('= 4. 修改某个学生')
    print('= 5. 删除某个学生')
    print('= 6. 退出系统')
    print('=' * 20)


"""保存文件"""


def save_data():
    """保存文件"""
    with open('student.db', 'w') as f:
        f.write(str(user_dict_list))


"""读取文件"""


def load_data():
    # 判断文件是否存在. 文件存在就读取
    if os.path.exists('student.db'):
        # 读取数据
        with open('student.db') as f:
            content = eval(f.read())  # 读取并转换成列表

            # 结论: 无论是可变还是不可变类型. 只要重新赋值了, 就需要使用global

            # 方式一: 使用extend, 不用加global
            user_dict_list.extend(content)

            # 方式二: 使用重新赋值, 配合global
            # global user_dict_list
            # user_dict_list = content  # 对可变类型重新赋值, 会导致内存发生变化
            print(user_dict_list, type(user_dict_list))


"""入口函数"""


def start():
    load_data()  # 数据加载只需要1次. 所以不能放到循环里面

    """程序的入口函数"""
    while True:

        # load_data()  # 千万不能重复加载数据

        show_menu()

        cmd_num = int(input("请输入功能数字："))

        if cmd_num == 1:
            add_student()  # 添加学生
        elif cmd_num == 2:
            show_all_student()  # 显示所有学生
        elif cmd_num == 3:
            show_one_student()  # 显示指定学生
        elif cmd_num == 4:
            update_student()  # 修改学生
        elif cmd_num == 5:
            delete_student()  # 删除学生
        elif cmd_num == 6:
            save_data()  # 退出前保存
            print('退出系统')
            break
        else:
            print('输入有误, 请重新输入')


# main有智能提示, 然后回车即可
if __name__ == '__main__':
    start()  # 在这个if判断里面写程序启动的代码

# ------------------面向对象版学生管理系统----------------


"""
面向对象分类思想--> 需要将字典-->对象
学生类:
    属性: 存储属性 姓名 年龄 电话 --> 替换的是原先的列表中的字典
    方法: __init__\__str__\__to_dict__
系统类:
    属性: 学生列表\文件路径
    方法: __init__\启动系统\添加学生\修改学生\删除学生\查询学生\文件保存\文件读取
"""
import os

"""学生类"""


class Student(object):
    def __init__(self, name='', age=0, tel=''):
        self.name = name
        self.age = age
        self.tel = tel

    def __str__(self):
        return f"姓名是:{self.name}, 年龄是:{self.age}, 电话是:{self.tel}"

    def to_dict(self):
        """对象转字典的方法"""
        return {'name': self.name, 'age': self.age, 'tel': self.tel}


"""系统类"""


class System(object):
    def __init__(self, file_name='student.db'):
        self.user_obj_list = []
        self.file_name = file_name

    def start(self):
        """启动程序"""
        # 0. 程序启动时加载一次
        self.load_data()

        while True:

            # 1. 显示菜单
            self.show_menu()

            # 2. 用户选择
            if self.do_select():
                # 3. 如果用户选择了退出6, 就会终止
                break

    # 用不到self或者cls时, 就修改成静态方法
    @staticmethod
    def show_menu():
        """显示菜单"""
        print('=' * 20)
        print('= 1. 添加学生')
        print('= 2. 查询所有学生')
        print('= 3. 查询某个学生')
        print('= 4. 修改某个学生')
        print('= 5. 删除某个学生')
        print('= 6. 退出系统')
        print('=' * 20)

    def do_select(self):
        """用户选择功能"""
        try:
            cmd_num = int(input('请输入命令:'))
        except Exception as error:
            print('输入有误, 请输入1~6', error)
        else:
            if cmd_num == 1:
                self.add_stu()
            elif cmd_num == 2:
                self.search_all_stu()
            elif cmd_num == 3:
                self.search_one_stu()
            elif cmd_num == 4:
                self.update_stu()
            elif cmd_num == 5:
                self.delete_stu()
            elif cmd_num == 6:
                self.save_data()
                return True  # 只有选择了6才会返回True
            else:
                print("输入有误, 请重新输入")

    def load_data(self):
        """加载数据"""
        if os.path.exists(self.file_name):
            with open(self.file_name) as file:
                user_dict_list = eval(file.read())

                # 使用列表推导式, 直接生成转换成对象的列表
                self.user_obj_list = [Student(user_dict['name'], user_dict['age'], user_dict['tel']) for user_dict in
                                      user_dict_list]

    def save_data(self):
        """保存数据"""
        with open(self.file_name, 'w') as file:
            """因为文件需要字符串格式的字典信息, 所以需要循环遍历, 将每一个对象都转换为字典"""
            # temp_list = []
            # for user_obj in self.user_obj_list:
            #     temp_list.append(user_obj.to_dict())
            temp_list = [user_obj.to_dict() for user_obj in self.user_obj_list]
            file.write(str(temp_list))

    def delete_stu(self):
        """删除学生"""
        user_name = input("请输入要删除的姓名:")
        for user_obj in self.user_obj_list:
            if user_obj.name == user_name:
                self.user_obj_list.remove(user_obj)
                break
        else:
            print('该学生未找到')

    def update_stu(self):
        """修改学生"""
        user_name = input("请输入要修改的姓名:")
        for user_obj in self.user_obj_list:
            if user_obj.name == user_name:
                # 暂时不处理年龄和电话的问题
                user_obj.name = input('请输入新的姓名:')
                user_obj.age = int(input('请输入新的年龄:'))
                user_obj.tel = input('请输入新的电话:')
                break
        else:
            print('该学生未找到')

    def search_one_stu(self):
        """查询某个学生"""
        user_name = input('请输入要查询的姓名:')
        for user_obj in self.user_obj_list:
            if user_obj.name == user_name:
                print(user_obj)  # 打印对象, 会调用该对象的__str__
                break
        else:
            print('该学生未找到')

    def search_all_stu(self):
        """查询所有学生"""
        print('序号\t\t姓名\t\t年龄\t\t电话')
        for i, user_obj in enumerate(self.user_obj_list):
            print(f'{i + 1}\t\t{user_obj.name}\t\t{user_obj.age}\t\t{user_obj.tel}')

    def add_stu(self):
        """添加学生"""
        # 1. 输入手机号 --> 遍历查询是否有注册
        user_tel = input('请输入电话:')
        for user_obj in self.user_obj_list:
            if user_obj.tel == user_tel:
                print('该用户已注册')
                break
        else:
            # 2. 输入年龄 --> 转换整型, 输入错误重新输入
            while True:
                try:
                    user_age = int(input('请输入年龄:'))
                except Exception as error:
                    # error将来可以写入日志里, 给程序员看
                    print('年龄输入有误, 请输入数字')
                else:
                    break

            # 3. 输入姓名
            user_name = input('请输入姓名:')

            # 4. 将信息转换为对象, 添加到列表中
            user_obj = Student(user_name, user_age, user_tel)
            self.user_obj_list.append(user_obj)
            print(self.user_obj_list)


"""测试代码"""
if __name__ == '__main__':
    sys = System()
    sys.start()


















# -------------自己瞎鸡儿敲的------------------
import os

user_dict_list = []


def main():
    load_student()

    while True:
        """显示菜单功能"""
        menu()

        cmd_num = input('请输入功能数字:')

        if cmd_num == '1':
            add_student()
        elif cmd_num == '2':
            show_all_studnet()
        elif cmd_num == '3':
            show_one_student()
        elif cmd_num == '4':
            update_student()
        elif cmd_num == '5':
            del_one_studnet()
        elif cmd_num == '6':
            print('感谢您的使用,再见!')
            save_student()
            break
        else:
            print('您的输入有误,请重新输入!')


def menu():
    print('========学生信息管理系统======')
    print('----------功能菜单----------')
    print('=1,添加学生')
    print('=2,查询所有学生')
    print('=3,查询某个学生')
    print('=4,修改某个学生')
    print('=5,删除某个学生')
    print('=6,退出系统')
    print('=' * 20)


def add_student():
    username = input('请输入您要添加的学生姓名:')
    for user_dict in user_dict_list:
        if username == user_dict['name']:
            print('该学生已被注册!')
            answer = input('是否需要继续添加学生? y/n')
            if answer == 'y' or answer == 'Y':
                add_student()
            else:
                print('拜拜!')
                break
    else:
        user_age = input('请输入学生的年龄:')
        user_tel = input('请输入学生的电话:')
        student_dict = {'name': username, 'age': user_age, 'tel': user_tel}
        user_dict_list.append(student_dict)


def show_all_studnet():
    print('序号\t\t姓名\t\t年龄\t\t电话')
    for i, user_dict in enumerate(user_dict_list):
        print(f'{i}\t\t{user_dict["name"]}\t\t{user_dict["age"]}\t\t{user_dict["tel"]}')


def show_one_student():
    username = input('请输入您要查询的学生姓名:')
    for i, user_dict in enumerate(user_dict_list):
        if username != user_dict['name']:
            print('查找的用户信息如下:')
            print(f'姓名:{username}\n年龄:{user_dict["age"]}\n电话:{user_dict["tel"]}')
            break
    else:
        print('您输入的学生不存在!')
        answer = input('是否需要继续查询学生? y/n')
        if answer == 'y' or answer == 'Y':
            show_one_student()
        else:
            print('拜拜!')


def update_student():
    username = input('请输入您要修改的学生姓名:')
    for user_dict in user_dict_list:
        if username == user_dict['name']:
            new_name = input('请输入修改后的姓名:')
            new_age = input('请输入修改后的年龄:')
            new_tel = input('请输入修改后的电话:')
            user_dict['name'] = new_name
            user_dict['age'] = new_age
            user_dict['tel'] = new_tel
            break
    else:
        print('您要修改的学生不存在!')


def del_one_studnet():
    username = input('请输入您要删除的学生姓名:')
    for i, user_dict in enumerate(user_dict_list):
        if username == user_dict['name']:
            del user_dict_list[i]
            print('删除学生成功!')
            break
    else:
        print('您要删除的学生不存在!')


def save_student():
    with open('student.txt', 'w') as file:
        file.write(str(user_dict_list))


def load_student():
    if os.path.exists('student.txt'):
        with open('student.txt', 'r') as f:
            content = f.read()
            user_dict_list.extend(eval(content))

if __name__ == '__main__':
    main()
