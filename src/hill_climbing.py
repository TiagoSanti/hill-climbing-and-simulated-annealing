import os
from os import path
import sys
import helper
import math


def main():
    arguments = sys.argv
    if len(arguments) != 3:
        print('Quantidade de argumentos inválida -> python3 hill_climbing.py <caminho do arquivo de entrada> <MAX>')
    else:
        file_path = arguments[1]
        if not os.path.exists(file_path):
            print('Arquivo de entrada não encontrado')
            return 0

        MAX = int(arguments[2])

        vertices = helper.read_file(file_path)

        solution, solution_cost = hill_climbing(vertices, MAX)

        output_file_name = path.split(file_path)[-1]
        name, ext = '.'.join(output_file_name.split('.')[:-1]), output_file_name.split('.')[-1]
        output_file_name = f'{name}_{MAX}.{ext}'
        helper.create_output_dir()
        helper.write_solution(solution, solution_cost, output_file_name)


def hill_climbing(vertices, MAX):
    best = []
    best_cost = math.inf

    for t in range(MAX):
        print(f'Iteração {t+1}/{MAX}..')
        local = True

        current = helper.init_current(vertices)
        current_cost = helper.aval(current)

        while local:
            neighbours = helper.get_all_neighbours(current)
            best_neighbour, best_neighbour_cost = helper.get_best_neighbour(neighbours)

            if best_neighbour_cost < current_cost:
                current, current_cost = best_neighbour, best_neighbour_cost
            else:
                local = False

        if current_cost < best_cost:
            best = current
            best_cost = current_cost

    return best, best_cost


if __name__ == '__main__':
    main()
