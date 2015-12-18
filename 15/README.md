# Day 15: Science for Hungry People  

##Part One
The problem is small enough to be bruteforced, but of course, some optimizations must be made. Since all numbers are positive, the amount of the first ingredient must be somewhere between `0` and `100`, the amount of the second one must be between `0` and `100 - first`, and so on. This leaves us with only 176851 combinations to run through, which is doable in reasonable time.

## Part Two
Same as Part One, but with added condition that total calories must be 500.