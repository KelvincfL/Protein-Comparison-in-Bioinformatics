from edit_distance_with_local_alignment import *
from proteins import *
from BLOSUM_matrix import *

result = v_sub(C, D, -2, -2, blosum)
print(result)