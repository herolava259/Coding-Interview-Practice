#from C2_W2.EulerCycle import EulerianCycle
from collections import defaultdict
import re
from numpy import random


def EulerCycle(graph, node_start, node_end):

    eulercycle = []


    eulercycle.append(node_start)

    eulercycle.append(node_end)
    if not graph[node_start]:
        graph.pop(node_start)
    curr_node = node_end
    next_node = -1

    while next_node != node_start:
        index = random.randint(len(graph[curr_node]))
        next_node = graph[curr_node].pop(index)
        eulercycle.append(next_node)
        if not graph[curr_node]:
            graph.pop(curr_node)

        curr_node = next_node

    #print(eulercycle)
    eulercycle = eulercycle[1:]
    #print(eulercycle)
    while graph:
        keys_choice = eulercycle.copy()
        index = random.randint(len(keys_choice))
        curr_node = keys_choice[index]
        #print(graph)
        while not graph.get(curr_node,[]) and len(keys_choice) >0:

            #print(keys_choice)
            keys_choice.pop(index)
            #print(keys_choice)
            index = random.randint(len(keys_choice))
            curr_node = keys_choice[index]
        if len(keys_choice) == 0:
            break

        tmp_start = curr_node
        next_node = ""
        insert_idx = eulercycle.index(curr_node)+1

        while next_node != tmp_start:
            index = random.randint(len(graph[curr_node]))
            next_node = graph[curr_node].pop(index)
            eulercycle.insert(insert_idx,next_node)
            insert_idx +=1
            if not graph[curr_node]:
                graph.pop(curr_node)
            curr_node = next_node

    #print(eulercycle)
    return eulercycle

def EulerianPath(rawGraph):
    from_graph = defaultdict(list)
    to_graph = defaultdict(list)
    set_nodes = set()

    for line in rawGraph:

        if not line:
            continue

        nodes = re.findall("\w+", line)
        node_from = nodes[0]
        set_nodes.add(nodes[0])
        nodes_to = nodes[1:]
        for n in nodes_to:
            set_nodes.add(n)
            from_graph[node_from].append(n)
            to_graph[n].append(node_from)

    #print(from_graph)
    #print(to_graph)

    from_odd_node = to_odd_node = -1
    for n in set_nodes:
        len_from = len(from_graph[n])
        len_to = len(to_graph[n])

        if len_from < len_to:
            from_odd_node = n
            #print(from_odd_node)
        elif len_from > len_to:
            to_odd_node = n
            #print(to_odd_node)

    euler_cycle = EulerCycle(dict(from_graph), node_start=from_odd_node,node_end=to_odd_node)
    raw_path = euler_cycle

    euler_path = raw_path[0]

    for n in raw_path[1:]:
        euler_path = euler_path + "->" + n

    return raw_path,euler_path


def graph_to_raw(graph):

    raw_graph = []

    for node in graph:
        for enode in graph[node]:
            raw_graph.append(node + " -> " + enode)


    return raw_graph




in_put = "0 -> 2\n1 -> 3\n2 -> 1\n3 -> 0,4\n6 -> 3,7\n7 -> 8\n8 -> 9\n9 -> 6".split("\n")
#print(EulerianPath(in_put))


