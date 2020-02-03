# x = 6
# r=x%2
# if r==0:
#     print('是偶数')
#     if x>8:
#         print('x是大于8的数字')
# else:
#     print('是奇数')
# print('结束了！')

x=input('请输入一个数字：')
x=int(x)
if x==5:
    print('恭喜你猜对了！')
elif x>5:
    print('你猜的数字偏大！')
elif x<5:
    print('你猜的数字偏小！')