a=100 #变量a，值为100
b=50 #变量b，值为50
print(90,sep=',' ,end=',',file=None,flush=False)
print(a,sep=',' ,end='\n',file=None,flush=False) #输出变量的值，a的值为100
print(a,b,sep=',' ,end='\n',file=None,flush=False)#print的完整语法格式
#“sep=”→分隔符号的赋值，“end=”→终结符号的赋值，“file=None”→显示区域，“flusn=False”→是否立即执行
#ASCII码字符转换
print(chr(88))
print(ord("川"))#中文unicode码
print(chr(24029))
fp=open('test 1.0.txt', 'w', encoding='utf-8')#打开文件，w→write，encoding='utf-8'→统一文件的编码格式与编辑器格式统一
print("糟蒙了！！！",file=fp)#将内容输出至文件text中
fp.close()#关闭文件
with open("test 2.0.txt", "w", encoding='utf-8') as f:#进阶写法,不需要书写.close()
    print("赞美愚者！！！",file=f)
print("周明瑞"+"克莱恩")
print("周明瑞"'克莱恩',sep='')