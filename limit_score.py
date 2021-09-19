import random
from edit_distance_with_gaps import *

m = 1000
p = 0.5
u = -3
n = 10000
U_n = ['' for i in range(m)]
V_n = ['' for i in range(m)]
Vgap = [0 for i in range(m)]
s = {('a', 'b'): -1, ('a', 'a'): 1, ('b', 'a'): -1, ('b', 'b'): 1}

for i in range(m):
    for j in range(n):
        if random.random() < p:
            U_n[i] += 'a'
        else:
            U_n[i] += 'b'
        if random.random() < p:
            V_n[i] += 'a'
        else:
            V_n[i] += 'b'
    Vgap[i] = edit_distance_without_transcript(U_n[i], V_n[i], u, s)[-1][-1][0]
estimated_mean = sum(Vgap)/m
result = estimated_mean/n

print(result)
