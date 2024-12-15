def flood_fill(grid, sr, sc, target):
  # get source value
  source_value = grid[sr][sc]

  if source_value == target:
    return grid
  # use backtracking to go through source and update grid
  def is_valid(row, col):
    nonlocal source_value
    return row >= 0 and row < len(grid) and col >= 0 and col < len(grid[0]) and grid[row][col] == source_value
    
  
  def backtracking(row, col):
    
    grid[row][col] = target
    
    DIRECTIONS = [(1,0), (0,1), (-1,0), (0,-1)]
    
    for dx, dy in DIRECTIONS:
      nx, ny = dx + row, dy + col
      if is_valid(nx, ny):
        backtracking(nx, ny)
  
  backtracking(sr, sc)
  return grid