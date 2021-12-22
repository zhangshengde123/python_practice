str1 = input('请输入字符串：')
letter = 0
space = 0
digit = 0
other = 0
for c in str1:
    if c.isalpha():
        letter += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        other += 1
print(f'letter的个数是：{letter} space的个数是：{space} digit的个数是：{digit} 特殊字符个数是：{other}')



