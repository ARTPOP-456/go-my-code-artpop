f =open("texte.txt",'r',encoding = 'utf-8')
for l in f:
    print(l)
def nth_line_reader(f,n):
    for i in range (n):
        print(f.readline())

def lastnth_lines(f,n):
    lines=f.readlines()
    last_lines = lines[-n-1:]
    for i in last_lines:
        a=i.replace('n/','')
        print(a)
def nb_lines(f):
    b=[]
    a=0
    for i in f:
        b=b+i.split()
    for i in b:
        a=a+1
    print(a)

    

