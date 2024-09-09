with open('input 0.2') as f:
    n = int(f.readline())
if n == 0:
    with open('output 0.2', 'w') as f:
        f.write('0')
elif n == 1:
    with open('output 0.2', 'w') as f:
        f.write('1')
else:
    a = 0
    b = 1
    for i in range(n-1):
        a, b = b, a + b
    with open('output 0.2', 'w') as f:
        f.write(str(b))




