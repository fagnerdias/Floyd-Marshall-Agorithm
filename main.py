def floydWarshall(graph): 
	dist = graph
	for k in range(V): 
		for i in range(V):  
			for j in range(V):
				dist[i][j] = min(dist[i][j] , dist[i][k]+ dist[k][j]) 
	isNegCicle(dist)
	printSolution(dist)

def isNegCicle(dist):
	for k in range(V):
		if dist[k][k] < 0:
			print("The graph has a negative cicle")
	print("The graph has not a negative cicle")	
    				 

def printSolution(dist): 
	for i in range(V): 
		for j in range(V): 
			if(dist[i][j] == INF): 
				print ("%7s" %("INF")), 
			else: 
				print ("%7d\t" %(dist[i][j])), 
			if j == V-1: 
				print (" ")

graph = []		 
INF = 99999	
ref_arq = open('test.txt','r')
V = int(ref_arq.readline())

for line in ref_arq:
	values = line.split()
	tmp = []
	for k in values:
		if k == 'INF':
				k = INF
		tmp.append(int(k))
	graph.append(tmp)
print(graph)
ref_arq.close()

floydWarshall(graph); 

