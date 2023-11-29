def merge_the_tools(string, k):
    substrings = [string[i:i+k] for i in range(0, len(string), k)]
    for substring in substrings:
        unique_chars = set()
        new_substring = ""

        for char in substring:
            if char not in unique_chars:
                new_substring += char
                unique_chars.add(char)

        print(new_substring)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
