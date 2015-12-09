# Day 8: Matchsticks 

## Part One
After trying to attack this from multiple angles, I decided for regular expressions. It was the only way to capture escaped ASCII characters (such as `\x27`) without matching those that start with \x but are not encoded ASCII characters (such as `\xss`). Escaped backlashes and quotes are easier to count with `.count()` string method.

## Part two
I sort of cheated in Part Two, beacuse Python has a bult-in function for encoding strings, so it was trivial to implement it.