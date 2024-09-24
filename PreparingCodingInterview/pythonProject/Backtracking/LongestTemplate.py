def solution(AA, AB, BB):
    # Implement your solution here
    aa_temp = 'AA'
    ab_temp = 'AB'
    bb_temp = 'BB'

    max_str = ''

    def backtrack(n_aa: int, n_ab: int, n_bb: int, candidate: str):
        nonlocal max_str
        if len(max_str) < len(candidate):
            max_str = candidate

        if not candidate:
            if n_aa > 0:
                backtrack(n_aa-1, n_ab, n_bb, aa_temp)
            if n_ab > 0:
                backtrack(n_aa, n_ab-1, n_bb, ab_temp)
            if n_bb > 0:
                backtrack(n_aa, n_ab, n_bb-1, bb_temp)

        last_c = candidate[-2:]

        if last_c == aa_temp:
            if n_bb > 0:
                backtrack(n_aa, n_ab, n_bb-1, candidate + bb_temp)
        elif last_c == ab_temp:
            if n_ab > 0:
                backtrack(n_aa, n_ab-1, n_bb, candidate + ab_temp)
            if n_aa > 0:
                backtrack(n_aa-1, n_ab, n_bb, candidate + aa_temp)
        elif last_c == bb_temp:
            if n_aa > 0:
                backtrack(n_aa-1, n_ab, n_bb, candidate + aa_temp)
            if n_ab > 0:
                backtrack(n_aa, n_ab-1, n_bb, candidate + ab_temp)

    backtrack(AA, AB, BB, '')

    return max_str