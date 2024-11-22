from contextlib import suppress, redirect_stdout


L = [ (1,2), (3,4), (5,6), (6,7), (5,0), (67,34), (3,2) ]

with suppress(ZeroDivisionError):
    for a, b in L:
        print(a/b)
        

with open('nums.txt', 'wt', encoding='utf-8') as trg:
    with redirect_stdout(trg):
        for a, b in L:
            print(a, b)
