import re

d = {'A' :'00','C' : '10','G':'01','T': '11'}

patterns = ['GAGTGAGGGATCGAGGGAATGGACGGCGGGAAGGGAGATTGAGTGGACGAAGGGAAGACAGGCG']

for p in patterns:
    for c in p:
        p = re.sub(c,d[c],p)
    
    print(p)
    