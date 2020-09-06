#OOP
#Important: The indentation space I've used here is 2. You'll need to make the changes, if any on your compiler!

class houseBluePrint:
  material_walls = 'birch'       #Change to oak for the second house
  material_roof = 'jungle'       #Change to spruce for the second house
  
  def build_wall(self):
    print(f'Build the walls using {self.material_walls}')
  def build_roof(self):
    print(f'Build the roof using {self.material_roof}')
  
  
 birch_house = houseBluePrint()  #Change based on the house
 birch_house.build_wall()         
 birch_house.build_roof()
    
