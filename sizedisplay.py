import os

dropout = 0.1

def getDirs(path = '.'):
    dirs = []
    for root, dirs, filenames in os.walk(path):
        for fileName in filenames:
            dirs.append(fileName)
        break   #prevent decending into subfolders
    return dirs

    
def getSize(start_path = '.'):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total_size += os.path.getsize(fp)
    return total_size


def convSize(size):
    sizes = []

    for i in range(0,4):
        sizes.append(size)  # [0]Byte [1]kB  [2]MB  [3]GB
        size = round(size / 1024, 2)
        if size < 0.01:
            size = 0.01

    return sizes


def sortSec(a, reverse=False):
    sort = {}
    tmpList = []

    for i in a.keys():
        tmpList.append(a[i])
    tmpList = sorted(tmpList, reverse=reverse)

    nameList = []
    for i in a.keys():
        nameList.append(i)
    
    for i in tmpList:
        for j in nameList:
            if a[j] == i:
                sort[j] = i
                nameList.remove(j)
                break
    return sort


def getTotalSize(a):
    total = 0
    for i in a.keys():
        total = total + a[i]
    return round(total, 2)

# ---------

print(" Start")

dirs = getDirs()
a = {}

for j, i in enumerate(dirs):
    try:
        size = convSize(getSize(i))      
#        print(str(size[3]) + " " + i)
        a[i] = size[3] #size first easyer to sort but dubble index possible!!
    except FileNotFoundError:
        print("ERROR " + i)

print(" ------- \n")

#for i in sorted(a.keys(), reverse = True): #size first
#    print(a[i] + ' ' + i)


sort = sortSec(a)

for i in sort.keys():
    if sort[i] < dropout:
        continue
    print(str(sort[i]) + "GB " + i)
print("---------")
print(str(getTotalSize(a)) + "GB Total")

input("Press Key to exit")


