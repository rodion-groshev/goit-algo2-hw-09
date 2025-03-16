##  Task. Minimize Sphere function

   Implement a program to minimize the Sphere function using three different approaches to local optimization:

-   Hill Climbing algorithm
-   Random Local Search
-   Simulated Annealing


#### Specifications:

1. The limits of the function are defined as xi∈[-5,5]xi∈[-5,5] for each parameter xixi.


2. The algorithms must return the optimal point (a list of x coordinates) and the value of the function at this point.


3. Implement three optimization methods:

    hill_climbing - a hill climbing algorithm.
    random_local_search - random local search.
    simulated_annealing - simulation of annealing.


4. Each algorithm must accept the iterations parameter, which determines the maximum number of iterations to execute the algorithm.


5. Algorithms must terminate execution under one of the conditions:

    The change in the value of the objective function or the position of a point in the solution space between two consecutive iterations becomes less than epsilon, where epsilon is an accuracy parameter and determines the sensitivity of the algorithm to small improvements.
    For the annealing algorithm, the temperature is taken into account: if the temperature decreases to a value less than epsilon, the algorithm terminates execution, as this indicates that the search ability of the algorithm has been exhausted.