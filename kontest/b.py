n = int(input())
g=[]
def f(n):
    m=0
    if n%3==0:
        if n>1: 
            m=1+f(n/3)
#            g.append([n])
    elif n%2 == 0:
        if n>1: 
            m=1+f(n/2)
#            g.append([n])
    else:
        if n>1: 
            m=1+f(n-1)
#            g.append([n])
    return m
'''g.append([1])
g.reverse()'''
print(f(n))
#print(g)
#заполнеине массива как в 1 задаче
#добавляем к минимуму единицу