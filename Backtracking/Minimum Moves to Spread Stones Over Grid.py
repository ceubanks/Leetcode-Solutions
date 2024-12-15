'''
Given a 2D grid of integers of size (3×3), 
where each value represents the number of stones in the given cell, 
return the minimum number of moves required to place exactly one stone in each grid cell.

Constraints:

Only one stone can be moved in one move.

Stone from a cell can only be moved to another cell if they are adjacent (share a side).

The sum of all stones in the grid must be equal to 
9
.

grid.length = 3, grid[i].length = 3
'''

'''
3 0 1
0 2 2
0 0 1

output: 6


'''


'''
Extra stone locations:
[
(0,0), 3)
(1,1), 2)
(1,2), 2)
]

Zero stone locations:
[(0,1), (2,0), (2,1), (2,2)]

(0,0) has 3 stones, so we can move 1 stone to (0,1) and remove (0,1) from zero stone locations
(0,0) has 2 stones, so we can move 1 stone to (0,1) 
(1,1) has 2 stones, so we can move 1 stone to 

(1,1) has 2 stones, so we can move 1 stone to (2,0)
(1,2) has 2 stones, so we can move 1 stone to (2,1)

Now we have:
[(0,0), 1)
(1,1), 1)
(1,2), 1)


'''

'''
1. Check if sum of all stones is 9
2. Find extra stones locations and zero stones locations
3. Backtrack to find the minimum moves.
    a. If we have extra stones, we can move them to zero stones locations.
    b. If we have multiple extra stones, we can move them to the same zero stone location.
    c. We can move one stone at a time to a zero stone location.
'''
DIRECTIONS = [(0,1), (1,0), (0,-1), (-1,0)]
def min_moves(grid):

    # check if sum of all stones is 9
    total_stones = sum(sum(row) for row in grid)
    if total_stones != 9:
        return -1
    
    # find extra stones locations and zero stones locations
    extra_stones_locations = {}
    zero_stones_locations = set()

    min_moves = float('inf')

    for i in range(3):
        for j in range(3):
            if grid[i][j] > 1:
                extra_stones_locations[(i, j)] = grid[i][j]
            elif grid[i][j] == 0:
                zero_stones_locations.add((i, j))

    def backtrack(moves):
        nonlocal min_moves
        if moves >= min_moves:  # Pruning: skip if we've already found a better solution
            return
            
        if not zero_stones_locations:  # Changed condition
            min_moves = min(min_moves, moves)
            return
        
        curr_extra = dict(extra_stones_locations)
        for extra_stone_location, count in curr_extra.items():
            x, y = extra_stone_location
            for zero_loc in list(zero_stones_locations):
                zx, zy = zero_loc
                # Calculate Manhattan distance
                dist = abs(x - zx) + abs(y - zy)
                
                # Only proceed if we can move a stone to this zero location
                if count > 1 or (count == 1 and len(extra_stones_locations) > 1):
                    # Move stone
                    extra_stones_locations[extra_stone_location] = count - 1
                    if extra_stones_locations[extra_stone_location] == 1:
                        extra_stones_locations.pop(extra_stone_location)
                    
                    zero_stones_locations.remove(zero_loc)
                    grid[zx][zy] = 1
                    
                    backtrack(moves + dist)
                    
                    # Restore state
                    if count > 1:
                        extra_stones_locations[extra_stone_location] = count
                    else:
                        extra_stones_locations[extra_stone_location] = count
                    zero_stones_locations.add(zero_loc)
                    grid[zx][zy] = 0

    backtrack(0)
    return min_moves if min_moves != float('inf') else -1
    
    
print(min_moves([[3, 0, 1], [0, 2, 2], [0, 0, 1]]))
    
    
    