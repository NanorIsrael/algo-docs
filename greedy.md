# How greedy algorithms work

Greedy algorithms work by making the locally optimal choice at each stage with the hope of finding a global optimum. In other words, at each step of the algorithm, it chooses the best possible solution without considering the consequences of that choice on future steps.

The key characteristic of greedy algorithms is that they make a series of choices that are optimal at the time, but there is no guarantee that these choices will lead to the overall optimal solution. However, in many cases, greedy algorithms can provide a sufficiently good solution, especially when the problem has the greedy-choice property and the optimal solution can be reached by a series of local optimal choices.

Here's a general outline of how a greedy algorithm works:

Initialization: Start with an empty solution or an initial feasible solution.

Selection: At each step, select the best available choice. This choice should be locally optimal, meaning it is the best choice among the options available at that step.

Feasibility: Ensure that the chosen solution is feasible, i.e., it satisfies all constraints of the problem.

Optimality: Repeat the selection process until a complete solution is obtained. The hope is that the series of locally optimal choices will lead to the global optimal solution.

Termination: The algorithm terminates when a complete solution is obtained.

Greedy algorithms are commonly used in optimization problems where a solution needs to be found that maximizes or minimizes a certain objective function. Examples include finding the shortest path in a graph (Dijkstra's algorithm), minimizing the number of coins for change (making change problem), and scheduling tasks to minimize completion time (interval scheduling).


## limitations of greedy algorithms

While greedy algorithms are simple and efficient, they may not always provide the optimal solution for a given problem. Some limitations of greedy algorithms include:

No backtracking: Greedy algorithms make decisions based on the current state without considering future consequences. This lack of backtracking means that once a decision is made, it cannot be undone, which can lead to suboptimal solutions.

Local optimum: Greedy algorithms choose the best local option at each step, hoping that it will lead to the global optimum. However, this approach does not guarantee the best overall solution, as the optimal solution may require a series of non-local choices.

Dependency on problem structure: Greedy algorithms rely heavily on the problem having the greedy-choice property, where the optimal solution can be reached by making locally optimal choices. If this property does not hold, the greedy algorithm may fail to find the optimal solution.

Complexity analysis: Analyzing the correctness and efficiency of greedy algorithms can be challenging, as it requires proving that the locally optimal choices lead to the global optimum in all cases.

Scenarios where greedy algorithms might not provide the optimal solution include:

Non-greedy-choice property: If the problem does not have the greedy-choice property, the greedy algorithm may select a locally optimal choice that leads to a suboptimal solution overall. For example, in the traveling salesman problem, choosing the nearest city at each step may not lead to the shortest overall path.

Dependency on future choices: Some problems require considering future choices to make the best decision at each step. Greedy algorithms, which make decisions based solely on the current state, may not be able to take into account these future dependencies.


## Basic principles of dynamic programming as a method to solve optimization problems

Dynamic programming is a method for solving complex problems by breaking them down into simpler subproblems and solving each subproblem only once, storing the results to avoid redundant computations. The key principles of dynamic programming are:

Optimal substructure: A problem has optimal substructure if an optimal solution to the problem contains optimal solutions to its subproblems. This property allows us to solve a complex problem by solving its subproblems recursively and then combining the solutions to the subproblems to obtain the optimal solution to the original problem.

Overlapping subproblems: A problem has overlapping subproblems if it can be broken down into subproblems that are reused several times. Dynamic programming solves each subproblem once and stores the solution in a table (usually an array or matrix), so that the next time the same subproblem occurs, its solution can be looked up rather than recomputed.

Dynamic programming is used to solve optimization problems where we need to find the best solution from a set of possible solutions. It is particularly useful for problems that can be divided into overlapping subproblems and have optimal substructure. By using dynamic programming, we can avoid redundant computations and find the optimal solution efficiently.

The general steps involved in solving a problem using dynamic programming are:

- Define the subproblems: Determine the structure of the subproblems and how they relate to each other.

- Formulate a recurrence relation: Express the solution to each subproblem in terms of solutions to smaller subproblems.

- Identify the base cases: Determine the simplest subproblems that can be solved directly without further recursion.

- Build a table (or array) to store the solutions: Use the recurrence relation to fill in the table from the base cases up to the final solution.

- Compute the optimal solution: Use the table to find the optimal solution to the original problem.

## The concept of overlapping subproblems and optimal substructure in the context of the coin change problem.


n the context of the coin change problem, which is a classic problem in dynamic programming, overlapping subproblems and optimal substructure play important roles.

Overlapping subproblems: In the coin change problem, overlapping subproblems arise because the same subproblems are encountered multiple times during the computation of the optimal solution. For example, when considering how many ways there are to make change for a certain amount using a certain set of coin denominations, the subproblem of making change for a smaller amount may be encountered multiple times.

Optimal substructure: The coin change problem exhibits optimal substructure because the optimal solution to the problem can be constructed from the optimal solutions to its subproblems. Specifically, if we know the minimum number of coins needed to make change for smaller amounts, we can use this information to determine the minimum number of coins needed to make change for a larger amount.

Dynamic programming exploits these properties by storing the solutions to subproblems in a table (often called a memoization table or DP table) and reusing these solutions to avoid redundant computations. By building up solutions from smaller subproblems and storing them in a table, dynamic programming efficiently solves the coin change problem and other problems with similar characteristics.


##



