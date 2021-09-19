# S, T are the two strings to be compared
# deletion is s(Si,-)
# insertion is s(-,Tj)
def v_sub(S, T, insertion, deletion, replacement):
    m = len(S)  # length of S
    n = len(T)  # length of T
    # initialising the results table
    Vsfx = [[0 for i in range(n+1)] for i in range(m+1)]
    maximum_score = 0
    # boundary conditions
    for i in range(m+1):
        Vsfx[i][0] = 0
    for j in range(n+1):
        Vsfx[0][j] = 0
    # recursion calculation
    for i in range(1, m+1):
        for j in range(1, n+1):
            Vsfx[i][j] = max(0, Vsfx[i][j-1]+deletion, Vsfx[i-1][j]+insertion,
                             Vsfx[i-1][j-1]+replacement[(S[i-1], T[j-1])])
            # update the maximum score if required
            if Vsfx[i][j] > maximum_score:
                maximum_score = Vsfx[i][j]
    return maximum_score
