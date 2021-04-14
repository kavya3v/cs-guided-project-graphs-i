#adjacency matrix
graph_matrix=[
    [0,1,0,0,0],
    [1,0,1,1,1],
    [0,1,0,1,0],
    [0,1,1,0,0],
    [0,1,0,0,0],]

#what the neighbours of A
graph_matrix[0]

#Check if B and C connected
graph_matrix[1][2] == 1

#adjacency list
graph_list={
    'A':{'B'},
    'B':{'A','C','D','E'},
    'C':{'B','D'},
    'D':{'B','C'},
    'E':{'B'},
}
#what are the neighbours of A
graph_list['A'] #gives the set

#Is B and C connected
'C' in graph_list['B'] #return True

#add connection from 'A' to 'C
graph_list['A'].add('C')

#add new vertix and connect a and c to it
graph_list['F']={'A','C'}
graph_list['A'].add('F')
graph_list['C'].add('F')

current_path =[]

def print_paths(graph,start_ver,current_path):
    #traverse a graph

#check https://leetcode.com/problems/all-paths-from-source-to-target/discuss/1101410/python-3-bfs-solution-faster-than-89

def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
    	stack = []
	l = len(graph[0])
	target = len(graph)-1

	for i in range(l):
		stack.append([0, graph[0][i]])
	res = []

	while stack:
		r = stack.pop()
		n = r[-1]
		if n==target:
			res.append(r)
		else:
			l = len(graph[n])

			for i in range(l):
				stack.append(r+[graph[n][i]])
	return res     


