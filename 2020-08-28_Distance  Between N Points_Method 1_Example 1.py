import math
#Comentario:
##N_p, N_a,Nb, E_p,E_a,E_b) Coordenadas en metros
##pow = power = elevado a la potencia, ejemplo:  x^0.5 = pow(x,0.5)
## 1 pi = 180 degrees = 57.2956  : Conversion Factor

def CalculateDistance(N_p, N_a,N_b, E_p,E_a,E_b):

    return round(math.sqrt((N_p - N_a)**2 + ( E_p -E_a)**2),4)

AP= CalculateDistance(2055.55,2000,2077.869,1160.245,1020, 1078.331)
print(AP)
