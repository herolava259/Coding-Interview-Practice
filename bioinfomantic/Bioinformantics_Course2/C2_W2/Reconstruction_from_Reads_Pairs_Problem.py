import re
from collections import defaultdict
from numpy import random

def convert_to_tuple(pairs):
    res = []
    for line in pairs:
        res.append(tuple(re.findall("\w+",line)))

    return res

def DeBruijnGraph(pairs):
    res_from = defaultdict(list)
    res_to = defaultdict(list)
    edges = set()

    for pair in pairs:
        edge1 = (pair[0][:-1],pair[1][:-1])
        edge2 = (pair[0][1:],pair[1][1:])
        res_from[edge1].append(edge2)
        res_to[edge2].append(edge1)
        edges.add(edge1)
        edges.add(edge2)


    return res_from,res_to,edges

def EulerCycle(graph, node_start, node_end):

    eulercycle = []


    eulercycle.append(node_start)

    eulercycle.append(node_end)
    curr_node = node_end
    next_node = ()

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

def StringSpelledByGapped(GappedPatterns,k):
    spelled_str = GappedPatterns[0]

    for pat in GappedPatterns[1:]:
        spelled_str += pat[-1]

    return spelled_str

def StringSpelledByGappedPatterns(gapped_patterns,k,d):

    first_patterns = []
    second_patterns = []

    for pair in gapped_patterns:
        first_patterns.append(pair[0])
        second_patterns.append(pair[1])
    prefix_str = StringSpelledByGapped(first_patterns,k)
    suffix_str = StringSpelledByGapped(second_patterns,k)

    for i in range(k+d+1,len(prefix_str)):
        if prefix_str[i] != suffix_str[i-k-d]:
            return None

    #prefix_str += suffix_str[-k-d:]
    return prefix_str  + suffix_str[-k-d:]

def start_and_end(from_graph, to_graph, nodes):
    graph_to = to_graph.copy()
    graph_from = from_graph.copy()

    pair_from = ()
    pair_to = ()

    for n in nodes:
        if len(graph_from[n]) < len(graph_to[n]):
            pair_from = n
        if len(graph_from[n]) > len(graph_to[n]):
            pair_to = n
    return pair_from, pair_to


def ReFromReadPairs(k,d, read_pairs):

    read_pairs = convert_to_tuple(read_pairs)
    graph_from, graph_to,nodes = DeBruijnGraph(read_pairs)
    graph = dict(graph_from.copy())
    pair_from , pair_to = start_and_end(graph_from,graph_to,nodes)

    path = EulerCycle(graph,pair_from,pair_to)
    check_str = StringSpelledByGappedPatterns(path,k,d)

    while not check_str:
        path = EulerCycle(graph,pair_from,pair_to)
        check_str = StringSpelledByGappedPatterns(path,k,d)

    print(check_str)




read_pairs = "GAGA|TTGA TCGT|GATG CGTG|ATGT TGGT|TGAG GTGA|TGTT GTGG|GTGA TGAG|GTTG GGTC|GAGA GTCG|AGAT".split()


#p1,p2,p3 = DeBruijnGraph(convert_to_tuple(read_pairs))
#print(start_and_end(p1,p2,p3))

#print(convert_to_tuple(read_pairs))
#print(DeBruijnGraph(convert_to_tuple(read_pairs)))
#ReFromReadPairs(4,2,read_pairs)