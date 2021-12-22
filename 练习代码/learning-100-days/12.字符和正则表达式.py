# import re
#
#
# def main():
#     username = input("zhagnhao:")
#     password = input("mima:")
#     m1 = re.match(r'^[1]{1}[0~9]{2,11}$', username)
#     if not m1:
#         print('请输入有效的用户名')
#     m2 = re.match(r'^[0~9]\d{0,5}$', password)
#     if not m2:
#         print("请输入有效的密码")
#     if m1 and m2:
#         print('通过')
#
#
# if __name__ == '__main_':
#     main()
"""
验证输入用户名和QQ号是否有效
要求：用户名必须由字母、数字或下划线构成且长度在6~20个字符之间，QQ号是5~12的数字且首位不能为0
"""

import re

# def main():
#     username = input('请输入用户名: ')
#     qq = input('请输入QQ号: ')
#     # match函数的第一个参数是正则表达式字符串或正则表达式对象
#     # 第二个参数是要跟正则表达式做匹配的字符串对象
#     m1 = re.match(r'^[1]{1}[0-9a-zA-Z_]{6,10}$', username)
#     if not m1:
#         print('请输入有效的用户名.')
#     m2 = re.match(r'^[1-9]\d{4,11}$', qq)
#     if not m2:
#         print('请输入有效的QQ号.')
#     if m1 and m2:
#         print('你输入的信息是有效的!')
#

"""
------------------------------------------------------------------------
例二:从一串文字中提取手机号
----------------------------------------------------------------------------
"""

# def main():
#     pattern = re.compile(r'(?<=\D)1[34578]5\d{8}(?=\D)')
#     sentence = '''
#     重要的事情说8130123456789遍，我的手机号是13512346789这个靓号，
#     不是15600998765，也是110或119，王大锤的手机号才是15600998765，
#     王宝强的才是17535434543。
#     '''
#     #查找所有匹配并保存到一个列表中
#     numlist = re.findall(pattern, sentence)
#     print(numlist)
#     #通过迭代器取出匹配对象并获得匹配的内容
#     for temp in pattern.finditer(sentence):
#         print(temp.group())
#     print('------华丽的分界线')
#     #通过search函数指定搜索位置找出所有匹配
#     m = pattern.search(sentence)
#     while m:
#         print(m.group())
#         m = pattern.search(sentence, m.end())

"""
------------------------------------------------------------------------
例三:替换字符中的不良内容
----------------------------------------------------------------------------
"""


# def main():
#     sentence = '我操你大爷的，去死吧你，你好骚啊，fuck you.'
#     sub_sentance = re.sub('fuck |操|死|骚', '#', sentence, flags=re.IGNORECASE)
#     print(sub_sentance)

"""
------------------------------------------------------------------------
例三:拆分字符串
----------------------------------------------------------------------------
"""


def main():
    poem = "窗前明月光，疑是地上霜。举头望明月，低头思故乡。"
    sentence_list = re.split('[，。]', poem)
    while '' in sentence_list:
        sentence_list.remove('')
        print(sentence_list)

if __name__ == '__main__':
    main()

