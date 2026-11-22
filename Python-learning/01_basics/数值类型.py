#整数类型：无小数部分的数值类型，包含正整数、负整数和0

#整数的四种表现形式
num=987 #默认十进制，表示整数
num2=0b010101 #使用二进制表示整数，"ob"开头,字母大小写均可
num3=0o765 #八进制 (0o)
num4=0x87ABF #十六进制 (0x)
print(num)
print(num2)
print(num3)
print(num4)


#浮点数类型：带有小数部分的数值，由整数部分与小数部分组成

#注意：两个浮点类型的数进行运算时，有一定概率运算结果后增加一些“不确定的”尾数




#浮点数的使用
height=175.5
print(height)
print(type(height))

#不确定的尾数问题
print(0.1+0.2)
print(round(0.1+0.2,1)) # round()保留小数数位


#复数类型的使用：Python中的复数与数学中的复数形式完全一致，由实部(.real)与虚部(.imag)组成
x=123+456j
print('实数部分：',x.real)
print('虚数部分：',x.imag)
