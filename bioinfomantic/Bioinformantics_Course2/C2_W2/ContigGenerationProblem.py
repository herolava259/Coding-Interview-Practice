import re
from collections import defaultdict

def is_1in1out_node(node, graph):
    return len(graph[node][0]) == 1 and len(graph[node][1]) == 1



def isolated_cycles(graph):
    cycles = []
    for node in graph:
        if is_1in1out_node(node,graph):
            cycle = [node]

            next_node = graph[node][0][0]
            check_node = is_1in1out_node(next_node,graph)
            while next_node != node and check_node:
                cycle.append(next_node)
                next_node = graph[next_node][0].pop()
                check_node = is_1in1out_node(next_node,graph)
            if check_node:
                cycle.append(next_node)
                cycles.append(cycle)

    return cycles

def MaximalNonBranchingPaths(graph):

    """

    :param graph: type dict(key:str, values: tuple(list,list))
    :return: type list(str)
    """
    paths = []

    for node in graph:
        if not is_1in1out_node(node,graph) and len(graph[node][0]) > 0 :
            out_nodes = graph[node][0]
            for node2 in out_nodes:
                nbr_path = []
                nbr_path.append(node)
                curr_node = node2
                while is_1in1out_node(curr_node,graph):
                    nbr_path.append(curr_node)
                    curr_node = graph[curr_node][0][0]
                nbr_path.append(curr_node)
                paths.append(nbr_path)


    paths.extend(isolated_cycles(graph.copy()))

    return paths

def init_fn():
    return ([],[])

def convert_input(graph):
    out_put = defaultdict(init_fn)

    for line in graph:
        nodes = re.findall('\w+',line)
        out_node = nodes[0]
        in_node = nodes[1:]
        out_put[out_node][0].extend(in_node)

        for n in in_node:
            out_put[n][1].append(out_node)

    return out_put

def DeBruijnGraph(patterns):

    graph = defaultdict(init_fn)
    for pat in patterns:

        if not pat:
            continue

        out_node = pat[:-1]
        in_node = pat[1:]
        graph[out_node][0].append(in_node)
        graph[in_node][1].append(out_node)
    return graph



def convert_data(in_put):
    out_put = ""
    for line in in_put:
        out_put += line[0]
        for n in line[1:]:
            out_put += " -> " + n

        out_put += "\n"

    return out_put

def convert_sequence(set_path):
    out_put = ""
    for path in set_path:
        seq = path[0]
        for node in path[1:]:
            seq += node[-1]
        out_put += seq
        out_put += "\n"

    return out_put

in_put = "1 -> 2\n2 -> 3\n3 -> 4,5\n6 -> 7\n7 -> 6".split("\n")
with open("C://Users\Admin\Desktop\dataset_205_5.txt",'r') as file:
    in_put = file.read()

in_put = in_put.split("\n")
#print(in_put)
in_put = dict(DeBruijnGraph(in_put))
#print(in_put)

print(convert_sequence(MaximalNonBranchingPaths(in_put)))




