# Day 6: Probably a Fire Hazard 

My solutions for this are awfully slow for some reason, if someone finds the bottleneck, please let me know.

## Part One
We define three lambdas for turning on, turning off, and toggling lights. Then we loop through instructions, and change every light in the grid that's covered by those instructions.

## Part two
Similar to Part One, but even easier because all changes are constant numbers(+1, +2, or -1).