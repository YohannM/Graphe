import numpy as np

def createMatrix():
    t=0
    c=0

    fo=open("./Louis/graphex.txt","r")
   

    file=fo.readlines()
    for line in file :
        #print(line)
        t=t+1

    matrix=np.zeros(shape=(t,t),dtype=int)
    
    
    for line in file :
        c=0
        while line[c] != ';' and c<len(line)-2:
            c=c+1
            if line[c+1]=='.' :
                i1=int(line[0])
                i2=int(line[c])
                val=int(line[c+2])
                matrix[i1][i2]=val
    #print(matrix)

            
    return matrix
    fo.close()

createMatrix()

