class Node():
	def __init__(self, name, value, level=0, parent=None):
		self.__name = name
		self.__value = value
		self.__level = level
		self.__parent = parent
		self.__edges = []

	def get_edges(self):
		return self.__edges

	def get_name(self):
		return self.__name
	
	def get_value(self):
		return self.__value
	
	def get_level(self):
		return self.__level

	def get_parent(self):
		return self.__parent

	def __str__(self):
		return "{}: {}, {}".format(self.__name, self.__value, self.__level)
	
	def __repr__(self):
		return self.__str__()
	
	def add_edge(self, to, edge_value):
		edge = Edge(self, to, edge_value)
		self.__edges += [edge]
		return edge
	
	def remove_edge(self, edge):
		self.__edges.remove(edge)

class Edge():
	def __init__(self, node_from, node_to, value):
		self.__node_from = node_from
		self.__node_to = node_to
		self.__value = value

	def get_from(self):
		return self.__node_from

	def get_to(self):
		return self.__node_to

	def get_value(self):
		return self.__value

	def __str__(self):
		return "{} ={}=> {}".format(self.__node_from.get_name(), self.__value, self.__node_to.get_name())

	def __repr__(self):
		return self.__str__()

class Graph():
	def __init__(self):
		self.__nodes = {}
	
	def get_nodes(self):
		return self.__nodes

	def __str__(self):
		return "{}".format(len(self.__nodes))

	def __repr__(self):
		return self.__str__()

	def add_node(self, name, value=None):
		if value == None:
			value = name
		if self.find_node(name) == None:
			node = Node(name, value)
			self.__nodes[name] = node
			return node
		return None

	def find_node(self, name):
		if name in self.__nodes:
			return self.__nodes[name]
		else:
			return None
		
	def add_edge(self, from_name, to_name, edge_value=None):
		node_from = self.find_node(from_name)
		node_to = self.find_node(to_name)

		if node_from == None or node_to == None:
			raise Exception('node_from == None or node_to == None')

		if edge_value == None:
			edge_value = node_to.get_name()

		return node_from.add_edge(node_to, edge_value)
		
	def get_neighbours(self, from_name):
		node_from = self.find_node(from_name)

		if node_from == None:
			raise Exception('!find_node(from_name)')
		
		neighbours = []

		for e in node_from.get_edges():
			neighbours += [e.get_to()]
		
		return node_from, neighbours

	def reverse(self):
		graph_rev = Graph()
		for name,node in self.get_nodes().items():
			graph_rev.add_node(node.get_name(), node.get_value())
		
		for name,node in self.get_nodes().items():			
			for e in node.get_edges():
				graph_rev.add_edge(e.get_to().get_name(), e.get_from().get_name(), e.get_from().get_name())
		
		return graph_rev
		

