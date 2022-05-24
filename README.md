# DiceRolling

dicerolling.py is a Python file that will help you roll dice.

It contains 3 functions:

  -diceroll(n, d) which rolls n d-sided dice and returns the sum of the results
  
  -diceprobtable(n, d, N) which rolls n d-sided dice N times and returns an estimated probability of rolling each value as a dictionary
  
  
  -mixroll(n, d) which is based on diceroll but allows n and d to be lists, so you can roll different kinds of dice at once
  (for example, mixroll(n = [2,5], d = [6, 7]) will roll 2 6-sided die and 5 7-sided die. This one is odd in the family and the rest don't really talk to them
  
 
and 1 class with 2 methods:

-DiceRollDist creates a class that represents a singular diceroll:

  *method tables returns diceprobtable for that roll
  
  *method plot plots that diceroll table as neat graph
