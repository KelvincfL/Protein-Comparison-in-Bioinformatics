# S, T are the two strings to be compared
# weight=w(l)=u
def edit_distance_without_transcript(S, T, weight, scoring):
    m = len(S)  # length of S
    n = len(T)  # length of T
    # initialising the results table
    Vgap = [[[0, ''] for i in range(n+1)] for i in range(m+1)]
    E = [[0 for i in range(n+1)] for i in range(m+1)]
    F = [[0 for i in range(n+1)] for i in range(m+1)]
    # boundary conditions
    for i in range(m+1):
        Vgap[i][0][0] = weight
        Vgap[i][0][1] = 'D'
        E[i][0] = weight    # so E(i,1)=Vgap(i,0)+u
    for j in range(n+1):
        Vgap[0][j][0] = weight
        Vgap[0][j][1] = 'I'
        F[0][j] = weight   # so F(1,j)=Vgap(0,j)+u
    Vgap[0][0][0] = 0
    Vgap[0][0][1] = 'M'
    # recursion calculation
    for i in range(1, m+1):
        for j in range(1, n+1):
            # recursive formula to calculate E[i][j] and F[i][j]
            E[i][j] = max(E[i][j-1], Vgap[i][j-1][0]+weight)
            F[i][j] = max(F[i-1][j], Vgap[i-1][j][0]+weight)
            # calculate G[i][j]
            G = Vgap[i-1][j-1][0] + scoring[(S[i-1], T[j-1])]
            Vgap[i][j][0] = max(E[i][j], F[i][j], G)
            if Vgap[i][j][0] == G:      # G is replacement or matching
                if S[i-1] == T[j-1]:
                    Vgap[i][j][1] = 'M'
                else:
                    Vgap[i][j][1] = 'R'
            elif Vgap[i][j][0] == E[i][j]:
                Vgap[i][j][1] = 'I'     # E is insertion
            else:
                Vgap[i][j][1] = 'D'     # F is deletion
    return Vgap


def backtrace(S, T, weight, scoring):
    Vgap = edit_distance_without_transcript(S, T, weight, scoring)
    # backtracing for optimal route
    m = len(S)
    n = len(T)
    i, j = m, n
    string = ''
    # we iterate until both strings have length zero, at each index we use the pointer
    # to determine which operation was taken, and backtrace accordingly
    while i >= 0 or j >= 0:
        string += Vgap[i][j][1]
        # replace or matching
        if Vgap[i][j][1] == 'R' or Vgap[i][j][1] == 'M':
            i -= 1
            j -= 1
        # insert
        elif Vgap[i][j][1] == 'I':
            j -= 1
        # delete
        else:
            i -= 1
    return string[::-1]