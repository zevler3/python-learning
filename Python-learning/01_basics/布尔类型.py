"""

布尔类型：用来表示“真(True)(1)”值或“假(False)(0)”值的数据类型


布尔值为 False 的情况如下
1、False 或者是 None

2、数值中的 0 ，包含 0 , 0.0 , 虚数 0

3、空序列，包含空字符串、空元组、空列表、空字典、空集合

4、自定义对象的实例，该对象的 __bool__() 方法返回 False 或 __len__()方法返回 0

"""

x=True
print(x)
print(type(x))
print(x+10) # 11 → 1+10
print(False+10) # 10 → 0+10

#在Python中一切皆对象，一个变量其实就是一个对象，每一个对象都会有一个布尔值

#使用内置函数bool()测试对象的布尔值
print(bool(666)) # 非0的整数的布尔值皆为true

print(bool('周明瑞')) #所有的非空字符串皆为true
print(bool(''))

print(bool('False'))
print(bool('None'))

