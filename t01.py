
a = 'HackerRank' 
b = 'Monday'
def mergeStrings(a, b):
    a_l = len(a)
    b_l = len(b)

    #print(a_l)
    #print(b_l)

    if a_l >= b_l:
        iter = a_l
        iter_s = b_l
    else:
        iter = b_l
        iter_s = a_l
        
    outstr =''
       
    for i in range(iter):
        #print(a[i])
        if i < iter_s:
            outstr = outstr+a[i]+b[i]
        else:
            if a_l >= b_l:
                outstr = outstr+a[i]
            else:
                outstr = outstr+b[i]
    return(outstr)
print(mergeStrings(a,b))

print(mergeStrings(b,a))