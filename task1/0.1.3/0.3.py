with open('input 0.3') as f:
    a, b = f.readline().split()
    a = int(a)
    b = int(b)
with open('output 0.3', 'w') as f:
    f.write(str(a + b))
    
