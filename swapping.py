def swappingFile():
    file1=input("file1:")
    file2=input("file2:")
    with open(file1,"r")as a:
        data_a=a.read()
    with open(file2,"r")as b:
        data_b=b.read()
    with open(file1,"w")as a:
        data_a=a.write()
    with open(file1,"w")as b:
        data_b=b.write()