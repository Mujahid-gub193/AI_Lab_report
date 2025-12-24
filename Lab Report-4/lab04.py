import random

def fitness(board):
    """Calculate number of non-attacking pairs of queens"""
    n = len(board)
    non_attacking = 0
    for i in range(n):
        for j in range(i + 1, n):
            if board[i] != board[j] and abs(board[i] - board[j]) != j - i:
                non_attacking += 1
    return non_attacking

def generate_board(n):
    """Generate a random board"""
    board = list(range(n))
    random.shuffle(board)
    return board

def crossover(parent1, parent2):
    """Order 1 crossover"""
    n = len(parent1)
    start, end = sorted(random.sample(range(n), 2))
    child = [None]*n
    child[start:end+1] = parent1[start:end+1]
    p2_idx = 0
    for i in range(n):
        if child[i] is None:
            while parent2[p2_idx] in child:
                p2_idx += 1
            child[i] = parent2[p2_idx]
    return child

def mutate(board, mutation_rate=0.1):
    n = len(board)
    if random.random() < mutation_rate:
        i, j = random.sample(range(n), 2)
        board[i], board[j] = board[j], board[i]

def genetic_algorithm(n, population_size=100, max_generations=1000):
    population = [generate_board(n) for _ in range(population_size)]
    max_fitness = n*(n-1)//2 

    for generation in range(max_generations):
        population.sort(key=lambda x: fitness(x), reverse=True)
        if fitness(population[0]) == max_fitness:
            print(f"Solution found in generation {generation}:")
            print(population[0])
            return population[0]

        top_half = population[:population_size//2]
        new_population = []
        while len(new_population) < population_size:
            parent1, parent2 = random.sample(top_half, 2)
            child = crossover(parent1, parent2)
            mutate(child)
            new_population.append(child)

        population = new_population

    print("No solution found.")
    return None
if __name__ == "__main__":
    N = 8 
    genetic_algorithm(N)
