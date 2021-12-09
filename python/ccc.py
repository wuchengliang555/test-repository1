# import pymysql
# import json
# import logging
# # 导入 Flask 类
# from flask import Flask
# from flask_cors import CORS
# from flask import request
#
# # 创建 Flask 类的实例对象
# app = Flask(__name__)
# # 设置后端服务器允许任何地址前端进行访问
# CORS(app, origins='*')
#
#
# @app.route('/index')
# def index():
#     conn = pymysql.connect(host='127.0.0.1', port=3306,
#                            database='booksite', user='root', password='root')
#     # conn = pymysql.connect(host='192.168.88.100', port=3306,
#     #                        database='booksite', user='root', password='123456')
#     cursor = conn.cursor()
#     sql = 'select * from bookinfo;'
#     cursor.execute(sql)
#     result = cursor.fetchall()
#     print(result)
#     cursor.close()
#     conn.close()
#
#     data_list = []
#     for data in result:
#         data_list.append({
#             'id': data[0],
#             'name': data[1],
#             'auth': data[2],
#             'img_url': data[3],
#             'rank': data[4]
#         })
#     data_str = json.dumps(data_list, ensure_ascii=False)
#     return data_str
#
#
# # 定义获取图书详情信息的处理函数
# @app.route('/detail')
# def detail():
#     """使用 pymysql 加载图书详情数据"""
#     # 1. 获取指定的图书id
#     book_id = request.args.get('id', 1)  # 获取不到 id 参数时，get函数默认返回1
#
#     # 2. 根据 id 查询数据库，获取对应图书的信息
#     # 创建数据库连接对象
#     conn = pymysql.connect(host='127.0.0.1', port=3306,
#                            database='booksite', user='root', password='root')
#
#     # 创建游标对象
#     cursor = conn.cursor()
#
#     # 准备查询的 SQL 语句
#     sql = f'select * from bookinfo where id={book_id}'
#
#     # 通过游标对象执行 SQL 语句
#     cursor.execute(sql)
#
#     # 获取执行 SQL 结果中的一条数据
#     result = cursor.fetchone()  # 注意：结果是元组
#
#     # 3. 将图书数据转换为字典的形式
#     data_dict = {
#         'id': result[0],
#         'name': result[1],
#         'auth': result[2],
#         'img_url': result[3],
#         'read': result[5],
#         'comment': result[6],
#         'score': result[8],
#         'content': result[7],
#         'synopsis': result[9]
#     }
#     print(data_dict)
#
#     # 4. 更新指定图书的阅读量
#     new_read = result[5] + 1
#     sql = f'update bookinfo set bread={new_read} where id={book_id}'
#     cursor.execute(sql)
#     conn.commit()
#
#     # 5. 关闭游标对象和数据库连接
#     cursor.close()
#     conn.close()
#
#     # TODO：进行埋点统计
#     header = request.headers
#     print(("请求头:", header))
#
#     logging.info({
#         'bookClick': {  # 事件名称
#             "identification": header['User-Agent'],  # 获取设备号
#             "ip": request.remote_addr,  # 用户ip
#             "equipment": header['User-Agent'],  # 用户系统信息
#             "entrance": header['Referer'],  # 用户跳转路径
#             "bookname": data_dict['name'],  # 书名
#             "read": data_dict['read'],  # 阅读量
#         }
#     })
#
#     # 6. 将指定图书数据转化为JSON字符串并返回
#     json_str = json.dumps(data_dict, ensure_ascii=False)
#     return json_str
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
#
#
# import requests
#
# url = 'http://manager-health-java.itheima.net/pages/main.html'
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
# }
#
# cookies = {
#     "JSESSIONID": "FECC0D572C97347D29CDCE7EFCB61123"
# }
#
# response = requests.get(url, headers=headers, cookies=cookies)
# print(response.content.decode())

# 抓取贴吧
# import faker
# import requests
# import time
# import random
# from faker import Faker
#
# fake = Faker()
# User = fake.user_agent()
#
# name = input('请输入要访问的贴吧的名字:')
# num = int(input('请输入要抓取的页数:'))
#
# base_url = 'https://tieba.baidu.com/f?&kw={}&pn={}'
# url_list = [base_url.format(name, i * 50) for i in range(num)]
#
# headers = {
#     'User-Agent': fake.user_agent()
# }
# for i, url in enumerate(url_list):
#     response = requests.get(url, headers)
#     file_name = f'{name}第{i + 1}页.html'
#     content = response.content.decode()
#     with open('E:/pa/校花贴吧/%s' % file_name, 'w', encoding='utf8') as f:
#         f.write(content)
#
#     print(f'{file_name}----> 抓取完成')
#
#     time.sleep(random.uniform(0, 2))


# 提示用户输入手机号码，然后使用正则判断用户的输入是否符合手机号的格式。

# import re
#
# num = input('请输入您的手机号:')
#
# res = re.match(r'\d{11}', num)
# if bool(res) == False:
#     print('您输入的手机号有误')


# 提示用户输入内容，然后使用正则判断用户的输入是否是全小写字母。

# import re
#
# content = input('请输入内容:')
# res = re.findall(r'^[a-z]+$', content)
# if res:
#     print('全部为小写!')
# else:
#     print('不全为小写')


# import re
#
# content = input('请输入内容:')
# index = len(content)
# print(index, type(index))
# res = re.findall(r'[a-z]{%d}' % index, content)
# print(res)



# 创建一个文件 stu.txt，内容如下：
# smart,18,13155667788
# david,20,13377881010
# lucy,21,15367892103
# 读取该文件的内容，使用正则从中提取出所有手机号码。

# import re
#
# with open('stu.txt', 'r', encoding='utf8') as f:
#     content = f.read()
#
# res = re.findall(r'\d{11}', content)
# print(res)
#
# import re
#
# # 读取文件内容1
# with open('./stu.txt', 'r', encoding='utf8') as f:
#     content = f.read()
#
#     # 使用正则匹配手机号
#     mobile_list = re.findall(r'1[3-9]\d{9}', content)
#
#     # 打印匹配的内容
#     print(mobile_list)
#


# # 有字符串内容如下，使用正则从中提取出`大数据分析`文字
# my_str = """
#     <!DOCTYPE html>
#     <html>
#     <head>
#         <title>徐清风</title>
#     <head>
#     <body>
#         <h2>
#             <em>大数据分析</em>
#         </h2>
#     </body>
#     </html>
#     """
#
# import re
#
# print(re.findall(r'<em>(.*?)</em>', my_str))
#
#
# # 将如下手机号的中间4位替换为 `****
# my_str = '13155661013'
#
# res = re.sub(r'(\d{3})\d{4}(\d{4})', r'\1****\2', my_str)
# print(res)

# import re
# import requests
# import jsonpath
#
# url = 'https://api.apishop.net/common/weather/get15DaysWeatherByArea?apiKey=tQntBLT1120d915becfd7863b84819c9e52f047cf6fe862&area=上海'
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
# }
#
# response = requests.get(url, headers=headers)
# content = response.content.decode()
# json_dict = response.json()
# res = jsonpath.jsonpath(json_dict, '$..daytime,day_weather')
# print(res)


# 1）使用 def 定义一个名叫 auto_sum 的函数，接收一个名叫 max_num 的参数
# 2）使用 range 生成 1~max_num 间的数字（记得要考虑range的右区间要加1）
# 3）使用 sum 对 range 进行求和，并将数值返回(return)

# def auto_sum(max_num):
#     sum = 0
#     for i in range(1, max_num+1):
#         sum += i
#     return sum
#
#
# print(auto_sum(5))
#
#
#
# # 定义一个函数，功能如下：
# # 1）定义一个函数 out_even，接收一个参数 max_num
# # 2）将 0 ~ max_num 内所有的偶数找出来，放到一个列表里，并返回
# # 3）例如：out_even(10)，得到[0, 2, 4, 6, 8, 10]
#
# def out_even(max_num):
#     num_list=[]
#     for i in range(max_num+1):
#         if i % 2 == 0:
#             num_list.append(i)
#     return num_list
#
# print(out_even(10))

# orders = [
#     {"buyer_name": "Pony", "product": "MacBook", "email": "pony@qq.com", "phone": 13812341234},
#     {"buyer_name": "Bill", "product": "AirPods", "email": "bill@ms.com", "phone": 13812341235},
#     {"buyer_name": "Hank", "product": "iPhone", "email": "hank@xyz.com", "phone": 13812341239},
# ]
#
#
# class Order(object):
#     def __init__(self, name, product, email, phone):
#         self.name = name
#         self.product = product
#         self.email = email
#         self.phone = phone
#
#     def deliver_mail(self):
#         print(f"to {self.email}\n"
#               f"Dear {self.name}:\n"
#               f"    Your purchased product : {self.product} is delivered!\n"
#               "     Thanks for your choosing!")
#
#     def deliver_sms(self):
#         print(f"to {self.phone}\n"
#               f"Dear {self.name}:\n"
#               f"    Your purchased product : {self.product} is delivered!\n"
#               "     Thanks for your choosing!")
#
#
# for order_dict in orders:
#     app = Order(name=order_dict['buyer_name'], product=order_dict['product'], email=order_dict['email'], phone=order_dict['phone'])
#     app.deliver_mail()
#     app.deliver_sms()

# import re
#
# key = "lalala<hTml>hello</Html>heiheihei"
# p1 = r"<[H,h][T,t][M,m][L,l]>.+?</[Hh][Tt][Mm][Ll]>"
# print(re.findall(p1, key))
#
#
# key = "mat cat hat pat"
# print(re.findall(r'[^p]at', key))

# import re
#
# s = "i love you not because\n12sd 34er 56\ndf e4 54434"
#
# print(re.findall(r'\w+', s, re.M))
import json


# from urllib import request
# from urllib import parse
#
# if __name__ == '__main__':
#
#     url = 'http://www.baidu.com/s?'
#     wd = input('请输入keywords:')
#     qs = {
#         "wd": wd
#     }
#     qs = parse.urlencode(qs)
#     fullurl = url + qs
#     print(fullurl)
#
#     rsp = request.urlopen(fullurl)
#     html = rsp.read()
#     html = html.decode()
#     print(html)



# 段子所有的div标签  //div[@class="col1 old-style-col1"]/div

# 段子作者   //div["@author clearfix"]//h2/text()

# 段子内容   //div[@class="content"]/span/text()

# 好笑数    //span[@class="stats-vote"]/i/text()

# 评论数    //a[@class="qiushi_comments"]/i/text()

# import json
# import requests
# from lxml import etree
#
# base_url = 'https://www.qiushibaike.com/text/page/{}/'
#
# url_list = [base_url.format(i) for i in range(1, 14)]
# print(url_list)
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
#                   '(KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
# }
#
# data_list = []
#
# for url in url_list:
#     response = requests.get(url, headers=headers)
#     html_str = response.content.decode()
#
#     # with open("糗事百科.html", 'w', encoding='utf8') as f:
#     #     f.write(html_str)
#
#     element = etree.HTML(html_str)
#
#     div_list = element.xpath('//div[@class="col1 old-style-col1"]/div')
#
#     for div in div_list:
#         item = {}
#
#         author = div.xpath('.//div["@author clearfix"]//h2/text()')[0].strip()
#         # content = div.xpath('.//div[@class="content"]/span/text()')[0].strip()
#         content = ''.join(div.xpath('.//div[@class="content"]/span/text()')).strip()
#
#         funny_num = div.xpath('.//span[@class="stats-vote"]/i/text()')[0].strip()
#
#         comment_num = div.xpath('.//a[@class="qiushi_comments"]/i/text()')[0].strip()
#
#         item['author'] = author
#         item['content'] = content
#         item['funny_num'] = funny_num
#         item['comment_num'] = comment_num
#         data_list.append(item)
#     print(f'{url}页 --- 解析完成 ---')
#
# with open('糗事百科.json', 'w', encoding='utf8') as f:
#     json_str = json.dumps(data_list, ensure_ascii=False, indent=2)
#     f.write(json_str)






# 段子所有的div标签  //div[@class="col1 old-style-col1"]/div

# 段子作者   //div["@author clearfix"]//h2/text()

# 段子内容   //div[@class="content"]/span/text()

# 好笑数    //span[@class="stats-vote"]/i/text()

# 评论数    //a[@class="qiushi_comments"]/i/text()

import requests
import json
from lxml import etree


base_url = 'https://www.qiushibaike.com/text/page/{}/'

url_list = [base_url.format(i) for i in range(1, 14)]

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                  '(KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
}

data_list = []

for url in url_list:
    response = requests.get(url, headers=headers)
    html_str = response.content.decode()
    element = etree.HTML(html_str)
    div_list = element.xpath('//div[@class="col1 old-style-col1"]/div')

    for div in div_list:
        data_dict = {}
        author = div.xpath('.//div["@author clearfix"]//h2/text()')[0].strip()
        content = div.xpath('.//div[@class="content"]/span/text()')[0].strip()
        funny_num = div.xpath('.//span[@class="stats-vote"]/i/text()')[0].strip()
        comment_num = div.xpath('.//a[@class="qiushi_comments"]/i/text()')[0].strip()

        data_dict['author'] = author
        data_dict['content'] = content
        data_dict['funny_num'] = funny_num
        data_dict['comment_num'] = comment_num

        data_list.append(data_dict)

    print(f'{url}页 --加载完成--')

with open('糗事百科.json', 'w', encoding='utf8')as f:
    json_str = json.dumps(data_list, ensure_ascii=False, indent=2)
    f.write(json_str)























