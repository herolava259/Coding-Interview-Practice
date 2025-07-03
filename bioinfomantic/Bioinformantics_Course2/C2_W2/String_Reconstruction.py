from C2_W1.DeBruijnGraph_with_k_mers_problem import DeBruijnGraph
from C2_W1.StringSpelled_by_a_GAT import PathToGenome
from C2_W2.Eulerian_Path_Problem import EulerianPath
from C2_W2.Eulerian_Path_Problem import graph_to_raw

def StringReconstruction(k,patterns):

    graph = DeBruijnGraph(patterns)
    euler_path,_ = EulerianPath(graph_to_raw(graph))
    return PathToGenome(euler_path)

in_put = "CTTA\nACCA\nTACC\nGGCT\nGCTT\nTTAC".split()

print(StringReconstruction(4,in_put))
