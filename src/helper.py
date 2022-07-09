import math
import random
from os import path
import os

class Vertice:
    def __init__(self, num, x, y):
        self.num = num
        self.x = x
        self.y = y

    def distance_to(self, v):
        return math.sqrt((self.x-v.x)**2+(self.y-v.y)**2)

    def show(self):
        print(f'{self.num}: ({self.x},{self.y})')


def print_solution(solution, file):
    for v in solution:
        file.write(f'{v.num} ')
    file.write('')


def remove_trailing(lines):
    new_lines = []
    for line in lines:
        new_line = line.rstrip('\n')
        if new_line != '':
            new_lines.append(new_line)
    return new_lines


def init_current(vertices):
    current = vertices.copy()
    random.shuffle(current)
    return current


def aval(vertices):
    cost = 0
    for i in range(len(vertices)):
        cost += vertices[i-1].distance_to(vertices[i])
    return cost


def get_best_neighbour(current_neighbours):
    best_neighbour = current_neighbours[0]
    best_neighbour_cost = aval(best_neighbour)

    for neighbour in current_neighbours:
        cost = aval(neighbour)
        if cost < best_neighbour_cost:
            best_neighbour = neighbour
            best_neighbour_cost = cost

    return best_neighbour, best_neighbour_cost


def get_neighbour(current, i, k):
    neighbour = current.copy()

    for j in range(i):
        neighbour[j] = current[j]
    for j in range(i, k + 1):
        neighbour[j] = current[k - j + i]
    for j in range(k + 1, len(current)):
        neighbour[j] = current[j]

    return neighbour


def get_random_neighbour(current):
    neighbours = get_all_neighbours(current)
    neighbour = neighbours[random.randint(0, len(current)-1)]

    return neighbour


def get_all_neighbours(current):
    n = len(current)
    neighbours = []

    for k in range(2, n-1):
        neighbours.append(get_neighbour(current, 1, k))
    for i in range(2, n-1):
        for k in range(i+1, n):
            neighbours.append(get_neighbour(current, i, k))

    return neighbours


def read_file(file_path):
    if not path.exists(file_path):
        print('Arquivo de entrada não encontrado')
    else:
        with open(file_path, 'r') as input_file:
            lines = input_file.readlines()
            lines = remove_trailing(lines)

            vertices = []
            for line in lines:
                num, x, y = line.split()
                vertices.append(Vertice(int(num), float(x), float(y)))

        return vertices


def create_output_dir():
    try:
        os.mkdir('./output')
    except FileExistsError:
        pass


def write_solution(solution, solution_cost, output_file_name):
    with open(path.join('./output', output_file_name), 'w') as output_file:
        output_file.write('Solution: ')
        print_solution(solution, output_file)
        output_file.write(f'\nSolution cost: {solution_cost:.2f}')
    print(f'Resultado salvo no arquivo {output_file_name}')
