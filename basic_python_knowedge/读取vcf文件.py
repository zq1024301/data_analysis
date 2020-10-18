path = r"C:\Users\sunny\Desktop\zuhui\Bacillus_subtilis.snp.vcf"
output_path = r"C:\Users\sunny\Desktop\zuhui\a.txt"
f = open(path, 'r')
buff = open(output_path, 'w')
for line in f.readlines():
    line = line.split()
    res = ''
    res = res + line[0] + ',' + line[1] + ',' + line[3] + ',' + line[4] + ',' + line[5]
    buff.write(res)
    buff.write('\n')
f.close()
buff.close()


class FileProcess():

    def __init__(self, read_path, write_path):
        self.read_path = read_path
        self.write_path = write_path
        self.buffer = []

    def read_(self):
        f = open(self.read_path, 'r')
        for line in f.readlines():
            line = line.split()
            res = ''
            res = res + line[0] + ',' + line[1] + ',' + line[3] + ',' + line[4] + ',' + line[5] + '\n'
            self.buffer.append(res)
        f.close()

    def write_(self):
        f = open(self.write_path, 'w')
        for line in self.buffer:
            f.write(line)
        f.close()

if __name__ == '__main__':
    read_path = r"C:\Users\sunny\Desktop\zuhui\Bacillus_subtilis.snp.vcf"
    write_path = r"C:\Users\sunny\Desktop\zuhui\b.txt"
    f1 = FileProcess(read_path, write_path)
    f1.read_()
    f1.write_()









