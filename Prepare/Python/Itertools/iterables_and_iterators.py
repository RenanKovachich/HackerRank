from itertools import combinations

def solve():
    n = int(input())
    english_letters = list(input().split())
    k = int(input())
    
    a_count = english_letters.count('a')

    total_combinations = len(list(combinations(range(n), k)))

    combinations_with_a = 0
    for combo in combinations(range(n), k):
        if any(english_letters[i] == 'a' for i in combo):
            combinations_with_a += 1

    probability = combinations_with_a / total_combinations

    print("{}".format(probability))

if __name__ == "__main__":
    solve()
