from collections import deque

# BFS
def hasRoute1(G, begin, end):
	visited = {}
	queue = deque()
	if begin != None:
		queue.append(begin)
	while len(queue) != 0:
		node = queue.popleft()
		if node == end:
			return True
		if node not in visited:
			visited[node] = True
		for nd in G.get(node, []):
			queue.append(nd)
	return False

# DFS
hasRoute2(G, begin, end, visited = None):
	if visited == None:
		visited = {}
	if begin == end:
		return True
	visited[begin] = True
	for node in G.get(begin, []):
		if node not in visited:
			if hasRoute2(G, node, end, visited):
				return True
	return False

G = dict()
G[1] = [6,2,3]
G[2] = [4,3]
G[3] = [5]
G[4] = [6,5]
print hasRoute1(G, 4, 1)
print hasRoute1(G, 1, 4)
print hasRoute1(G, 2, 3)
print hasRoute1(G, 3, 2)
print hasRoute1(G, 1, 7)
