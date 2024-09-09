with open('input 0.1.4') as f:
    a, b = f.readline(). split()
    a = int(a)
    b = int(b)
with open('output 0.1.4', 'w') as f:
    f.write(str(a + b**2))



