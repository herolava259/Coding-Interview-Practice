from collections import defaultdict
from C2_W1.DeBruijnGraph_with_k_mers_problem import DeBruijnGraph
from numpy import random
from C2_W1.StringSpelled_by_a_GAT import PathToGenome

def binary_k_mers(k):
    bin_mers = []
    containers = []
    for i in range(k):
        bin_mers.append(0)
    num_loop = 2**k - 1
    containers.append(bin_mers.copy())
    for i in range(num_loop):
        j = k-1
        while bin_mers[j] != 0 and j >=0:
            bin_mers[j] = 0
            j -=1
        bin_mers[j] = 1
        containers.append(bin_mers.copy())

    rally = []

    for lis in containers:
        rally.append(list_to_string(lis))

    return rally

def list_to_string(k_mers):
    rstr = ""
    for i in k_mers:
        if i==1:
            rstr += "1"
        else:
            rstr += "0"
    return rstr




def k_universal_cicular_string(k):

    k_binary_digits = binary_k_mers(k)
    debuijn_dict = DeBruijnGraph(k_binary_digits)

    #print(debuijn_dict)
    euler_cycle = []
    init_node = "0"*(k-1)
    euler_cycle.append(init_node)
    curr_node = init_node
    next_node = ""

    while next_node != init_node:
        index = random.randint(len(debuijn_dict[curr_node]))
        next_node = debuijn_dict[curr_node].pop(index)
        euler_cycle.append(next_node)
        if not debuijn_dict[curr_node]:
            debuijn_dict.pop(curr_node)
        curr_node = next_node

    while debuijn_dict:
        choice_nodes = euler_cycle.copy()
        index = random.randint(len(choice_nodes))
        curr_node = choice_nodes.pop(index)

        while not debuijn_dict.get(curr_node,[]) and len(choice_nodes)>0:
            index = random.randint(len(choice_nodes))
            curr_node = choice_nodes.pop(index)

        if len(choice_nodes) == 0:
            break

        insert_idx = index +1
        tmp_start = curr_node
        next_node = ""
        #print(curr_node)
        #print(debuijn_dict)
        while next_node != tmp_start:
            #print(next_node)
            #print(len(debuijn_dict[curr_node]))
            #print(debuijn_dict)
            index = random.randint(len(debuijn_dict[curr_node]))
            next_node = debuijn_dict[curr_node].pop(index)
            euler_cycle.insert(insert_idx,next_node)
            insert_idx +=1
            if not debuijn_dict[curr_node] :
                debuijn_dict.pop(curr_node)
            curr_node = next_node



    return PathToGenome(euler_cycle)[:-(k-1)]

def node_to_edge(seq):
    res = []
    for i in range(len(seq)-1):
        node1 = seq[i]
        node2 = seq[i+1]
        res.append(node1+node2[-1])
    return res
a = ["00","01","10","11"]
print(node_to_edge(a))
#print(binary_k_mers(15))
def Cicular_string(k):
    graph = binary_k_mers(k)
    graph = dict(DeBruijnGraph(graph))
    cycle_node = []
    node_start = "0"*(k-1)
    curr_node = node_start
    next_node = ""

    cycle_node.append(node_start)
    while next_node != node_start:
        next_node = graph[curr_node].pop(0)
        if not graph[curr_node]:
            graph.pop(curr_node)
        cycle_node.append(next_node)
        curr_node = next_node
    #print(cycle_node)

    #print(graph)
    while graph:

        choices = cycle_node.copy()
        tmp = choices[0]
        choices.pop(0)
        #print(graph)
        while not graph.get(tmp,[]) and len(choices) >0:
            tmp = choices[0]
            choices.pop(0)
        if len(choices) == 0:
            break
        node_start =tmp
        curr_node = node_start
        next_node = ""
        idx = cycle_node.index(node_start)+1

        while next_node != node_start:
            next_node = graph[curr_node].pop(0)
            cycle_node.insert(idx,next_node)
            idx+=1
            if not graph[curr_node]:
                graph.pop(curr_node)
            curr_node = next_node

        #print(cycle_node)
    cycle_edge = node_to_edge(cycle_node)
    #print(cycle_edge)
    idx = cycle_edge.index("0" * (k))
    cir_str = cycle_edge[idx]
    for i in range(2 ** k - k ):
        idx = (idx + 1) % (2 ** k)
        #print(idx)
        cir_str += cycle_edge[idx][-1]
    print(cir_str)


print(Cicular_string(8))