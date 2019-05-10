import time


start_time = time.time()


f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names

f.close()

duplicates = []

nameList1 = set()
nameList2 = set()

for name in names_1:
    nameList1.add(name)

for name in names_2:
    nameList2.add(name)

duplicates = nameList1.intersection(nameList2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")


