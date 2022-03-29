# 3CNF
Given a propositional logic formula in 3-CNF form, the model maximizes the percentage of satisfied clauses in the formula using the genetic algorithm.


## Genetic Algorithm

The genetic algorithm is a method for solving both constrained and unconstrained optimization problems that is based on natural selection, the process that drives biological evolution. The genetic algorithm repeatedly modifies a population of individual solutions. 
I implemented the basic genetic algorithm given in Artificial Intelligence: A Modern Approach (Third Edition) by Stuart J. Russell and Peter Norvig


![image](https://user-images.githubusercontent.com/68149849/160559094-a111ac92-2777-41d1-bd5c-e0b1c7b4a283.png)


I tried to improve the GA algorithm by making the following changes to the traditional GA algorithm -
- Initial number of random states - changed to half of number of clauses for more exploration and greater options to choose parents from.
- Crossover of 3 parents to produce a child - implemented using random uniform selection of 2 crossover points for every child.
- Elitism - preserved the states with maximum fitness value for the next generation. This helps in reducing the running time of the algorithm because we ensure that the best states we have found till now do not get lost in the next generations due to crossovers.

## How to execute
The program reads the 3-CNF from the given csv file using the ReadCNFfromCSVfile() function in CNF_Creator.py file, and reports the best model found.

_Note: If the improved algorithm takes more than 45 seconds, then the program is terminated and the best model found yet is reported. Algorithm is terminated if the best fitness function value does not change over 1000 generations or the fitness value of 100% is reached._
