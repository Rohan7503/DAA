def Solve(A):
	for i in range(1,len(A)):
		for j in range(1,len(A[0])):
		
			if s1[i]==s2[j]:
				A[i][j]=A[i-1][j-1]+2
			else:
				A[i][j]=max([ A[i-1][j], A[i-1][j-1], A[i][j-1] ]) - 1



def Prims(G):

	INF = 9999999
	N = len(G)-1
	selected_node = [0 for i in range(N) ]
	no_edge = 0
	selected_node[0] = True

	print("Edge : Weight\n")
	while (no_edge < N - 1):
		minimum = INF
		a = 0
		b = 0
		for m in range(N):
			if selected_node[m]:
		    		for n in range(N):
		        		if ((not selected_node[n]) and G[m+1][n+1]):  
		            			# not in selected and there is an edge
		            			if minimum > G[m+1][n+1]:
		                			minimum = G[m+1][n+1]
		                			a = m
		                			b = n
		print(str(a+1) + "-" + str(b+1) + ":" + str(G[a+1][b+1]))
		selected_node[b] = True
		no_edge += 1


def Display(A):
	print()
	for i in ' '+s2:
		print(i,end='   ')
	print('\n')
	
	idx=0
	for i in A:
		print(s1[idx], end='  ')
		idx+=1
		for j in i:
			print("{x:>2}".format(x=str(j)),end='  ')
		print()
	
	print()


# main
s1='-AGCTAGTACGCT'
s2='-ACTGATCGATCG'
A = [ [0 for i in range(13)] for i in range(13) ]
G = [ [0 for i in range(13)] for i in range(13) ]


Solve(A)

for i in range(13):
	for j in range(13):
		if i not in [j,j-1,j+1]:
			G[i][j]=0
		else:
			G[i][j]=A[i][j]

Display(A)
Display(G)

Prims(G)
