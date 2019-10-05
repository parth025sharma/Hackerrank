#!/usr/bin/python3

n=int(input())
names=[]
for i in range(0,n):
	names.append([input(),int(input())])

names.remove([names[i],names[i][1])
