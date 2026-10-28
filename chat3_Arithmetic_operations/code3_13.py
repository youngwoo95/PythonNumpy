a, b = 10, -20

#print(dir(a))
print(f"{+a = } / {a.__pos__() = }")
print(f"{-a = } / {a.__neg__() = }")

print(f"{+b = } / {b.__pos__()}")
print(f"{-b = } / {b.__neg__()}")