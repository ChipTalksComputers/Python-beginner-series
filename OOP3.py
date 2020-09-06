#OOP
#Important: The indentation space I've used here is 2. You'll need to make the changes, if any on your compiler!

#Multi-level inheritance

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
  def build_door(self):
    print(f'Build the doors using {self.material_doors}')
    
class finalHouseBluePrint(modern_houseBluePrint):
  def __init__(self, windows, doors, walls, roof):
    super().__init__(windows, doors, walls, roof)
    
finalHouse = finalHouseBluePrint('white stained glass', 'oak', 'oak', 'spruce')
finalHouse.build_wall()
finalHouse.build_roof()
finalHouse.build_window()
finalHouse.build_door()

#-----------------------------------------------------------------------------------------------------------

#Multiple inheritance

class primitive_houseBluePrint:
  def __init__(self, walls, roof):
    self.material_walls = walls       #Change to oak for the second house
    self.material_roof = roof       #Change to spruce for the second house
  def build_wall(self):
    print(f'Build the walls using {self.material_walls}')
  def build_roof(self):
    print(f'Build the roof using {self.material_roof}')
  
class modern_houseBluePrint:
  def __init__(self, windows, doors):
    self.windows = windows
    self.doors = doors
  def build_window(self):
    print(f'Build the windows using {self.material_windows}')
  def build_door(self):
    print(f'Build the doors using {self.material_doors}')
    
def class finalHouseBluePrint(modern_houseBluePrint, primitive_houseBluePrint):
  def __init__(self, windows, doors, walls, roof):
    modern_houseBluePrint.__init__(self, windows, doors)
    primitive_houseBluePrint.__init__(self, walls, roof)

finnalHouse = finalHouseBluePrint('white stained glass', 'oak', 'oak', 'spruce')
finalHouse.build_wall()
finalHouse.build_roof()
finalHouse.build_window()
finalHouse.build_door()    
    
    
    
    
