#program to find the largest word in a file
a=input("Enter file name:")
f=open(a,'r')
x=f.read()
x=x.strip('\n').split()
z=[]
y=[]
g=[]
h=''
for i in x:
    z.append(len(i))
b=max(z)
d=z.count(b)
if d==1:
    c=z.index(b)
    print("The longest word is:",x[c])
if d>1:
    for i in range(d):
        c=z.index(b)
        y.append(c+i)
        z.remove(b)
    for i in y:
        g.append(x[i])
    for i in g:
        h=h+i+' '
    print("The longest words are:",h)
