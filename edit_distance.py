# S, T are the two strings to be compared
def edit_distance_without_transcript(S, T):
    m = len(S)  # length of S
    n = len(T)  #length of T
    # initialising the results table
    D = [[0 for i in range(n+1)] for i in range(m+1)]
    # boundary conditions
    for i in range(m+1):
        D[i][0] = i
    for j in range(n+1):
        D[0][j] = j
    # recursion calculation
    for i in range(0, m):
        for j in range(0, n):
            if S[i] == T[j]:
                D[i+1][j+1] = D[i][j]
            else:
                D[i+1][j+1] = min(D[i][j+1]+1, D[i+1][j]+1, D[i][j]+1)
    return D


def backtrace(S, T):
    D = edit_distance_without_transcript(S, T)
    # backtracing for optimal route
    m = len(S)
    n = len(T)
    i, j = m,n
    string = ''
    while i > 0 or j > 0:
        if i and j and S[i] == T[j]:
            i -= 1
            j -= 1
            string += 'M'
        else:
            # replace
            if i and j and D[i][j] == 1 + D[i-1][j-1]:
                i -= 1
                j -= 1
                string += 'R'
            # deletion
            elif i and D[i][j] == 1 + D[i-1][j]:
                i -= 1
                string += 'D'
            # insertion
            elif j and D[i][j] == 1 + D[i][j-1]:
                j -= 1
                string += 'I'

    return string[::-1]