
def pmat(s1,s2,mat):
    s1 = "-"+s1
    s2 = "-"+s2
    print(" ", *s2, sep = "  ")
    for x, L in zip(s1, mat):
        print(x, *[f"{y:2d}" for y in L])
    print()

def consensus(s1, s2):
    return ''.join(x1 if x1 == x2 else x1 if x2 == '-' else x2 for x1, x2 in zip(s1, s2))

def align(s1, s2):
    eq, df, sp = 4, -1, -4
    def score(x1, x2):
        return eq if x1 == x2 else df
    DIAG = 1
    LEFT = 2
    UP = 4

    mat = [[0 for C in range(len(s2) + 1)] for L in range(len(s1) + 1)]
    tr = [[0 for C in range(len(s2) + 1)] for L in range(len(s1) + 1)]
    for L in range(len(s1)):
        mat[L + 1][0] = mat[L][0] + sp
        tr[L + 1][0] = UP
    for C in range(len(s2)):
        mat[0][C + 1] = mat[0][C] + sp
        tr[0][C + 1] = LEFT

    for L, x1 in enumerate(s1):
        for C, x2 in enumerate(s2):
            poss = mat[L][C] + score(x1, x2), mat[L + 1][C] + sp, mat[L][C + 1] + sp
            mat[L + 1][C + 1] = max(*poss)
            tr[L + 1][C + 1] = sum(2 ** I for I, x in enumerate(poss) if x == max(poss))

    #pmat(s1, s2, mat)
    #pmat(s1, s2, tr)

    S1 = S2 = ""
    L = len(mat) - 1
    C = len(mat[0]) - 1
    while L > 0 or C > 0:
        delta = [(-1,-1), (0, -1), (-1, 0)]
        Diag = -1, -1
        Up = -1, 0
        Left = 0, -1

        if tr[L][C] & DIAG:
            DL, DC = Diag
            S1 = s1[L - 1] + S1
            S2 = s2[C - 1] + S2
        elif tr[L][C] & UP:
            DL, DC = Up
            S1 = s1[L - 1] + S1
            S2 = "-" + S2
        else:
            DL, DC = Left
            S1 = "-" + S1
            S2 = s2[C - 1] + S2
        L += DL
        C += DC
    return mat[-1][-1], S1, S2

def malign(seqs):
    s1, s2, *rest = seqs
    score, S1, S2 = align(s1, s2)
    cons = consensus(S1, S2)
    mal = [S1, S2]
    for s in rest:
        score, S1, S2 = align(cons, s)
        mal.append(S2)
        cons = consensus(S1, S2)

    for s in seqs:
        score, S, other = align(s, cons)
        print(S)

seqs = """ACTCAT
AGTCAT
ACGTCCT
"""
seqs = [s.strip() for s in seqs.splitlines()]

import sys
seqs = [s.strip() for s in sys.stdin.readlines()]
malign(seqs)
