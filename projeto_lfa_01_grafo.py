import data_structure
import a_star

producao = [
 {"S"	:	"XY"	},
 {'X'	:	'XaA'	},
 {'X'	:	'XbB'	},
 {'X'	:	'F'	},
 {'Aa'	:	'aA'	},
 {'Ab'	:	'bA'	},
 {'AY'	:	'Ya'	},
 {'Ba'	:	'aB'	},
 {'Bb'	:	'bB'	},
 {'BY'	:	'Yb'	},
 {'Fa'	:	'aF'	},
 {'Fb'	:	'bF'	},
 {'FY'	:	"@e@"	}
 ]

def gerar_grafo(producao):
    grafo = data_structure.Graph()
    for p in producao:
        for k,v in p.items():
            grafo.add_node(k)
            grafo.add_node(v)
    
    for p in producao:
        for k,v in p.items():
            grafo.add_edge(k,v, edge_value=v)
    
    return grafo



for p in producao:
        print(p)

print()

grafo_producao = gerar_grafo(producao)

for name, node in grafo_producao.get_nodes().items():
        for e in node.get_edges():
                print(e)

print()

phrase = 'baba, nao existe: [iXXo], existe: [iXYXYo XaA I@e@@e@O], ba@e@ba ba@e@ba@e@ba@e@ba ba@e@baSba@e@ba ba@e@baSba@e@ba ba@e@baSba@e@ba ba@e@baSba@e@ba'
node_start = data_structure.Node(phrase,'start')

first_node = a_star.search(grafo_producao, node_start)

node = first_node

while node.get_parent() != None:
        print(node)
        node = node.get_parent()
        if node.get_parent() == None:
                print(node)

print()

# import sys
# if __name__ == '__main__':
