# hill-climbing-and-simulated-annealing
Travelling Salesman Problem solving with Hill Climbing and Simulated Annealing heuristics

The algorithms have been successfully executed using 3.10.5 Python version.
For its execution, use the following command format:

    <python or python3> <heuristic script file path> <input file path> <parameters>

Example:

    D:\UFMS\IMPLEMENTAÇÃO ALGORÍTMICA\Trabalho_Final> python3 ./hill_climbing.py ./graphs/att48.tsp.txt 2

"D:\UFMS\IMPLEMENTAÇÃO ALGORÍTMICA\Trabalho_Final>" as directory in cmd<br>
"python3" as Python interpreter<br>
"./hill_climbing.py" as the hill climbing algorithm file<br>
"./graphs/att48.tsp.txt" as the input file containing the graph info and "2" is the MAX parameter for hill climbing<br>

For hill climbing, the parameters are: MAX (integer)<br>
For simulated annealing, the parameters are: Tmax (integer), k (float), Kt (integer), Tmin (integer)

The algorithms will create a directory "output" to store the output .txt file containing the solution found with its cost, its name will contain the parameters used for execution. 

The file helper.py has common functions for both algorithms.

The following are the known best solutions fot graphs in 'graphs' directory:
* att48 : 10628
* berlin52 : 7542
* bier127 : 118282
* eil76 : 538
* kroA100 : 21282
* kroE100 : 22068
* pr76 : 108159
* rat99 : 1211
* st70 : 675