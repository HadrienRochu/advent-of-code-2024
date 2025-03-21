from d6_cell_type import CellType
from d6_cell import Cell

class Grid:
    def __init__(self, grid:list[str]):
        self._construct_grid(grid)
        self.dim = (len(self.grid), len(self.grid[0]))

    def _construct_grid(self, grid:list[list[str]]):
        self.grid = [[Cell.factory(x=j, y=i, cell_value=grid[i][j]) for j in range(len(grid[i])) if Cell.factory(x=i, y=j, cell_value=grid[i][j]) != None] for i in range(len(grid))]

    def count_visited(self)->int:
        return sum([sum([1 for cell in row if cell.cell_type == CellType.VISITED]) for row in self.grid])
        
    def update(self, x:int, y:int, cell_type:CellType):
        self.grid[x][y].update(cell_type)

    def print_grid(self):
        for row in self.grid:
            for cell in row:
                print(cell.cell_type.value, end="")
            print()

    def is_valid_location_for_obstacle(self, x:int, y:int)->bool:
        return 0 <= x < self.dim[0] and 0 <= y < self.dim[1] and self.grid[x][y].cell_type != CellType.OBSTACLE