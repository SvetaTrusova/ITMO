import time
t_start = time.perf_counter()
with open('input 0.3') as f:
    n = int(f.readline())
if n == 0:
    with open('output 0.3', 'w') as f:
        f.write('0')
elif n == 1:
    with open('output 0.3', 'w') as f:
        f.write('1')
else:
    a = 0
    b = 1
    for i in range(n-1):
        a, b = b, a + b
    with open('output 0.3', 'w') as f:
        f.write(str(b % 10))
print(time.perf_counter() - t_start)



