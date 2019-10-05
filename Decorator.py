import operator
a=[]
for i in range(1,int(input())+1):
    a.append(input().split(" "))
a=a.sort(key=operator.itemgetter(2))
print(a)
