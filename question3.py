from question4 import ListUtils

def doubleList(numberList):
	for n in numberList:
		print(n*2)

print(doubleList([3,1,5]))

list2 = ListUtils([],0)

print(list2.contents)