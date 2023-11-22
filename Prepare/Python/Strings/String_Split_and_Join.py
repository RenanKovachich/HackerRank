def split_and_join(line):
    result = line.replace(" ", "-")
    return result

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
