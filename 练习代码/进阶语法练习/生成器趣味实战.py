#使用生成器实现遍历文件中所有的单词
def generateWord(file):
    while True:
        line = file.readline()
        if not line:
            break
        words = line.split()
        for word in words:
            yield word

# file = open('test.txt')
# count = 0
# generator = generateWord(file)
# while True:
#     try:
#         word = next(generator)
#         print(word)
#         count += 1
#
#     except StopIteration:
#         break
#

#统计单词出现的频率
file = open('test.txt')
dict = {}
generator = generateWord(file)
for word in generator:
    if word in dict:
        dict[word] += 1

    else:
        dict[word] = 1

for word, count in dict.items():
    print(f'{word},{count}')



