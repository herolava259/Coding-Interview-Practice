from numpy import random
from collections import defaultdict
import re



def EulerianCycle(Graph_dict, isinit = False, n_start = 1, n_end = 2):


    n = len(Graph_dict)

    euler_cycle = []
    new_start = next_node = curr_node = -1

    if not isinit:
        new_start = random.randint(n)
        next_node = -1
        curr_node = new_start
        euler_cycle.append(curr_node)
    else:
        new_start = n_start
        euler_cycle.append(n_start)
        euler_cycle.append(n_end)
        if not Graph_dict[n_start]:
            Graph_dict.pop(n_start)
        next_node = -1
        curr_node = n_end
        #print("curr node",curr_node)

    #print(curr_node)
    while next_node != new_start:
        #print(curr_node)
        #print(len(Graph_dict[curr_node]))
        index = random.randint(len(Graph_dict[curr_node]))
        next_node = Graph_dict[curr_node].pop(index)
        euler_cycle.append(next_node)
        #print(next_node)
        if(not Graph_dict[curr_node]):
            #print(Graph_dict[curr_node])
            Graph_dict.pop(curr_node)
        curr_node = next_node

    #print(euler_cycle)

    while Graph_dict:
        #print("trong vong lap while")
        keys_choice = list(euler_cycle)
        index = random.randint(len(keys_choice))
        curr_node = keys_choice[index]

        while not Graph_dict.get(curr_node,[]) and  len(keys_choice) > 0:

            keys_choice.pop(index)
            index= random.randint(len(keys_choice))
            curr_node = keys_choice[index]

        if len(keys_choice) == 0:
            break
        tmp_start = curr_node
        next_node = -1
        insert_idx = euler_cycle.index(curr_node) +1
        while next_node != tmp_start:
            index = random.randint(len(Graph_dict[curr_node]))
            next_node = Graph_dict[curr_node].pop(index)
            euler_cycle.insert(insert_idx,next_node)
            insert_idx += 1
            if (not Graph_dict[curr_node]):
                Graph_dict.pop(curr_node)
            curr_node = next_node


    return euler_cycle

def RealEulerCycler(graph):

    graph_dict = defaultdict(list)
    for line in graph:
        if(not line):
            continue
        node_lis = re.findall("\d+",line)
        #print(node_lis)
        start = int(node_lis[0])
        for end in node_lis[1:]:
            graph_dict[start].append(int(end))

    euler_cycle = EulerianCycle(graph_dict)

    chain = str(euler_cycle[0])
    for i in euler_cycle[1:]:
        chain = chain + "->" + str(i)
    return chain


in_put = "0 -> 3\n1 -> 0\n2 -> 1,6\n3 -> 2\n4 -> 2\n5 -> 4\n6 -> 5,8\n7 -> 9\n8 -> 7\n9 -> 6".split("\n")
#print(in_put)
#print(RealEulerCycler(in_put))