# DiceRolling

dicerolling.py is a Python file that will help you roll dice.

It contains 3 functions:

  **diceroll(n, d)** which rolls n d-sided dice and returns the sum of the results
  
  **diceprobtable(n, d, N)** which rolls n d-sided dice N times and returns an estimated probability of rolling each value as a dictionary
  
  
  **mixroll(n, d)** which is based on diceroll but allows n and d to be lists, so you can roll different kinds of dice at once
  (for example, mixroll(n = [2,5], d = [6, 7]) will roll 2 6-sided die and 5 7-sided die. This one is odd in the family and the rest don't really talk to them
  
 
and 1 class with 2 methods:

**DiceRollDist** creates a class that represents a singular diceroll:

  -method tables returns diceprobtable for that roll
  
  -method plot plots that diceroll table as neat graph
  
  Example:
  ```
  import dicerolling as dr

dyst6x6 = dr.DiceRollDist(6, 6)
print(dyst6x6.table)
dyst6x6.plot()
```
returns
```
{6: 0.0, 7: 0.0001, 8: 0.0002, 9: 0.001, 10: 0.00255, 11: 0.00505, 12: 0.01085, 13: 0.01545, 14: 0.02465, 15: 0.0376, 16: 0.04515, 17: 0.06095, 18: 0.074, 19: 0.0822, 20: 0.091, 21: 0.092, 22: 0.0952, 23: 0.08185, 24: 0.07255, 25: 0.06075, 26: 0.047, 27: 0.037, 28: 0.0242, 29: 0.01815, 30: 0.00955, 31: 0.00665, 32: 0.00295, 33: 0.00085, 34: 0.00035, 35: 0.0002, 36: 0.0}
```
![dyst6x6.plot()](https://github.com/[username]/[reponame]/blob/[branch]/image.jpg?raw=true)
