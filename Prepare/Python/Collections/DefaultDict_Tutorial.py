from collections import defaultdict

if __name__ == "__main__":
    n, m = map(int, input().split())
    d = defaultdict(list)

    for i in range(1, n + 1):
        word = input()
        d[word].append(i)

    for _ in range(m):
        query = input()
        print(" ".join(map(str, d[query])) or -1)
