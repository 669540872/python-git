#嵌套列表解析:以下实例展示了3X4的矩阵列表：
matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12], ]

print([[row[i] for row in matrix] for i in range(4)])