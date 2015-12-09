# Day 3: Perfectly Spherical Houses in a Vacuum 

## Part One
We have a set of visited coordinates, and depending on direction, we move, and then we add those new coordinates to the set. Because sets can't contain duplicates, printing size of the set is the answer

## Part two
Same as Part One, but be have two pairs of coordinates, one for Santa, and one for RoboSanta. We use modulo operator to determine who moves (when index of a character is divisible by two, Santa moves, when it's not, RoboSanta moves).