import data_structure

def aval_function(node_state):
    return len(node_state.get_name()) + node_state.get_level()

def get_successors(graph, node_state):
    successors = []
    edges = []   

    for name, node in graph.get_nodes().items():
        for e in node.get_edges():
            if e.get_value() in node_state.get_name():
                edges += [e]
                # print(nodes)

    for e in edges:
        new_state_name = '{}'.format(node_state.get_name().replace(e.get_value(),e.get_from().get_value()))
        new_state_value = e
        new_level = node_state.get_level() + 1
        new_node = data_structure.Node(new_state_name,new_state_value, new_level, parent=node_state)
        
        successors += [new_node]

    return successors

def search(graph, node_start):
    found = False
    successors = [node_start]
    last_successors = successors
    min_len = int(2**32)
    for name, node in graph.get_nodes().items():
        if len(name) < min_len:
            min_len = len(name)
    
    while not found:
        successors, found = searching(graph,successors, lambda x: len(x.get_name()) == min_len)
        
        if len(successors) == 0:
            print('= '*25)
            print()
            break
        else:
            last_successors = successors

    min_len = int(2**32)
    idx = 0
    for i in range(len(last_successors)):
        succ = last_successors[i]
        if len(succ.get_name()) < min_len:
            min_len = len(succ.get_name())
            idx = i
        
    return last_successors[idx]

def searching(graph, successors, stop_criterion):
        
    next_successors = []
    found = False
    for succ in successors:
        next_succ = get_successors(graph,succ)
        for each_succ in next_succ:
            next_successors += [each_succ]
            if stop_criterion(each_succ):                
                found = True
                return [each_succ], found
                        
    return next_successors, found