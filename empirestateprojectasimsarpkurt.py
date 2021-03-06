# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 16:22:18 2021

@author: Asım Sarp Kurt
"""
#I conducted this case study thanks to DataCamp.
#Rules Of The Game
#Imagine the following: you're walking up the empire state building to DataCamp HeadQuarters and you're playing a game with a friend.
#You throw a die one hundred times.
#If it's 1 or 2 you'll go one step down.
#If it's 3, 4, or 5, you'll go one step up.
#If you throw a 6, you'll throw the die again and will walk up the resulting number of steps.
#Of course, you can not go lower than step number 0. And also, you admit that you're a bit clumsy and have a chance of 0.1% of falling down the stairs when you make a move. Falling down means that you have to start again from step 0. With all of this in mind, you bet with your friend that you'll reach 60 steps high.
#Objective-->The main aim is creating pseudo-random numbers, which will be consistent between runs.
import numpy as np
    # Numpy is imported, seed is set
np.random.seed(3)	
	# Starting step
step = 50
	# Roll the dice
dice=np.random.randint(1,7)
	# Finish the control construct
if dice <= 2 :
	    step = step - 1
elif dice<6 :
	    step=step+1
else :
	    step = step + np.random.randint(1,7)
# Print out dice and step
print(dice,step)
