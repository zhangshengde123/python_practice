import datetime
# 输出指定格式的日期


# 输出今日日期，格式为 dd/mm/yyyy。更多选项可以查看 strftime() 方法
print(datetime.date.today().strftime('%Y/%m/%d'))

# 创建日期对象
birthDate = datetime.date(1941, 1, 5)

print(birthDate.strftime('%Y/%m/%d'))

# 日期算术运算
birthNextDay = birthDate + datetime.timedelta(days=1)

print(birthNextDay.strftime('%Y/%m/%d'))

# 日期替换
firstBirthday = birthDate.replace(year=birthDate.year + 1)

print(firstBirthday.strftime('%Y/%m/%d'))