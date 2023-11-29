def can_pile_up(blocks):
    left = 0
    right = len(blocks) - 1
    left_pile = float('inf')
    right_pile = float('inf')

    while left <= right:
        atual = max(blocks[left], blocks[right])

        if atual <= left_pile and atual <= right_pile:
            if left_pile <= right_pile:
                left_pile = atual
                left += 1
            else:
                right_pile = atual
                right -= 1
        else:
            return "No"

    return "Yes"

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        blocks = [int(z) for z in input().split()]
        
        result = can_pile_up(blocks)
        print(result)
