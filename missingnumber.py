def missingNumber(n):
    number=set(n)
    lenght= len(n)
    output=[]
    for i in range (1, n[-1]):
        if i not in number:
            output.append(i)
    return output


listOfNumbers = [1,2,5,6,8,9,10,13,15,16]
print(missingNumber(listOfNumbers))