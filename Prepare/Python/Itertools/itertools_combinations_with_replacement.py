from itertools import combinations_with_replacement

def solve():
    string, number = map(str, input().split())
    number = int(number)
    
    lista = list(combinations_with_replacement(sorted(string), number))
    
    for combination in lista:
        print("".join(combination))
    
if __name__ == "__main__":
    solve()
