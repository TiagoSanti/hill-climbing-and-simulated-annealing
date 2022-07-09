import os
from os import path
import sys
import helper
import math
import random


def main():
    arguments = sys.argv
    if len(arguments) != 6:
        print('Quantidade de argumentos inválida -> python3 simulated_annealing.py <caminho do arquivo de entrada> '
              '<Tmax> <k> <Kt> <Tmin>')
    else:
        file_path = arguments[1]
        if not os.path.exists(file_path):
            print('Arquivo de entrada não encontrado')
            return 0

        Tmax = int(arguments[2])
        k = float(arguments[3])
        Kt = int(arguments[4])
        Tmin = int(arguments[5])

        vertices = helper.read_file(file_path)

        solution, solution_cost = simulated_annealing(vertices, Tmax, k, Kt, Tmin)

        output_file_name = path.split(file_path)[-1]
        name, ext = '.'.join(output_file_name.split('.')[:-1]), output_file_name.split('.')[-1]
        output_file_name = f'{name}_{Tmax}_{k}_{Kt}_{Tmin}.{ext}'
        helper.create_output_dir()
        helper.write_solution(solution, solution_cost, output_file_name)


def prob(candidate_cost, current_cost, T):
    try:
        probability = 1/(1+math.exp(candidate_cost-current_cost/T))
    except OverflowError:
        probability = math.inf
    return probability


def g(T, k):
    return k*T


def simulated_annealing(vertices, Tmax, k, Kt, Tmin):
    T = Tmax
    current = helper.init_current(vertices)
    current_cost = helper.aval(current)

    while T >= Tmin:
        print(f'Temperatura {T:.2f} >= {Tmin} ..')
        for t in range(Kt):
            candidate = helper.get_random_neighbour(current)
            candidate_cost = helper.aval(candidate)

            if candidate_cost < current_cost:
                current, current_cost = candidate, candidate_cost
            elif random.random() < prob(candidate_cost, current_cost, T):
                current, current_cost = candidate, candidate_cost

        T = g(T, k)

    return current, current_cost


if __name__ == '__main__':
    main()
