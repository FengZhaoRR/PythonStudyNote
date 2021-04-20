##day 6 文件
##
##文件的打开
##打开文件使用open() 函数
##第一个参数：打开的文件名
##第二个参数：打开模式，默认以只读(r) 去打开文件
##1.r: 只读方式打开，只能打开已经存在的文件
##2.w:只写方式打开，如果文件不存在，则会创建旧文件
##每次打开文件的时候，都会覆盖原先之前的旧文件
##3. a:追加，如果文件不存在，则创建新文件，不会覆盖原先内容



##相对路径: ./代表同级路径，或者不写
##相对路径: ../代表上一级路径
##绝对路径:从电脑的磁盘位置出发
##open(r'test1.txt','a')

##文件的写入
##write()  写入数据，每次写入一条数据
##f = open('test.txt','w')
##f.write ('\nhello world!')
##f.writelines(['\nthis','\nis','\npython'])
##f.flush()  #flush 刷新，保存数据
##f.close() #关闭文件，自动保存

##文件的读取
##read() 读取内容
##当不写值的情况下，读取文件里面全部的内容
##当写值得情况下，读取一定长度的内容
##readline()  :读取一行的内容
##readlines() :读取多行的内容，并把内容放在列表里存储
##f = open('test.txt','r')
##pritn(f.readlines())
##f.close()


##可读可写
##r+:会把前面的内容写入的时候覆盖掉
## a+: 会把数据加在文件的最后面
##b:代表以二进制操作文件,图片，视频，音频
##f =  open('test.txt','ab+')
##f.write(b'\nhello world44')
####把文件的指针移到文件开头
##f.seek(0)
##print(f.read())
##f.close()

##with open (上下文管理器)：自动关闭文件
##with open('test.txt','a+') as f :
##     f.seek(0)
##     print(f.read())


##文件流
##read() :
##getvalue():获取文件内容，并且不需要重新定义光标（指针）位置
##close(): 关闭文件，关闭之后整个内容都不存在，会被释放掉
##import io
####生成字符串临时假文件
##str_io = io.StringIO()
##str_io.write('my name is rourou')
####str_io.seek(0)
##print(str_io.getvalue())



##import io
#### 生成二进制临时假文件
##b_io=io.BytesIO()
##b_io.write(b'hello world')
##print(b_io.getvalue())
##b_io.close()




##文件目录操作
##os:与操作系统交互的模块
##import os
##getcwd(): 获取当前文件路径
##os.chdir():切换路径，该路径必须要存在
##os.listdir():查看目录下的文件和子目录，以列表方式进行显示
##os.mkdir():创建文件夹
##os.rmdir():删除文件夹，只能删除空文件夹
##os.makedirs(r'aaa\bbb\ccc'):创建多层目录
##os.removedirs():删除多层目录，只能删除空的目录
##os.system('cmd'):调用系统的cmd
##os.system('python'):调用系统的cmd ，并进入python
##os.walk(r'D:\python学习')遍历文件夹
##os.remove(r'绝对路径') 移除文件
##os.rename(原文件名，新文件名) 重命名
##os.path.join(路径1，路径2)

##模块和包
##模块: 在python中，模块指的就是一个Py文件
##import a

##import是全部导入，from是部分导入
##import datetime
##获取当前时间
##print(datetime.datetime.now())

##from datetime import datetime as dt
##print(dt.now())


##import sys
##sys.path :查看系统可导入模块的路径
##sys.path.append(r'绝对路径')  导入自定义模块  /添加一个模块导入的路径



##当前文件直接运行时，__name__值为__main__
##当文件作为模块被导入时，__name__值为文件名

##import sys
##if __name__ == '__main__':
##     print('这是a自己在运行')
##     #获取参数输入，直接运行时打印当前文件的路径
##     print(sys.argv)


##包：其实就是存放多个模块的文件夹
##从datetime 包里导入一个datetime的模块 命名为dt
##from datetime import datetime as dt
##print(dt.now())

















