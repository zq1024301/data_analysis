f = open("1.txt", 'r', encoding="utf-8")  # open默认以只读的方式打开文件,当打开不存在的文件时会报错
f_write = open("2.txt", 'w', encoding="utf-8")  # write当文件不存在时会新建文件

b = f.read()  # 再一次运行中光标从头运行到结尾，所以再次读取会读取不到内容
f_write.write(b)  # 复制粘贴
f_write.write("你好")  # 在结尾处接着写入


f.close()
f_write.close()



