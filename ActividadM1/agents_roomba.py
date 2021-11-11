from mesa import Agent

class Roomba(Agent):
    #Start the agent
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        
        # Has a status to simplify code. Allows line 24 in this file to work
        self.status = 'Roomba'
    
    # Function designed to handle movement
    def move(self):
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False)
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)
    
    # Always assume a tile has trash. If it doesn't, it won't return anything and won't do anything
    def clean_agent(self):
        trash = self.model.grid.get_cell_list_contents([self.pos])
        for obj in trash:
            if(obj.status == 'Dirty'):
                obj.status = 'Clean'
                return 1
    
    # Only move if you're not cleaning
    def step(self):
        if(self.clean_agent()!=1):
            self.move()
        else:
            pass

class DirtyTile(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.status = 'Dirty'

    def step(self):
        pass 

