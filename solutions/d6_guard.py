from d6_cell_type import CellType
from d6_grid import Grid


class Guard:
    def __init__(self, grid:Grid):
        self.grid = grid
        self.initialize_position()
        self.direction = (-1, 0)
        self.grid.update(x = self.current_x, y = self.current_y, cell_type=CellType.VISITED)
        self.visited = [(self.current_x, self.current_y, self.direction)]

    def initialize_position(self):
        for i in range(self.grid.dim[0]):
            for j in range(self.grid.dim[1]):
                if self.grid.grid[i][j].cell_type == CellType.VISITED:
                    self.current_x = i
                    self.current_y = j
                    print(f"current_x: {self.current_x}, current_y: {self.current_y}")

    def is_valid_move(self)->str:
        x, y = self.current_x + self.direction[0], self.current_y + self.direction[1]
        if 0 <= x < self.grid.dim[0] and 0 <= y < self.grid.dim[1] and self.grid.grid[x][y].cell_type != CellType.OBSTACLE:
            return "valid"
        elif 0 <= x < self.grid.dim[0] and 0 <= y < self.grid.dim[1] and self.grid.grid[x][y].cell_type == CellType.OBSTACLE:
            return "obstacle"
        elif x < 0 or x >= self.grid.dim[0] or y < 0 or y >= self.grid.dim[1]:
            return "out_of_bounds"
            

    def move(self)->bool:
        if self.is_valid_move() == "valid": 
            self.current_x += self.direction[0] 
            self.current_y += self.direction[1]
            self.grid.update(self.current_x, self.current_y, CellType.VISITED)
            self.visited.append((self.current_x, self.current_y, self.direction))
            return True
        elif self.is_valid_move() == "obstacle":
            # rotate right
            self.direction = (self.direction[1], -self.direction[0])
            return True
        elif self.is_valid_move() == "out_of_bounds":
            return False
        
    def count_visited(self)->int:
        return self.grid.count_visited()
    