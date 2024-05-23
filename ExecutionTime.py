from time import time
start = time()

# python program to create acronyms

word = "artificial intelligence"
text = word.split()
a = ""
for i in text:
    a = a+str(i[0]).upper()
    print(a)

    end = time()
    execution_time = end - start
    print("Execution TIme: ", execution_time)