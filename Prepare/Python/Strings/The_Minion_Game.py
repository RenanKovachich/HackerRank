def minion_game(string):
    vowls = 'AEIOU'
    stuart_points, kevin_points = 0, 0
    
    for i in range(len(string)):
        if string[i] in vowls:
            kevin_points += len(string) - i
        else:
            stuart_points += len(string) - i
    
    if stuart_points > kevin_points:
        print('Stuart {}'.format(stuart_points))
    elif kevin_points > stuart_points:
        print("Kevin {}".format(kevin_points))
    else:
        print("Draw")
        
if __name__ == '__main__':
    s = input()
    minion_game(s)
