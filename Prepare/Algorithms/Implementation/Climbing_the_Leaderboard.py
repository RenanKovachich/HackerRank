#!/bin/python3

import math
import os
import random
import re
import sys


def climbingLeaderboard(ranked, player):
    scores = list(set(ranked)) #Tirar os numeros duplicados
    scores.sort(reverse=True) #Inverter
    rank = len(scores)
    results_new = []

    for score in player:
        while rank > 0 and score >= scores[rank - 1]:
            rank -= 1
        results_new.append(rank + 1)

    return results_new
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
