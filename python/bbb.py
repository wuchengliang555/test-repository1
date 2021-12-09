# 爬图片

# from bs4 import BeautifulSoup
# import requests
#
# # 用户代理，作为用户的角色访问网站
# gHeads = {
#     "User_Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
# }
# # 整个for循环用于控制图片展示页面（第几页）
# for i in range(10):
#     url = "https://wallhaven.cc/hot?page=%s" % i
#
#     print(url)
#     html = requests.get(url, headers=gHeads)  # 请求页面
#     html = html.content  # 获取源码
#     soup = BeautifulSoup(html, 'lxml')  # 对界面进行解析
#     href_all = soup.find_all('a', {"class": "preview"})  # 找到对应的a，且其class=preview
#     for href in href_all:  # 打开高清图片的新页面
#         href_url = href['href']  # 找到对应的href属性值
#         # 重复上述的源码获取和页面解析
#         html4 = requests.get(href_url, headers=gHeads).content
#         soup4 = BeautifulSoup(html4, 'lxml')
#         img4 = soup4.find('img', {"id": "wallpaper"})  # 找到img标签，且id = wallpaper
#         urlimg = img4['src']  # 获取属性值
#         # 将图片下载到本地
#         r = requests.get(urlimg,
#                          stream=True)  # r是response响应对象，stream=true是以字节流的方式读取数据，同时用于确保数据不会直接全部下载到内存中，便于下一步用r.iter_content实现边下载边存储（因为数据太大可能会超时）。
#         image_name = urlimg.split('/')[-1]  # 获取图片名
#         with open('E:/Image/%s' % image_name, 'wb') as f:  # Image文件必须存在；with as可以方便实现文件的打开和关闭，且容易处理异常
#             for chunk in r.iter_content(
#                     chunk_size=128):  # 利用for循环，将响应对象response（r）中的数据信息 通过iter_content方法 依次读取大小为128字节的数据块（先下载到内存中，满128字节后存储到硬盘中，实现边下载边存储），直至数据读完为止。
#                 f.write(chunk)
#         print('Saved %s' % image_name)
#     print("end.....................")





# 爬美女图片

import re
import requests

# url = 'https://www.tupianzj.com/meinv/20210219/224797.html'
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
#                   '(KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'
# }
#
# response = requests.get(url, headers=headers)
# html_content = response.content.decode('gbk')
#
# src_list = re.findall(r'img src="(.*?)"', html_content)
# print(src_list)
# for image_url in src_list:
#     response = requests.get(image_url, headers=headers)
#
#     image_content = response.content

#     file_name = image_url[-10:]
#     with open('E:/pa/美女图片/%s' % file_name, 'wb',) as f:
#         f.write(image_content)
#
# print('图片保存完毕')





# 爬百度贴吧保存数据
import requests
import time
import random
from lxml import etree

# class TiebaSpider(object):
#     def __init__(self, tb_name):
#         self.url = 'https://tieba.baidu.com/f?kw={}'.format(tb_name)
#
#         self.headers = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
#                           '(KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
#             'Cookie': 'BIDUPSID=1554213AAE9DF601C20F40764ACD5EFD; PSTM=1629893724; BAIDUID=1554213AAE9DF601903E257A16EEBCC9:FG=1; __yjs_duid=1_d47e2d1d29f4aae6ba6ee65aa44e623b1629900889759; bdshare_firstime=1631526753261; '
#                       'BDSFRCVID=zxAOJexroG0vLovHeqGghqJWjdUY67jTDYLtOwXPsp3LGJLVgSfIEG0Ptsh4mzFbQWcXogKK0eOTHkCF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF=tJuq_II2JCL3H48k-4QEbbQH-UnLqboD22OZ04n-ah02flRv-x7qKtukMhQZL-TbQGKq'
#                       '_bcm3UTdsq76Wh35K5tTQP6rLtbg5e54KKJxbPOsMb6uQ45G3PtRhUJiB5O-Ban7BhOIXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtpChbC_4j68Bj5QBeU5eetjK2CntsJOOaCkKfM7Oy4oWK441Dhjr2-j7566L5bnhWf38eM5Xj6J83M04X-o9-hvT-54e2p3FBUQJVn'
#                       'QVQft20b0yMaOLhf5aLGv2hn7jWhk2eq72y-RTQlRX5q79atTMfNTJ-qcH0KQpsIJM5-DWbT8IjHCHJjKJfRPt_Dvt-5rDHJTg5DTjhPrMMHrmWMT-MTryKKJKBn7DOb5lhJ5sKfIiMxOPX6Kf2HnRhlRNB-3iV-OxDUvnyxAZbnbhBxQxtNRJQbP2a4cPHxj5-p7obUPUD'
#                       'Mo9LUvW02cdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLtD_-MKImjjD3-RJH-xQ0KnLXKKOLVhoVLp7ketn4hUt25xAe-47-b4r02T6Z-bceQxI-Mnc2QhrdQf4WWb3ebTJr32Qr-J3R5qTpsIJM5bbsj-uhQx5IL-JvaKviaKJHBMb1jpODBT5h2M4qMxtOLR3pWDTm_q'
#                       '5TtUJMeCnTDMFhe6jXjG88tTLqfKresJoq2RbhKROvhjR02M_gyxoObtRxtTcrW-Qd54jnennlylJ8bhL4jGJBLU3kBTn9LMnx--t58h3_XhjJ0PKPQttjQn3e2nnLXqQtLx3job7TyU42bf47yMRm0q4Hb6b9BJcjfU5MSlcNLTjpQT8r5MDOK5OuJRQ2QJ8BtC_-hK3P; '
#                       'st_key_id=17; USER_JUMP=-1; video_bubble0=1; wise_device=0; BDSFRCVID_BFESS=zxAOJexroG0vLovHeqGghqJWjdUY67jTDYLtOwXPsp3LGJLVgSfIEG0Ptsh4mzFbQWcXogKK0eOTHkCF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS='
#                       'tJuq_II2JCL3H48k-4QEbbQH-UnLqboD22OZ04n-ah02flRv-x7qKtukMhQZL-TbQGKq_bcm3UTdsq76Wh35K5tTQP6rLtbg5e54KKJxbPOsMb6uQ45G3PtRhUJiB5O-Ban7BhOIXKohJh7FM4tW3J0ZyxomtfQxtNRJ0DnjtpChbC_4j68Bj5QBeU5eetjK2CntsJOOaCkKfM'
#                       '7Oy4oWK441Dhjr2-j7566L5bnhWf38eM5Xj6J83M04X-o9-hvT-54e2p3FBUQJVnQVQft20b0yMaOLhf5aLGv2hn7jWhk2eq72y-RTQlRX5q79atTMfNTJ-qcH0KQpsIJM5-DWbT8IjHCHJjKJfRPt_Dvt-5rDHJTg5DTjhPrMMHrmWMT-MTryKKJKBn7DOb5lhJ5sKfIiMxOPX'
#                       '6Kf2HnRhlRNB-3iV-OxDUvnyxAZbnbhBxQxtNRJQbP2a4cPHxj5-p7obUPUDMo9LUvW02cdot5yBbc8eIna5hjkbfJBQttjQn3hfIkj2CKLtD_-MKImjjD3-RJH-xQ0KnLXKKOLVhoVLp7ketn4hUt25xAe-47-b4r02T6Z-bceQxI-Mnc2QhrdQf4WWb3ebTJr32Qr-J3R5qTpsIJM5bbsj-uhQx5IL-JvaKviaKJHBMb1jpODBT5h2M4qMxtOLR3pWDTm_q5TtUJMeCnTDMFhe6jXjG88tTLqfKresJoq2RbhKROvhjR02M_gyxoObtRxtTcrW-Qd54jnennlylJ8bhL4jGJBLU3kBTn9LMnx--t58h3_XhjJ0PKPQttjQn3e2nnLXqQtLx3job7TyU42bf47yMRm0q4Hb6b9BJcjfU5MSlcNLTjpQT8r5MDOK5OuJRQ2QJ8BtC_-hK3P; BAIDUID_BFESS=1554213AAE9DF601903E257A16EEBCC9:FG=1; BDRCVFR[SatCmkszMoT]=Yy_VSn8ASxbmg9kPWm8mvqV; delPer=0; PSINO=3; BDUSS=JrV2MyfkpkTmV4S1NMajhVUVc0bG1OeHhRTk5zY1RyYjd-LXR2VnItU0plWnRoSUFBQUFBJCQAAAAAAAAAAAEAAABL96dPwbwxMjMxMjMzNgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAInsc2GJ7HNhQ1; BDUSS_BFESS=JrV2MyfkpkTmV4S1NMajhVUVc0bG1OeHhRTk5zY1RyYjd-LXR2VnItU0plWnRoSUFBQUFBJCQAAAAAAAAAAAEAAABL96dPwbwxMjMxMjMzNgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAInsc2GJ7HNhQ1; BDRCVFR[S4-dAuiWMmn]=I67x6TjHwwYf0; ZD_ENTRY=bing; STOKEN=b26c7be5be5335fb616617d4b2abf24970991fa67ba3d3dcbcb6f0521c6cd2ec; BDRCVFR[feWj1Vr5u3D]=I67x6TjHwwYf0; H_PS_PSSID=34067_31254_34712_34584_34517_34829_34579_34871_26350_34789; BAIDU_WISE_UID=wapp_1635229856764_912; 1336407883_FRSVideoUploadTip=1; video_bubble1336407883=1; IS_NEW_USER=4f2f8148556fdbe11ea64ae1; TIEBAUID=c6ccba2ccabf8e8ead8045b8; Hm_lvt_98b9d8c2fd6608d564bf2ac2ae642948=1635233406,1635233412,1635233417,1635233713; ab_sr=1.0.1_N2IwMjIxODNlNGUwODU0YWNmMDViYjU3NDBkMjY5Y2IzMDgyMDFiNTUxN2Q1YWIwOTg5NGJjYTFkOTFlY2RkYWJhZDBjYWQ2NWUxY2Y1Y2U0MjUxYzEwODA4MjM3NjJiZGMwZjU5MTgxYWY3NjJjN2Q4ZWJjM2Y1ZWY3ODhlNDM1ZjMxZDFmYTI4ODEyYjAwNmFiZDk0MWE4ZmM3MjA5ZmQyNGZhM2Q4ZDY4NDYwZWEzZDZkYjBlMzY2NzVjYTEx; st_data=e74b80406560233fdb1bbd38e6f486c3f8797e9c8384aca7680aaf218adf0fa50727c104116912a82c6d45039b78e84a445e9aa015c7fdcfd7139d7d8ed42655e89dd2420de3b8583587369ce5e3ea144d64d8be9b4cf4f6581ab18867ae0793cf083bb2c505d89f96c30b91c80dab2059abef9ea2a4592000dc5a46d079d80a; st_sign=b0f6873f; tb_as_data=1651d173cd24fff23438f745be3211a41af4921c5a5821321e19a3e3fbe3cdf8eb20db4f22acaa4cbcb5a5f912a62d4f821588616d2b77282f3d2d17c472cc8c8e44ae857b30f32a604269b4bcd7c462d3c53f2d2d314995191cf7e8f3ddbcb02ffa3e4fca13b3c0794533f036fd93df; Hm_lpvt_98b9d8c2fd6608d564bf2ac2ae642948=1635234614'
#         }
#
#         self.base_url = 'https://tieba.baidu.com'
#         self.data_list = []
#
#     def send_request(self, url):
#         time.sleep(random.uniform(0, 1))
#         response = requests.get(url, headers=self.headers)
#         return response.content
#
#     def parse_data(self, html):
#         html_str = html.decode().replace('<!--', '').replace('-->', '')
#         element = etree.HTML(html_str)
#         li_list = element.xpath('//ul[@id="thread_list"]/li')
#
#         for li in li_list:
#             item = {}
#             item['tittle'] = li.xpath('.//a[@class="j_th_tit "]/text()')[0]
#             item['detail_url'] =li.xpath('.//a[@class="j_th_tit "]/@href')[0]
#             item['detail_url'] = self.base_url + item['detail_url']
#
#             detail_response = self.send_request(item['detail_url'])
#             detail_element = etree.HTML(detail_response)
#             img_url_list = detail_element.xpath('//img[@class="BDE_Image"]/@src')
#             item['img_url_list'] = img_url_list
#
#             self.data_list.append(item)
#
#     def save_data(self):
#         for item in self.data_list:
#             img_url_list = item['img_url_list']
#
#             for img_url in img_url_list:
#                 img_response = self.send_request(img_url)
#
#                 file_name = img_url[-20:]
#                 with open(file_name, 'wb') as f:
#                     f.write(img_response)
#
#                 print(f'{img_url}----保存成功')
#
#
#     def start(self):
#         html = self.send_request(self.url)
#
#         with open('tieba.html', 'w', encoding='utf8') as f:
#             f.write(html.decode())
#             print('文件写入成功!')
#
#         self.parse_data(html)
#
#         self.save_data()
#
# if __name__ == '__main__':
#     spider = TiebaSpider('传智播客')
#     spider.start()






# import pymysql
#
# conn = pymysql.connect(host='127.0.0.1', port=3306,
#                        database='winfunc', user='root', password='root')
#
# cursor = conn.cursor()
#
# conn.begin()
#
# cursor.execute('insert into students values(10, "jack", 20, "Male", 4.00);')
#
# conn.commit()
#
# cursor.close()
# conn.close()



from pymysql import connect


def main():
    # 创建数据库连接对象
    conn = connect(host='localhost', port=3306,
                   database='python', user='root', password='root')
    # 创建游标对象
    cursor = conn.cursor()
    # 循环向 test_index 表中添加 10 万条测试数据
    for i in range(100000):
        cursor.execute("insert into test_index values('py-%d')" % i)
    # 提交数据
    conn.commit()


if __name__ == "__main__":
    main()
