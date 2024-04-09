def calculaDelta(A,B,C):
    delta = B**2 -4*A*C
    return delta

import math
A,B,C = map(float, input().split())
if A == 0:
    print("Impossivel calcular")
else:
    delta = calculaDelta(A, B, C)
    
    if delta < 0:
        print("Impossivel calcular")
    elif delta == 0:
        R1 = (-B + math.sqrt(delta))/(2*A)
        print("R1 = {:.5f}".format(R1))
    elif delta > 0:
        R1 = (-B + math.sqrt(delta))/(2*A)
        R2 = (-B - math.sqrt(delta))/(2*A)
        print("R1 = {:.5f}".format(R1))
        print("R2 = {:.5f}".format(R2))