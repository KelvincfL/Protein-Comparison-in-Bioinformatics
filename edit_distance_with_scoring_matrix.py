# S, T are the two strings to be compared
def edit_distance_without_transcript(S, T, insertion, deletion, replacement):
    m = len(S)  # length of S
    n = len(T)  #length of T
    # initialising the results table
    D = [[[0, ''] for i in range(n+1)] for i in range(m+1)]
    # boundary conditions
    for i in range(m+1):
        D[i][0][0] = i * deletion
        D[i][0][1] = 'D'
    for j in range(n+1):
        D[0][j][0] = j * insertion
        D[0][j][1] = 'I'
    D[0][0][0] = 0
    D[0][0][1] = 'M'
    # recursion calculation
    for i in range(0, m):
        for j in range(0, n):
            D[i+1][j+1][0] = max(D[i][j+1][0]+deletion,
                                 D[i+1][j][0]+insertion, D[i][j][0]+replacement[(S[i], T[j])])
            if D[i+1][j+1][0] == D[i][j+1][0]+deletion:
                D[i+1][j+1][1] = 'D'
            elif D[i+1][j+1][0] == D[i+1][j][0]+insertion:
                D[i + 1][j + 1][1] = 'I'
            else:
                if S[i] == T[j]:
                    D[i + 1][j + 1][1] = 'M'
                else:
                    D[i + 1][j + 1][1] = 'R'

    return D


def backtrace(S, T, insertion, deletion, replacement):
    D = edit_distance_without_transcript(S, T,insertion, deletion, replacement)
    # backtracing for optimal route
    m = len(S)
    n = len(T)
    i, j = m, n
    string = ''
    # we iterate until both strings have length zero, at each index we use the pointer
    # to determine which operation was taken, and backtrace accordingly
    while i > 0 or j > 0:
        string += D[i][j][1]
        # replace or matching
        if D[i][j][1] == 'R' or D[i][j][1] == 'M':
            i -= 1
            j -= 1
        # insert
        elif D[i][j][1] == 'I':
            j -= 1
        # delete
        else:
            i -= 1
    return string[::-1]