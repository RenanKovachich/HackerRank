if __name__ == "__main__":
    types_of_shoes = int(input())
    numbers_of_shoes = list(map(int, input().split()))
    total_to_pay = 0
    
    customers = int(input())
    for j in range(customers):
        number, price = map(int, input().split())
        if number in numbers_of_shoes:
            total_to_pay += price
            numbers_of_shoes.remove(number)
        else:
            continue

    print(total_to_pay)
