# Day 5: Doesn't He Have Intern-Elves For This?

## Part One
Part One is simple, we just count the number of vowels, douslbe characters, and forbidden strings, and check if they fulfill the requirements

## Part two
Part Two is a little bit more complicated. The first loop looks for pairs of same leters with a different letter between them (such as zxz), and the second loop looks for two consecutive letters that appear more than once in a string. If both of those conditions are fulfilled, the string is nice.