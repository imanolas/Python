s = input("Γράψτε την λέξη: ")

if len(s) == 1:
    print("Μήκος = 1")
elif s == s[::-1]:
    adict={s:len(s)}
    alist=[]
    for s in s:
            alist.append(s[0:])
    print(adict)
    print(alist)
else:
    print("Δεν είναι παλίνδρομο")
