from itertools import groupby

if __name__ == "__main__":
    for k, c in groupby(input()):
        print("(%d, %d)" % (len(list(c)), int(k)), end=' ')
