class Maze:
    def __init__(self, file_path):
        self.grid = []
        self.start = None
        self.goal = None
        self.load_maze(file_path)

    def load_maze(self, file_path):
        with open(file_path, 'r') as file:
            for y, line in enumerate(file):
                row = list(line.strip())
                self.grid.append(row)
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
