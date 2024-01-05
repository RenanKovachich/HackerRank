from itertools import product

def multiplication(a, b):
    lista = list(product(a, b))
    
    for i in range(len(lista)):
        print(lista[i], end=" ")

a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

if __name__ == "__main__":
    multiplication(a, b)
