
from collections import defaultdict
def Suffix(Pattern):
    return Pattern[1:]

def Prefix(Pattern):
    return Pattern[:-1]



def GSGraph(path_graph):

    dict_graph = defaultdict(list)
    for start in path_graph:
        for end in path_graph[start]:
            dict_graph[end[:-1]].append(end[1:])
    return dict_graph

def DeBrujinGraph(k,txt):

    path_graph = defaultdict(list)
    n = len(txt)

    path_graph[txt[:k]].append(txt[:k])
    for i in range(n-k):
        path_graph[txt[i:i+k]].append(txt[i+1:i+k+1])


    #print(path_graph)
    dict_graph = defaultdict(list)
    for start in path_graph:
        for end in path_graph[start]:
            #print(start)
            dict_graph[end[:-1]].append(end[1:])
            #print(dict_graph)
    return dict_graph


