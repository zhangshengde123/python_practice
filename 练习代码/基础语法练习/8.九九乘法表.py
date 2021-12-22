#for循环
# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f'{i}*{j} = {i*j}', end='\t')
#     print('\n')

#while循环
i = 1

while i < 10:
    j = 1
    while j <= i:
        print(f'{i}*{j} = {i*j}', end='\t')
        j = j +1
    i = i+1
    print()



