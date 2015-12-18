# Day 14: Reindeer Olympics  

##Part One
For every deer we generate a `movement` list which contains its movement for its entire period. For example, if we have a deer which goes 4 km/h for 5 seconds, and then rests for 5 seconds, his list would look like this: `[4, 4, 4, 4, 4, 0, 0, 0, 0, 0]`. Then, in `calculate` funciton we calculate the number of whole cycles it completes, and add to that the extra steps.

## Part Two
Part Two involves some more `map` abusing. `results` list contains an entry for each deer, which is incremented for every second when that deer is leading. For every second, we calculate the distance for every deer, find the biggest one, and increment his entry. In the end we just print the highest one.