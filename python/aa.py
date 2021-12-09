import os

filename = 'syudent.txt'


def main():
    while True:
        choice = int(input("请输入选择:"))
        if choice in [1, 2, 3, 4, 5, 6, 7]:
            if choice == 0:
                answer = input("您确定要退出系统吗? y/n\n")
                if answer == 'y' or answer == 'Y':
                    print("谢谢您的使用!")
                    break
                else:
                    continue
            elif choice == 1:
                insert()  # 录入学生信息
            elif choice == 2:
                search()  # 查询学生信息
            elif choice == 3:
                delete()  # 删除学生信息
            elif choice == 4:
                modify()  # 修改学生信息
            elif choice == 5:
                sort()  # 排序
            elif choice == 6:
                total()  # 统计学生总人数
            elif choice == 7:
                show()  # 显示所有学生信息


def menu():
    print('============学生信息管理系统============')
    print('---------------功能菜单---------------')
    print('\t\t\t1.录入学生信息')
    print('\t\t\t2.查找学生信息')
    print('\t\t\t3.删除学生信息')
    print('\t\t\t4.修改学生信息')
    print('\t\t\t5.排序')
    print('\t\t\t6.统计学生总人数')
    print('\t\t\t7.显示所有学生信息')
    print('\t\t\t0.退出')
    print('------------------------------------')


def insert():
    student_list = []
    while True:
        sid = input("请输入ID(如:1001):")
        if not sid:
            break
        name = input("请输入姓名:")
        if not name:
            break
        try:
            english = input("请输入英语成绩:")
            python = input("请输入python成绩:")
            java = input("请输入java成绩:")
        except:
            print("输入无效,不是整数类型,请重新输入!")
            continue

        student = {'sid': sid, 'name': name, 'english': english, 'python': python, 'java': java}
        student_list.append(student)
        answer = input("是否继续添加?y/n\n")
        if answer == 'y' or answer == 'Y':
            continue
        else:
            break
    save(student_list)
    print('\n学生信息录入完毕!!')


def save(lst):
    try:
        stu_txt = open(filename, 'a', encoding='utf-8')
    except:
        stu_txt = open(filename, 'w', encoding='utf-8')
    for item in lst:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()


def search():
    student_query = []
    while True:
        sid = ''
        name = ''
        if os.path.exists(filename):
            mode = input('按ID查找请输入1,按姓名查找请输入2:')
            if mode == '1':
                sid = input("请输入学生ID:")
            elif mode == '2':
                name = input("请输入学生姓名:")
            else:
                print("您的输入有误,请重新输入!")
                search()
            with open(filename, 'r', encoding='utf-8') as f:
                student = f.readlines()
                for item in student:
                    d = dict(eval(item))
                    if sid != '':
                        if d['id'] == sid:
                            student_query.append(d)
                    elif name != '':
                        if d['name'] == name:
                            student_query.append(d)
            show_student(student_query)
            student_query.clear()
            answer = input('是否要继续查询?y/n\n')
            if answer == 'y' or answer == 'Y':
                continue
            else:
                break
        else:
            print("暂为保存学生信息!")


def show_student(lst):
    if len(lst) == 0:
        print("没有查询到学生信息,无数据显示!!!")
        return
    format_title = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    print(format_title.format('ID', '姓名', '英语成绩', 'Python成绩', 'Java成绩', '总成绩'))
    # 定义内容的显示格式
    format_date = '{:^6}\t{:^12}\t{:^8}\t{:^10}\t{:^10}\t{:^8}'
    for item in lst:
        print(format_date.format(item.get('sid'),
                                 item.get('name'),
                                 item.get('english'),
                                 item.get('python'),
                                 item.get('java'),
                                 int(item.get('java')) + int(item.get('python')) + int(item.get('english'))
                                 ))


def delete():
    while True:
        student_id = input('请输入需要删除的学生的ID:')
        if student_id != '':
            if os.path.exists(filename):
                with open(filename, 'r', encoding='utf-8') as f:
                    student_old = f.readlines()
            else:
                student_old = []
            flag = False
            if student_old:
                with open(filename, 'w', encoding='utf-8') as file:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))
                        if d['sid'] != student_id:
                            file.write(str(d) + '\n')
                        else:
                            flag = False
                    if flag:
                        print(f'ID为{student_id}的学生信息已被删除！')
                    else:
                        print(f'没有找到ID为{student_id}的学生信息')
            else:
                print('无学生信息!')
                break
            show()
            answer = input('您是否要继续删除？y/n\n')
            if answer == 'y' or answer == 'Y':
                continue
            else:
                break


def modify():
    show()
    if os.path.exists(filename):
        with open(filename,'r',encoding='utf-8') as file:
            student_old = file.readlines()
    else:
        return
    student_id = input("请输入要修改的学生的ID:")
    with open(filename,'w',encoding='utf-8') as f:
        for item in student_old:
            d = dict(eval(item))
            if d['sid'] == student_id:
                print("找到学生信息,可以修改他的相关信息了!")
                while True:
                    try:
                        d['name'] = input('请重新输入姓名：')
                        d['english'] = input('请重新输入英语成绩：')
                        d['python'] = input('请重新输入Python成绩：')
                        d['java'] = input('请重新输入Java成绩： ')
                    except:
                        print('您的输入有误，请重新输入！！！')
                        continue
                    else:
                        break
                f.write(str(d) + '\n')
                print("修改成功!!!")
            else:
                f.write(str(d) + '\n')
    answer = input('是否继续修改其他学生信息？y/n\n')
    if answer == 'y' or answer == 'Y':
        modify()


def sort():
    show()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8')as rfile:
            student_list = rfile.readlines()
        studnet_new = []
        for item in student_list:
            d = dict(eval(item))
            studnet_new.append(d)
        else:
            return
        asc_or_desc = input('请选择(0,升序 1,降序):')
        if asc_or_desc == '0':
            asc_or_desc_bool == False
        elif asc_or_desc == '1':
            asc_or_desc_bool == True
        else:
            print('您的输入有误,请您重新输入!')
            sort()
        mode = input('请选择排序方式(1.按英语成绩排序 2.按python成绩排序 3.按Java成绩排序 0.按总成绩排序):')
        if mode == '1':
            student_new.sort(key=lambda student_new: int(student_new['english']), reverse=asc_or_desc_bool)
        elif mode == '2':
            pass
        elif mode == '3':
            pass
        elif mode == '0':
            pass
        else:
            print('您的输入有误,请重新输入!')


def total():
    pass


def show():
    pass
