def fibunacci_list(n):
    fib =[]
    a,b=0,1
    for i in range (n):
        fib .append(a)
        a,b=b,b+a
    return fib
print(fibunacci_list(10))
