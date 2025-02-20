print('Введите число жителей:')
n = int(input())
print("Введите число связей:")
chain_number = int(input())
trust = []
for i in range(chain_number):
    numbers = input(f'Введите два числа, разделенные пробелом для {i+1} связи:').split()
    trust.append([int(numbers[0]), int(numbers[1])])
print(trust)
        
for i in range (n):
    c=1
    for a,b in trust:
        if a !=i+1 and b==i+1:
            c*=1
        else: c*=0
    if c==1: print(f'Судья - номер {i+1}')

print('Введите число жителей:')
n = int(input())
print("Введите число связей:")
chain_number = int(input())
trust = []
for i in range(chain_number):
    numbers = input(f'Введите два числа, разделенные пробелом для {i+1} связи:').split()
    trust.append([int(numbers[0]), int(numbers[1])])
print(trust)
        
for i in range (n):
    c=1
    for a,b in trust:
        if a !=i+1 and b==i+1:
            c*=1
        else: c*=0
    if c==1: print(f'Судья - номер {i+1}')
if c==0: print('-1')