import linecache
import os

def outputfile(i,j,n):
    # zh = file_zh.read().decode('utf-8').encode('gbk', 'ignore')
    if os.path.exists('2.txt'):
        os.remove('2.txt')
    file_new = open ('2.txt', 'wt')
    for l in range(i,j+1):
        # line = linecache.getline('tw.txt', l).decode('utf-8').encode('gbk', 'ignore')
        if(l%5==3):
            continue
        elif(l%5==4):
            line1 = str(linecache.getline('1.txt', l-1)[0:-1]).strip()
            line2 = str(linecache.getline('1.txt', l)[0:-1]).strip()
            if(len(str(line1[0:-1]))==0):
                continue
            file_new.write(''+ line2 +'\n')
            file_new.write(''+ line1 +'\n')
        else:
            line1 = str(linecache.getline('1.txt', l)[0:-1]).strip()
            file_new.write(''+ line1 +'\n')
    file_new.close()

filename = "1.txt"
myfile = open(filename)
lines = len(myfile.readlines())
outputfile(1,lines,1)
