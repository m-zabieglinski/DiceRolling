import numpy as np
import matplotlib.pyplot as plt

#diceroll rolls n d-sided dice and returns the sum of their results
def diceroll(n = 1, d = 6):
    sum = 0
    for i in range(n):
        sum = sum + np.random.randint(1, d+1)
    return sum

#mixroll combines multiple dicerolls: n and d are now lists of number and type of dice
#for example, mixroll(n = [2,5], d = [6, 7]) will roll 2 6-sided die and 5 7-sided die
def mixroll(n = [1], d = [6]):
    n = [n]
    d = [d]
    if len(n) != len(d):
        print("ERROR: input the list of the number of each dice thrown and the type of each dice thrown. lists must be same length")
    else:
        sum = 0
        for k in range(len(n)):
            for i in range(n[k]):
                sum = sum + np.random.randint(1, d[k]+1)
        return sum

#diceprobtable does the same diceroll many times (def 20k) and creates a probability table of each value
#it returns a dictionary
def diceprobtable(n = 1, d = 6, N = 20000):
    val = list(range(n, n*d+1))
    freq = [0] * (d * n)
    dictionary = {val[i]: freq[i] for i in range(len(val))}
    for i in range(N):
        temp_roll = diceroll(n, d)
        dictionary[temp_roll] += 1
    for val in dictionary:
        dictionary[val] = dictionary[val] / N        
    return dictionary;

#DiceRollDist creates a class that represents a singular diceroll
#method tables returns diceprobtable for that roll
#method plot plots that diceroll table as neat graph
class DiceRollDist():
    
    def __init__(self, NumberOfDice, NumberOfSides, NumberOfRolls = 20000):
        self.n = NumberOfDice
        self.d = NumberOfSides
        self.N = NumberOfRolls
        self.table = diceprobtable(NumberOfDice, NumberOfSides, NumberOfRolls)
        
    def table(self):
        self.table
    
    def plot(self, dpi = 300):
        
        plt.rcParams['figure.dpi'] = dpi
        plt.rcParams['savefig.dpi'] = dpi
        
        Val = list(self.table.keys())
        Freq = list(self.table.values())
        
        median = sum(list(range(1, 7))) / self.d * self.n
        
        plt.scatter(Val, Freq, color = "red")
        plt.ylim([0, 1.2 * max(Freq)])
        plt.xlim([min(Val), max(Val)])
        
        Val_ticks = np.array([median] * 9)
        
        scale = 4
        for i in range(scale):
            Val_ticks[i] = i/scale * Val_ticks[i] + (1-i/scale) * min(Val)
            Val_ticks[i + scale + 1] = i/scale * Val_ticks[i + scale + 1] + (1-i/scale) * max(Val)
        
        
        plt.xticks(Val_ticks)
                     
        plt.xlabel("Value on the dice")
        plt.ylabel("Frequency")
        plt.title(f"Value distribution for {self.n} {self.d}-sided dice thrown {self.N} times")
        
        plt.vlines(x = median, ymin = 0, ymax = max(Freq), colors = 'black', linestyles = '--', linewidth = 5)
        
        plt.grid()
        
        plt.show()
