import time

year = int(input("请输入年份："))
month = int(input("请输入月份："))
day = int(input("请输入日期："))
day_num = 0
month_list = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304,334]

if ((year % 4) == 0 or (year % 100) == 0) and (year % 400) != 0:
    if 1 <= month <= 12:
        if month < 3:
            day_num = month_list[month-1] + day
            print(f"这是这年的的第{day_num}天")
        else:
            day_num = month_list[month - 1] + day
            print(f"这是这年的的第{day_num}天")
    else:
        print("错误")
else:
    if 1 <= month <= 12:
        if month < 3:
            day_num = month_list[month-1] + day
            print(f"这是这年的的第{day_num}天")
        else:
            day_num = month_list[month - 1] + day +1
            print(f"这是这年的的第{day_num}天")
    else:
        print("数据错误")


