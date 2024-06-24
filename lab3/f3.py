def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if 2 * chickens + 4 * rabbits == numlegs:
            return chickens, rabbits
    return "No solution"
numheads = 35
numlegs = 94
result = solve(numheads, numlegs)
if result != "No solution":
    chickens, rabbits = result
    print(f"Number of chickens: {chickens}, Number of rabbits: {rabbits}")
else:
    print("No valid solution found.")