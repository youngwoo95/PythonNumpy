from numpy.random import randint

u = randint(1, 6, 4)
v = randint(1, 6, 4)

print(u)
print(v)

#print(dir(u))
print(f"{u + v =} / {u.__add__(v) =}")
print(f"{u - v =} / {u.__sub__(v) =}")
print(f"{u * v =} / {u.__mul__(v) =}")
print(f"{u ** v =} / {u.__pow__(v) =}")
print(f"{u / v =} / {u.__truediv__(v) =}")
print(f"{u // v =} / {u.__floordiv__(v ) =}")
print(f"{u % v =} / {u.__mod__(v) =}")