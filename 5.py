s = input()
g = s[0]
s=s[1:]
n = ""
for i in range(0,len(s),int(g)):
    n = n+s[i+int(g):i:-1]
print(n)
