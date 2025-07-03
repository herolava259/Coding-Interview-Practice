

def AdjacencyPattern(pat, lis_pat):

    result = []

    prefix = pat[1:]

    for p in lis_pat:
        if prefix == p[:-1]:
            result.append(p)

    return result

def OverlapGraph(col_pats):

    dict_adj = {}

    for pat in col_pats:
        adj_lis = AdjacencyPattern(pat, col_pats)

        strtmp = pat
        dict_adj[pat] = adj_lis

    return dict_adj

def OvetlapGraphStr(col_pats):

    dict_adj = OverlapGraph(col_pats)
    lis_adj = []
    for pat in col_pats:
        tmp_lis = dict_adj[pat]

        if len(tmp_lis) == 0:
            continue
        result = pat + " -> "
        for p in tmp_lis:
            result = result + p + ","

        lis_adj.append(result[:-1])
    return lis_adj


