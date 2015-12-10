# Day 7: Some Assembly Required

This is the first problem that I found  interesting, as it didn't require only routine string manipulation.

**NOTE:** Python's bitwise NOT function doesn't behave the way this problem needs it to. Since all signals are unsigned 16-bit integers, we can calculate bitwise NOT as `2**16 - 1 - x`, where x is the number we want to invert.

## Part One
When we load the instructions, we create a dictionary `exps`, which is the central piece of the algorithm. In the beggining, it contains integer values for wires that already have input, or a string instruction for those that don't. Then we call a recursive function `parse` on a wire we want calculated (in this case it is `a` wire, and the function automatically calculates all the dependencies of `a` recursively, until it hits a number. That number then replaces the string instruction for that wire, so the next time we need it, it's already precomputed (this way, the dictionary also serves as memoization). Once all the dependencies are resolved, `exps['a']` contains the value we need.

## Part two
Same as Part One, we just manually set `exps['b']`.