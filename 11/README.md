# Day 11: Corporate Policy  

Implementation is awfully inefficient, taking ~16 seconds for Part 1, and ~63 for Part 2, but at that point I was too tired to write anything better.

## Part One
`convert` and `convert2` convert password from string to base-26 number and back. When we convert it to a number, we increment it by one and convert it back to string. This double conversion is probably the source of inefficiency.
`isValid` checks is the password valid by matching against constraints in form of lists.
We just run through passwords until we find a valid one.

## Part Two
We just have to change the input.