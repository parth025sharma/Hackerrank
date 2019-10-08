#!/usr/bin/python3

N,K=map(int,input().split()) 
pair_list=list(map(int,input().split()))
#for i in range(0,len(pair_list)): 
 #   pair_list[i]=int(pair_list[i])

pair_list=sorted(pair_list)
total_pairs,x,y=0,0,0
while x < N:
	if pair_list[x]-pair_list[y]==K:
		total_pairs=total_pairs+1
		x=x+1
		y=y+1
	elif pair_list[x]-pair_list[y] < K:
		x=x+1
	elif pair_list[x]-pair_list[y] > K:
		y=y+1
		
print(total_pairs)
