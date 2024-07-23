file=open('sample.txt')
#Read all content of file
#print(file.readline())
line=file.readline()
while line!="":
    print(line)
    line=file.readline()


file.close()