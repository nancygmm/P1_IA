class Maze:
    def __init__(self, laberinto_data):
        self.grid = laberinto_data
        self.start = None
        self.goal = None
        self.find_start_and_goal()

    def find_start_and_goal(self):
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell == 'I':  
                    self.start = (x, y)
                elif cell == 'G': 
                    self.goal = (x, y)

    def get_neighbors(self, position):
        x, y = position
        neighbors = []
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= ny < len(self.grid) and 0 <= nx < len(self.grid[0]):
                if self.grid[ny][nx] != '#':  
                    neighbors.append((nx, ny))

        return neighbors

    def print_maze(self, path=None):
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if path and (x, y) in path:
                    print('*', end=' ') 
                else:
                    print(cell, end=' ')
            print()
