def hackerrankCity(A):
    modK = 1000000007
    t = 0
    y = 1
    p = 0
    d = 0

    for x in A:
        p = (4 * p + 12 * d * y + (16 * y * y + 12 * y + 1) * x) % modK
        d = (4 * d + 8 * y * x + 3 * y * t + 2 * t + 3 * x) % modK
        y = (4 * y + 2) % modK
        t = (2 * t + 3 * x) % modK

    return p


def nnew(n, mod):
    return (4*n+2)%mod
def jnew(j, A, mod):
    return (2*j+3*A)%mod
def xnew(x, A, n, j, mod):
    return (A+5*A*n+4*x+(3*n+2)*(j+A) )%mod
def sumnew(sm, A, n, x, mod):
    return ( 4*sm + (3*A*n+2*x)*4 + A + (2*n*(2*x+2*n*A) + 4*n*(2*x+3*n*A) ) )%mod
def hackerrankCity2(A):
    # Time complexity: O(N) ; N = len(A)
    # n is the number of nodes in the tree
    # j is the distance b/w left-topmost node and right-bottommost node
    # x is the sum of distances from right-bottommost node to all other nodes
    # sum is the sum of distances of all nodes from each other
    mod = 10**9+7
    N = len(A)
    j0 = x0 = sum0 = j1 = x1 = sum1 = 0
    n0 = n1 = 1
    for i in range(N):
        Ai = A[i]
        j1 = jnew(j0, Ai, mod)
        x1 = xnew(x0, Ai, n0, j0, mod)
        n1 = nnew(n0, mod)
        sum1 = sumnew(sum0, Ai, n0, x0, mod)
        j0=j1
        sum0=sum1
        n0=n1
        x0=x1
    return sum0
print(hackerrankCity2([2,1]))