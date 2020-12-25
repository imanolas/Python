import statistics as st

with open('inputdata.txt' , 'r') as fin:
    content = fin.read().splitlines()
    
x=[]

for inline in content:
    x.append(float(inline))
        
suma= round(st.mean(x),3)
sd=round(st.pstdev(x),3)

with open('outputdata.txt' , 'w') as fout:
    fout.write('Μέσος όρος= ' + str(suma) + '\n')
    fout.write('Τυπική απόκλιση= ' + str(sd))
    
