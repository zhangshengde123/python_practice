"""
写一个删除列表中重复元素的函数，要求去重后元素相对位置保持不变

"""
def dedup(items):
    list1 = []
    seen = set()
    for i in items:
        if i not in seen:
            list1.append(i)
            seen.add(i)
    return list1


#  使用生成器的方式

def dedup2(items):
    seen = set()
    for i in items:
        if i not in seen:
            yield i
            seen.add(i)



list2 = [3, 5, 6, 7, 2, 5, 3, 66, 34, 12, 4, 5]
# print(set(list2))
print(dedup(list2))

for i in (dedup2(list2)):
    print(i)