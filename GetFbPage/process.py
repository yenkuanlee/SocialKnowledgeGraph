import sys
f = open(sys.argv[1],'r')
Rset = set()
while True:
    line = f.readline()
    if not line:break
    line = line.replace("\n","")
    tmp = line.split("\t")
    if tmp[0] not in Rset:
        Rset.add(tmp[0])
        print line
    else:
        pass
