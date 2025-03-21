from d6_cell_type import CellType

class Cell:
    def __init__(self, x:int, y:int, cell_value:str):
        self.x = x
        self.y = y
        self.cell_type = CellType(cell_value)

    def update(self, cell_type:CellType):
        self.cell_type = cell_type

    @staticmethod
    def factory(x:int, y:int, cell_value:str):
        if cell_value == '\n':
            return None
        elif cell_value == '^':
            return Cell(x=x, y=y, cell_value="X")
        else:
            return Cell(x=x, y=y, cell_value=cell_value)