# -*- coding: utf-8 -*-
"""
Created on Sun Jun 27 14:32:45 2021

@author: Robin
"""
""" There are three doors. Behind two of them there are goats which for some 
reason you do not want. Behind one of the three doors there's a maserati which
you do want. You can pick any one door, but before you get to open your chosen
door, the gameshow host takes one of the left over two doors, knowing which one
has a goat behind it and opens it to reveal to you that this one has a worthless
goat. Now you are given the choice to either open your chosen door, or to 
switch to the only other door and open it. Apparently, there's a 2/3 chance
to win if you do switch the doors due to the gameshow host knowing which of
the other doors has a goat. The logic is that your first choice is 1/3, and
that by the host eliminating with certainty the wrong door, you are left with
2/3 or 66.6% chance of winning if you switch."""
import random

Count_win = 0
Lose_count = 0
AttemptNumb = 1000000

# Read the following first. This is where we play a shitload of games so we can calculate a winpercentage
for attempt in range(AttemptNumb):
    # We declare the doors as an array with 0, 1, 2 position representing door 1, 2, 3
    # And we put goats in all doors (represented by a 0)
    Door = [0, 0, 0]
    
    # Now we exchange 1 goat randomly with 1 maserati (represented by a 1)
    n = random.randint(1, 3)
    Door[n-1] = 1
    Maserati_door = Door.index(1)
    
    # Now the player makes a first guess
    First_guess = random.randint(1, 3) - 1
    
    # Now the Gameshow host eliminates one of the other doors that doesn't have a maserati
    for i in range(len(Door)):
        if not i == First_guess:
            if not Door[i] == 1:
                Eliminated_door = i
    
    # Now the player switches the door choice to the second guess
    for i in range(len(Door)):
        if not i == First_guess:
            if not i == Eliminated_door:
                Switched_door = i
    
    # We open the door now and see if we won. The wins get counted, or the losses get counted
    if Switched_door == Maserati_door:
        Count_win += 1
    else:
        Lose_count += 1

# Here we calculate the win percentage of the switch strategy
#print(Count_win)
win_percent = Count_win / AttemptNumb * 100
print(win_percent)

# =============================================================================
# #Checkup to see if doors are still good
# print(Maserati_door +1)
# print(First_guess +1)
# print(Eliminated_door +1)
# print(Switched_door +1)
# =============================================================================

 

