# N-Queens Problem Using Genetic Algorithm

## Algorithm Explanation
The N-Queens problem is solved using a **Genetic Algorithm (GA)**.  
The algorithm works as follows:

1. **Initial Population:** Generate a set of random boards.  
2. **Fitness Function:** Evaluate each board by counting non-attacking pairs of queens.  
3. **Selection:** Choose the top-performing boards for reproduction.  
4. **Crossover:** Combine two parent boards to produce a child board.  
5. **Mutation:** Swap positions of queens randomly with a small probability to maintain diversity.  
6. **Iteration:** Repeat selection, crossover, and mutation until a solution is found or maximum generations are reached.

This approach allows the population to evolve towards a solution where no queens attack each other.

---

## How to Run
1. Open the folder in VS Code.  
2. Set the value of `N` (number of queens) in `lab04.py`.  
3. Run in terminal:
```bash
python lab04.py
