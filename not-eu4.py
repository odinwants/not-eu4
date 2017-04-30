#!/usr/bin/env python3
"""
    TODO 1.0: Make a loop at user input, to pick the army composition
    TODO 1.1: Add a system to form an army such as typing 'inf10, cav4, art3' 
    TODO 1.1: Or else, like 'build(infantry, 6)' and 'buid(cavalry, 2)'
    TODO 2.0: Each kind of unit has their own stats/pros/cons
    TODO 3.0: Different terrain will change the amount of units i.e*
    TODO 3.1: Variables= Nation1 has more troops but Nation2 has better units (technology)
    TODO 3.1: Variables= Nation1 attacks on defensive terrain (combat penalty)
    TODO 3.1: i.e rough/bad/defensive/uninhabited/river/crossing = smaller rows
    TODO 3.1: i.e good/flat/dry/no_river = bigger rows
    TODO 4.0: |C| - |X| - |X| - |X| - |X| - |X| - |X| - |X| - |X| - |X| - |X| - |C|
    TODO 4.0: |C| - | | - | | - |0| - |0| - |0| - |0| - |0| - |0| - | | - | | - |C|
    TODO 4.0: |X| = infantry, gets deployed in the center *cheap
    TODO 4.0: |C| = cavalry gets deployed in the flank *a little more expensive
    TODO 4.0: |0| = artillery gets deployed in the back *very expensive
    TODO 5.0: Make battles, with random numbers for each side (maybe not, will see)
"""
class Army(object):
    def __init__(self):
        self.troops = [[2, 0.5, 1, 1], [1, 4, 3.5, 1], [4, 2, 0.5, 4]]
        self.inf = self.troops[0]
        self.cav = self.troops[1]
        self.art = self.troops[2]
    
    def build(self, typeOfUnit, amount, price): 
        return typeOfUnit, amount, price

def main():
    #creates the object
    x = Army()
    #types of units
    infantry = x.inf
    cavalry = x.cav
    artillery = x.art
    #user input,
    typeOfUnit = input("Type of troops (infantry, cavalry, artillery): ")
    amount = int(input("Amount of troops: "))
    #decision making
    if(typeOfUnit == infantry):
        print(x.build(typeOfUnit, amount, 0.3 * amount)) #last one is price

    elif(typeOfUnit == cavalry):
        print(x.build(typeOfUnit, amount, 0.6 * amount)) #last one is price

    elif(typeOfUnit == artillery):
        print(x.build(typeOfUnit, amount, 1.2 * amount)) #last one is price
    
    return 0
    
if __name__ == '__main__':
	main()
  
