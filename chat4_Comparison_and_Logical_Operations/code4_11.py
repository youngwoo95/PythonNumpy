A = [False, True]
B = [False, True]

print("XOR Gate:")
print(f'{'A':^10} {'B':^10} | {'Y':^10}')
print('-'*34)
for a in A:
    for b in B:
        print(f"{str(a):^10} {str(b):^10} | {str(a ^ b):^10}")


print("OR Gate:")
print(f'{'A':^10} {'B':^10} | {'Y':^10}')
print('-'*34)
for a in A:
    for b in B:
        print(f"{str(a):^10} {str(b):^10} | {str(a | b):^10}")


print("AND Gate:")
print(f'{'A':^10} {'B':^10} | {'Y':^10}')
print('-'*34)
for a in A:
    for b in B:
        print(f"{str(a):^10} {str(b):^10} | {str(a & b):^10}")

        
'''
print("NOT Gate:")
print(f"{'A':^10} | {'Y':^10}")
print('-'*23)
for a in A:
    print(f"{str(a):^10} | {str(not(a)^10)}\n")
'''    