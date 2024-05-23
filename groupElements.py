inputLists = [[10,20,30],[40,50,60],[70,80,90]]
outputList = []
index=0

for i in range (len(inputLists[0])):
    outputList.append([])
    for j in range(len(inputLists)):
        outputList[index].append(inputLists[j][index])
    index = index + 1
a,b,c = outputList[0],outputList[1],outputList[2]
print(a, b, c)