Import statistics as stats

def squares(alist):
    
    for i in alist:
        diff = (i-stats.mean(alist))**2
        
        yield diff


alist = []
while True:
    number = input('Δώστε αριθμό εάν θέλετε να συνεχίσετε: ')
    if number.isdecimal():
        alist.append(int(num))
    else:
        break
for j in squares(alist):
    print(j)