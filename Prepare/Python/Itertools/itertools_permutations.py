from itertools import permutations

def solve_permutation(word, number):
    lista = list(permutations(word, number))
    
    for i in range(len(lista)):
        print("".join(lista[i]))

word_and_number = [str(x) for x in input().split()]
word = sorted(word_and_number[0])
number = int(word_and_number[-1])

if __name__ == "__main__":
    solve_permutation(word, number)
