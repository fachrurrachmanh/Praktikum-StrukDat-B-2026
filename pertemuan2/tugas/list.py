thislist = ["apel","pisang","durian","mangga","pisang"]

print(thislist)

print(len(thislist))

alsoList = ["abc", 34, True, 40, "male"]

print(alsoList)

print(type(thislist))

thislist=tuple(thislist)
print(type(thislist))

print(alsoList[1])

print(alsoList[-1])

print(alsoList[1:4])

print(thislist[:4])

print(thislist[2:])

alsoList[1:5]=["def","hij","klmn"]
print(alsoList)

thislist=list(thislist)
thislist[1:2]=["anggur","melon","markisa"]
print(thislist)

alsoList.append("opqr")
print(alsoList)

thislist.insert(1, "jeruk")
print(thislist)

thislist.extend(alsoList)
print(thislist)

thisTuple = ("1","2")
thislist.extend(thisTuple)
print(thislist)

thislist.remove("pisang")
print(thislist)

thislist.pop(1)
print(thislist)

thislist.pop()
print(thislist)

del thislist[0]
print(thislist)

del alsoList
#print(alsoList) outputnya akan error karena alsoList sudah tidak ada lagi

thislist.clear()
print(thislist)

thislist=["apel","pisang","durian","mangga","pisang","jeruk"]
print(thislist)

for x in thislist:
    print(x)

print()

for x in range(len(thislist)):
  print(thislist[x])

print()

x = 0
while x < len(thislist):
  print(thislist[x])
  x = x + 1

print()

[print(x) for x in thislist]

newlist=[]
for x in thislist:
  if "a" in x:
    newlist.append(x)

print(newlist)

newlist = [x for x in thislist if "j" in x]
print(newlist)

newlist = [x for x in thislist if x != "apel"]
print(newlist)

newlist = [x for x in thislist]
print(newlist)

newlist = [x for x in range(10)]
print(newlist)

newlist = [x for x in range(10) if x < 5]
print(newlist)

newlist = [x.upper() for x in thislist]
print(newlist)

newlist = ['hello' for x in thislist]
print(newlist)

newlist = [x if x != "pisang" else "jeruk" for x in thislist]
print(newlist)

thislist.sort()
print(thislist)

thislist.sort(reverse = True)
print(thislist)

thislist=['pisang', 'pisang', 'mangga', 'Jeruk', 'Durian', 'apel']
thislist.sort()
print(thislist)

thislist.sort(key = str.lower)
print(thislist)

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print(mylist)

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)