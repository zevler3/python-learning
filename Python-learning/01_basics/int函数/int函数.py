print(int('101',2))#进制转换，“2”代表二进制

age=int(input('请输入年龄：'))#配合 input() 把用户输入转成整数
#到这一步为止是将用户所输入的数据存在名为“age”的盒子里

#括号里面套括号：里面做完做外面

#等价于
text = input("请输入年龄：")   # text 是字符串，比如 "18"
age = int(text)               # 把字符串转成整数 18
print(age)

'''
"配合 input() 把用户输入转成整数"
这句话的意思是：input()拿到的是文字，int()把它变成数字，两个经常一起用。

'''
age = input("请输入年龄：")#你输入18，但age里存的是字符串："18",不是数字 18。

#可以用type()验证：

age = input("请输入年龄：")
print(type(age))

#type() 是 Python 的内置函数，作用是：查看一个东西是什么类型。


'''

文字不能直接做数学计算
比如：
age = input("请输入年龄：")
print(age + 1)

你输入18，程序会报错：TypeError: can only concatenate str (not "int") to str


因为 "18" + 1是“文字加数字”，Python 不知道你想干什么,但如果是数字就没问题。


 先让用户输入文字，再把文字转成整数,常见写法：

age = int(input("请输入年龄："))
height = int(input("请输入身高："))
score = int(input("请输入分数："))
count = int(input("请输入数量："))

这些都是同一个套路：

变量 = int(input("提示："))

'''