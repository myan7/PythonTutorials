import random

wins_A = 0
wins_B = 0

for i in range(0,10_000):
    ## votes for A and B changed every time
    ## these variables should be local variables
    ## and reset for each simulation
    votes_A = 0
    votes_B = 0
    # reginon 1
    if(random.random() <= 0.87):
        votes_A += 1
    else:
        votes_B += 1
    # region 2
    if(random.random() <= 0.65):
        votes_A += 1
    else:
        votes_B += 1
    # region 3
    if(random.random() <= 0.17):
        votes_A += 1
    else:
        votes_B += 1

    if votes_A > votes_B:
        wins_A += 1
    elif votes_A < votes_B:
        wins_B += 1


print(f""" number of times A wins is {wins_A}
number of times B wins is {wins_B}
Percentage of A winning is {(wins_A / (wins_A+wins_B)):.2%}""")
