class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0 
        seen = set()
        directions = [[1,0],[-1,0],[0,1],[0,-1]]

        def explore(y,x):
            for yd, xd in directions:
                y_new = y+yd
                x_new = x+xd
                if y_new < len(grid) and y_new > -1:
                    if x_new < len(grid[0]) and x_new > -1:
                        if (y_new, x_new) not in seen and grid[y_new][x_new] == "1":
                            seen.add((y_new, x_new))
                            explore(y_new, x_new)

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if (y,x) not in seen and grid[y][x] == "1":
                    explore(y,x)
                    count+=1
        return count