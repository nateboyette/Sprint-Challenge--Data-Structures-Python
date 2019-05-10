import time
from binary_search_tree import BinarySearchTree
from max_heap import Heap

start_time = time.time()


nameList = BinarySearchTree("Sample Name")

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names

f.close()

duplicates = Heap()

for name in names_1:
    duplicates.insert(name)
    print(name)

for name in names_2:
    duplicates.insert(name)

print(duplicates)

end_time = time.time()
# print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")


