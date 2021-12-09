# school_list = [1, "foo", 3.5, {"hello": "bye"}]
# school = (str(i) for i in school_list)
# print(school)
# school1 = ','.join(school)
# print(school1, type(school1))
# print(type(i for i in school_list))
#
# print('------------------')
#
# print(i for i in school_list)
# a = (i for i in school_list)
# a = list(a)
# print(a)
#
# for r in a:
#     print(type(r), r, end=' ', )

# sid = 1
# name = 'jack'
# age = 18
# height = 170
# print("\033[0;31m%s\033[0m" % '我的学号是：{:08d}, 姓名是：{}, 年龄是:{}, 身高是：{:.1f}'.format(sid, name, age, height))
# # print("\033[0;30m%s\033[0m" % '我的学号是：{:08d}, 姓名是：{}, 年龄是:{}, 身高是：{:.1f}'.format(id, name, age, height))
# print("\033[0;32m%s\033[0m" % '我的学号是：{:08d}, 姓名是：{}, 年龄是:{}, 身高是：{:.1f}'.format(sid, name, age, height))
# print("\033[0;33m%s\033[0m" % '我的学号是：{:08d}, 姓名是：{}, 年龄是:{}, 身高是：{:.1f}'.format(sid, name, age, height))
# print("\033[0;34m%s\033[0m" % '我的学号是：{:08d}, 姓名是：{}, 年龄是:{}, 身高是：{:.1f}'.format(sid, name, age, height))
# print("\033[0;35m%s\033[0m" % '我的学号是：{:08d}, 姓名是：{}, 年龄是:{}, 身高是：{:.1f}'.format(sid, name, age, height))
# print("\033[0;36m%s\033[0m" % '我的学号是：{:08d}, 姓名是：{}, 年龄是:{}, 身高是：{:.1f}'.format(sid, name, age, height))
# print("\033[0;37m%s\033[0m" % '我的学号是：{:08d}, 姓名是：{}, 年龄是:{}, 身高是：{:.1f}'.format(sid, name, age, height))
# print("\033[0;42m%s\033[0m" % '我的学号是：{:08d}, 姓名是：{}, 年龄是:{}, 身高是：{:.1f}'.format(sid, name, age, height))
# print("\033[0;43m%s\033[0m" % '我的学号是：{:08d}, 姓名是：{}, 年龄是:{}, 身高是：{:.1f}'.format(sid, name, age, height))
# print("\033[0;44m%s\033[0m" % '我的学号是：{:08d}, 姓名是：{}, 年龄是:{}, 身高是：{:.1f}'.format(sid, name, age, height))
# print("\033[0;45m%s\033[0m" % '我的学号是：{:08d}, 姓名是：{}, 年龄是:{}, 身高是：{:.1f}'.format(sid, name, age, height))
# print("\033[0;46m%s\033[0m" % '我的学号是：{:08d}, 姓名是：{}, 年龄是:{}, 身高是：{:.1f}'.format(sid, name, age, height))

# fp = open('D:/test.pycharm/python/test.txt', 'w', encoding="utf-8")
#
# print('奋斗成就更好的你', file=fp)
# fp.close()
#
#
# with open('D:/test.pycharm/python/test1.txt', 'w', encoding="utf-8") as f:
#     f.write('奋斗成就更好的你')

# def _list(num,command):
#     list1 = []
#     list2 = []
#     for i in range(num+1):
#         if i % 2 == 0:
#             list1.append(i)
#         else:
#             list2.append(i)
#     if command == True:
#         return list2
#     else:
#         return list1
#
#
# print(_list(10, 1))
