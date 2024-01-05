from itertools import combinations

def solve_combinations():
    string, number = map(str, input().split())
    max_number = int(number)
    
    for number in range(1, max_number + 1):
        lista = list(combinations(sorted(string), number))
        
        for combination in lista:
            print("".join(combination))
    
if __name__ == "__main__":
    solve_combinations()
