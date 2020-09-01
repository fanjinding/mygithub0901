"""
@project: FM
@author: fanjinding
@time: 2020/1/8 17:10
"""
# 99乘法表
for j in range(1, 10):
    for i in range(1, j + 1):
        print("%d*%d=%d" % (i, j, i * j), end=" ")
    print("")
