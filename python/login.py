user = {'java': '123', 'python': '123', 'zs': '123'}
while True:
    users = input("请输入操作:1.用户注册/2.用户登录/3.退出程序:")
    if users.isdigit():
        users = int(users)
        if users == 1:
            username = input('请输入您的用户名:')
            usernames = user.keys()
            if username == usernames:
                print('该用户名已被注册!')
            else:
                print("请输入密码：")
                password = input()
                user[username] = password
                print("恭喜你注册成功")
                print(user)
                break
        elif users == 2:
            user_name = input("请输入你的用户名:")
            if user_name not in user.keys():
                print("您不是我们的会员哦!")
            else:
                i = 3
                while i > 0:
                    passwd = input("请输入您的密码:")
                    for pw in user.values():
                        if passwd == pw:
                            print("登录成功!")
                            break
                    else:
                        if i > 1:
                            print(f'密码不正确,还有{i - 1}次机会哦')
                        else:
                            print("机会用完了哦!")
                    i -= 1
        elif users == 3:
            print("拜拜!")
            break
        else:
            print("要输入数字1,2,3哦!")
    else:
        print("要输入数字哦!")

# TODO --------------使用列表中嵌套字典-------------------


user_list = [{'name': 'zs', 'pw': '123'}, {'name': 'ls', 'pw': '123'}]

while True:
    num = input("请输入操作:1.用户注册/2.用户登录/3.退出程序")
    if num.isdigit():
        if num == '1':
            user = input("请输入您要注册的用户名:")
            for username in user_list:
                if username['name'] == user:
                    print("该用户已被注册:")
                    break
            else:
                password = input("请输入密码:")
                user_list.append({'name': user, 'pw': password})
                print("注册成功!")
                print(user_list)
        elif num == '2':
            user = input("请输入您要注册的用户名:")
            for username in user_list:
                if username['name'] == user:
                    i = 3
                    while i > 0:
                        password = input("请输入您的密码:")
                        if password == username['pw']:
                            print("登陆成功!")
                            break
                        else:
                            if i > 0:
                                print(f"您输入的密码不正确,还有{i - 1}次机会哦!")
                            else:
                                print("您的次数已用完!")
                        i -= 1
                    break
            else:
                print("该用户不存在!")
        elif num == '3':
            print("拜拜!")
            break
        else:
            print("你输入的数字有误,请输入1~3!")
    else:
        print("要输入一个数字哦!")
