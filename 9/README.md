# Day 9: All in a Single Night 

This is a classic Hamiltonian path problem from graph theory (https://en.wikipedia.org/wiki/Hamiltonian_path_problem). Since it's NP complete, there are no efficient solutions, but because there are only 8 locations to visit, there are only  ` 8!=40320` possible paths, we can just run through all of them and pick the best one.
## Part One
We create a set of locations and a dict of distances. Using `itertools.permutations` we genereate all the permutations of locations and pick the shortest path.


## Part two
Same as Part One, but we are looking for the longest path.