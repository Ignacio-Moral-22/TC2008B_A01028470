from mesa import Model
from mesa.space import Grid
from mesa.time import SimultaneousActivation

from agent_gol import GameOfLife

class GameOfLifeModel(Model):
    def __init__(self, height=100, width=100, density = 0.05):
        super().__init__()
        self.schedule = SimultaneousActivation(self)
        self.grid = Grid(width, height, torus=False)
        
        for (contents, x, y) in self.grid.coord_iter():
            new_human = GameOfLife((x, y), self)
            new_human.condition = "Dead"
            if (self.random.random() < density):
                new_human.condition = "Alive"
                
                # self.grid.place_agent(new_tree, (x,y))
            self.grid._place_agent((x,y), new_human)
            self.schedule.add(new_human)
        
        self.running=True

    def step(self):
        self.schedule.step()
