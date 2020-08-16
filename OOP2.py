#OOP

class primitive_houseBluePrint:
  def __init__(self, walls, roof):
    self.material_walls = walls       #Change to oak for the second house
    self.material_roof = roof       #Change to spruce for the second house
  
  def build_wall(self):
    print(f'Build the walls using {self.material_walls}')
  def build_roof(self):
    print(f'Build the roof using {self.material_roof}')
  
class modern_houseBluePrint(primitive_houseBluePrint):
  def __init__(self, windows, doors, walls, roof):
    self.windows = windows
    self.doors = doors
    super().__init__(walls, roof)
  def build_window(self):
    print(f'Build the windows using {self.material_windows}')
  def build_doors(self):
    print(f'Build the doors using {self.material_doors}')
    
modern_house1 = modern_houseBluePrint('white stained glass', 'oak', 'oak', 'spruce')
modern_house1.build_walls()
modern_house1.build_roof()
modern_house1.build_windows()
modern_house1.build_doors()

print('\n')

modern_house2 = modern_houseBluePrint('blue stained glass', 'birch', 'birch', 'jungle')
modern_house2.build_walls()
modern_house2.build_roof()
modern_house2.build_windows()
modern_house2.build_doors()
  
  
  
  
