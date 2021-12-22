#用生成器输出0到4
generator = (i for i in range(5))
while True:
    try:
        item = next(generator)
        print(item)
    except StopIteration:
        break





# class Node:
#     def __init__(self, item):
#         self.item = item
#         self.next = None
#
#
# class Stack:
#     def __init__(self):
#         self.head = None
#
#     def push(self, item):
#         node = Node(item)
#         node.next = self.head
#         self.head = node
#
# stack = Stack()
# stack.push('a')
# stack.push('b')
# stack.push('c')
#
# def stackGenerator(stack):
#     cursor = stack.head
#     while cursor != None:
#         yield cursor.item
#         cursor =cursor.next
#
# generator = stackGenerator(stack)
#使用while循环遍历
# while True:
#     try:
#         item = next(generator)
#         print(item)
#     except StopIteration:
#         break
#使用for循环遍历
# for item in generator:
#     print(item)





