def fibonacci_sequence(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b

n = int(input("enter number:"))
fib_sequence = fibonacci_sequence(n)
for num in fib_sequence:
    print(num)

"""
output:-  enter number: 100
0
1
1
2
3
5
8
13
21
34
55
89
"""
