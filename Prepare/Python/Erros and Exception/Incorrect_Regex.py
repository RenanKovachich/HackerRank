import re

def is_valid_regex(pattern):
    try:
        re.compile(pattern)
        if re.search(r'[*+?]{2,}', pattern):
            return False
        return True
    except re.error:
        return False

def main():
    t = int(input().strip())

    for _ in range(t):
        pattern = input().strip()

        print(is_valid_regex(pattern))

if __name__ == "__main__":
    main()
