f = open("1.txt", encoding="utf-8")
f_write = open("4.txt", "w", encoding="utf-8")

while True:
    text = f.readline()

    if not text:
        break

    f_write.write(text)  # 按行复制
    # print(text, end='')


f.close()
f_write.close()


