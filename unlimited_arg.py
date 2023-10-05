def add(*args):
    s=0
    for n in args:
        s=s+n
    return s

a=add(3,2,5,5)
print(a)