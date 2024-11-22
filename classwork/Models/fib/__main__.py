from Fibonacci import Fibonacci
from gold_ratio import gold_ratio

#fb = Fibonacci(1, 1)
#it = iter(fb)
#for n, x in zip(range(0,10), it):
#    print(x)
    
#print('Ура!!!!!')

#for n, x in zip(range(0,15), it):
#    print(x)


for phi in gold_ratio(eps=1e-6):
    print(phi)
