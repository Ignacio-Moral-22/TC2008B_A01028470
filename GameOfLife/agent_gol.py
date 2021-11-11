from mesa import Agent

class GameOfLife(Agent):
    def __init__(self, pos, model):
        super().__init__(pos, model)
        self.pos = pos
        self.condition = "Alive"
        self.next_state = self.condition
    
    def step(self):
        self.next_state = self.condition
        count = 0
        for neighbor in self.model.grid.neighbor_iter(self.pos):
            if(neighbor.condition == "Alive"):
                count += 1
        if(self.condition=="Alive" and (count>=4 or count<2)):
            self.next_state = "Dead"
        elif(self.condition=="Dead" and count==3):
            self.next_state = "Alive"
    
    def advance(self):
        self.condition = self.next_state
