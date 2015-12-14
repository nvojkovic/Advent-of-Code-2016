# Day 13: Knights of the Dinner Table 

##Part One
We can permutate 8 around the talbe in `8!` possible seating arrangments, but for every arrangment, there are 8 rotations that are equivalent, so the actual number of arrangments is `8!/8 = 7!`. We simulate that by putting the first person into a fixed position, and then putting everyone else around the table. `itertools.permutations` are used to calculate all of the permutations, and the function `evaluate` calculates the total change in happiness for every seating arrangment. We run through all of the permutations and print the total change in happiness of the best one.

## Part Two
Very similar to Part One, but now we have the `addMe` function, which adds us to the list of people, and adds our indifference towards everyone (and vice versa) to the dictionary.

