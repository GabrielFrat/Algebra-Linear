import numpy as np

# Conversão de listas para vetores (arrays)
u = [2, -4, 1]
print(type(u))

u = np.array(u)
print(u)
print(type(u))

print(u.shape)

v = np.array([3, 2, -5])
print(v[0])

# Soma de vetores
soma = u + v
print(soma)

# Produto interno do vetor
prod_int = 0
for i in range(len(u)):
    prod_int = prod_int + (u[i] * v[i])
    i = i + 1

print(prod_int)

# Multiplicação de vetor po escalar
mul1 = 5 * u
print(mul1)

mul2 = 5 * v
print(mul2)

# Distancia entre vetores
