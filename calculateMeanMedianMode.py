# Mean

list1 = [12,16,20,22,24,25,26,33,47,53,33]
mean =sum(list1)/len(list1)
print(mean)

# Meadian

list2= [22,34,54,64,3,45,67,4,3,44,89,43]
list2.sort()

if len(list2)%2 == 0:
    m1 = list1[len(list2)//2]
    m2 = list2[len(list2)//2 - 1]
    median = (m1+m2)/2
else:
    median= list2[len(list2)//2]
print(median)

# Mode

list3= [32,43,54,32,5,67,53,32,56,65,43,33]
frequency = {}
for i in list3:
    frequency.setdefault(i, 0)
    frequency[i]+=1
frequent= max(frequency.values())
for i,j in frequency.items():
    if j == frequent:
        mode = i
print(mode)