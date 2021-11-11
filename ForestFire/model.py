from mesa import Model
from mesa.space import Grid
from mesa.time import RandomActivation

from agent import TreeCell

class ForestFire(Model):
    def __init__(self, height=100, width=100, density=0.6):
        super().__init__()
        self.schedule = RandomActivation(self)
        self.grid = Grid(width, height, torus=False)

        for (contents, x, y) in self.grid.coord_iter():
            if (self.random.random() < density):
                new_tree = TreeCell((x,y), self)

                if (x==0):
                    new_tree.condition = "On Fire"
                
                # self.grid.place_agent(new_tree, (x,y))
                self.grid._place_agent((x,y), new_tree)
                self.schedule.add(new_tree)
        
        self.running=True

    def step(self):
        self.schedule.step()
        count = 0

        for tree in self.schedule.agents:       # Lo mas correcto es primero checar que si sea tipo TreeCell, no simplemente asumir que lo es
            if(tree.condition == "On Fire"):
                count += 1

        if count == 0:
            self.running = False
