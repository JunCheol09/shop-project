
a=20
def p(x):
    global a
    a=x
    return a
p(30)
print(a)