# Day 10: Elves Look, Elves Say 

## Part One
Implementation is straightforward: we just count all the same digits until we encounter a different one, then we push both
of those numbers to a new string, until we reach the end of first string. We use some optimization tricks, such as appending to a list instead of adding characters to a string, which is a lot slower, since strings are imutable.

## Part Two
We just replace change the number of applications of the process.