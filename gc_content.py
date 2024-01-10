

#script to get the length of fasta and also calculate the gc content
import os
# Getting the current work directory (cwd)
thisdir = os.getcwd()
import pandas as pd


result=[]
for r, d, f in os.walk(thisdir):
    for file in f:
        if file.endswith("fasta"):
            count = 0; total_gc = 0
            name = ''; mem = True; id_line = ''
            for line in open(file, 'r'):
                
                if line.startswith('>'):
                    if mem:
                        id_line = line.strip()
                        id_line = id_line.split()[0][1:] # gets the header without the > symbol
                        mem = False
                else:
                    seq = line.strip()
                    #print(seq)
                    num = len(seq)
                    count += num
                    G = seq.count("G")
                    C = seq.count("C")
                    GC = G + C
                    total_gc += GC
            #print(count, total_gc)
            gc = round(total_gc/count*100, 2)
           #print(gc)
            res = id_line, name, gc
            result.append(res)
df = pd.DataFrame(result, columns=['file', 'name', 'gc'])
print(df)

df.to_csv('seq_gc.csv')                      
xxx                              

































                                    
                                    
                    
