class Node():
	def __init__(self, key, value):
		self.__key = key
		self.__value = value

class Edge():
	def __init__(self, node_from, node_to):
		self.__node_from = node_from
		self.__node_to = node_to
	
	def destroy(self):
		node = self.__node_to
		self.__node_from = None
		self.__node_to = None
		return node

class Graph():
	def __init__(self):
		self.__edges = {}
		self.__nodes = {}

	def add_node(self, key, value, node_to=None):
		node_from = Node(key,value)
		edges = [Edge(node_from,node_to)]
		if node_from in self.__edges:
			edges += self.__edges[node_from]
		self.__nodes[key] = node_from
		self.__edges[node_from] += edges
		
	def add_edge(self):
		pass
		
	def __remove_edges(self, node_from):
		return self.__edges[node_from].pop() if node_from in self.__edges else None
		
	def remove_edges(self,node_from):
		nodes = []
		edges = self.__remove_edges(self,node_from)
		if edges != None:
			for edge in edges:
				nodes += [edge.destroy()]
		return nodes
