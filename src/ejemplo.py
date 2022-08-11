# Codigo ejemplo
from platform import architecture
import sys


#def voltajediv():

if __name__ == "__main__":
    #voltajediv()
    vi = float(sys.argv[1])
    r1 = float(sys.argv[2])
    r2 = float(sys.argv[3])

    vo = float((vi*r2)/(r1+r2))
    print(f'El voltaje de salida es {vo}')