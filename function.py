def countingWords():
    fileName=input("Enter File Name:")
    file=open(fileName,"r")
    numberOfWords=0
    for line in file:
        words=line.split()
        numberOfWords=numberOfWords+len(words)
    print("numberOfWords:")
    print(numberOfWords)

countingWords()