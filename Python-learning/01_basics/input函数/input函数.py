name=input('请输入您的名字：')
print('我的名字是：'+name)
num=input('请输入您的幸运数字：')
print("您的幸运数字是"+num)#此时“num”是字符串，需要用“+”连接
num=int(num)#使用内置函数将num转换为整数，int函数的作用就是把其他类型的数据转换成整数，或直接创建一个整数对象
print("您的幸运数字是",num)
