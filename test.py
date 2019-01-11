n = 2543

a = n//1000
b = (n - 1000 * a)//100
c = (n - 1000 * a - 100 * b)//10
d = n - 1000 * a - 100 * b - 10 * c

print(a), print(b), print(c), print(d)