# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 14:49:45 2021

@author: Robin
"""
""" We pick a number in a certain range. For example between 1-100. 
Let's say 97 comes up. We then have to try and guess that. Randomly we guess a number. 
Let's say we guess 40. Next we guess again within the range 41-97. How often
do we have to guess on average before we guess 97? Next how does this number change
as we increase the range? Is there a pattern?"""

import random

# here we define a function that takes the average of all the values in a list
def Average(List):
    return sum(List) / len(List)

# Here we say what the range is within which we initiate the guessing
Guessing_range = [0, 100]

# Here we set up an exponent so we can range through multiple guessing ranges
# To properly make the list of exponents we want to try we have to remove exponent 0
Exponent = 11
Exponentrange = list(range(Exponent))
Exponentrange.pop(0)

# Initiate the total list of average attempts
AvCount = []

for i in Exponentrange:
    Guessing_range = [0, 100 ** i]
    # Here we initiate the count to see how often you have to guess to get the number
    # We do this 10 times hence we make an array of 10 guesses
    Attempts = 100
    Count = [1] * Attempts
    #print(Guessing_range)
    
    # To do this guessing procedure we go through all 10 times
    for i in range(len(Count)):
        # What is the value we are going to try and guess?
        Value_point = random.randint(Guessing_range[0], Guessing_range[1])
        #print('value point is ', Value_point)
        # Now we are going to attempt to guess the value randomly, this is the reason count begins at 1
        Guess = random.randint(Guessing_range[0], Guessing_range[1])
        #print(Guess)
        # As long as we haven't guessed we adjust the range to what we guessed, we then keep guessing until we get the value.
        while not (Value_point == Guess):
            if Guess < Value_point:
                New_range = [Guess + 1, Value_point]
            else:
                New_range = [Value_point, Guess - 1]
            Guess = random.randint(New_range[0], New_range[1])
            #print(Guess)
            # We keep track of the amount of attempts we've made to try and guess
            Count[i] += 1
    
    # Now I want to know what the range is in the amount of times it takes to guess
    Max_guessattempts = max(Count)
    Min_guessattempts = min(Count)
    Attempt_range = Max_guessattempts - Min_guessattempts
    
    # Let's calculate the average amount of times we need to guess
    Average_count = Average(Count)
    # Here we add all the average counts into a total list to keep track
    AvCount.append(Average_count)
    
    #print(Count)
    #print(Attempt_range)
    #print(Average_count)
    
print(AvCount)

# Make plots vs the log of the guessingranges