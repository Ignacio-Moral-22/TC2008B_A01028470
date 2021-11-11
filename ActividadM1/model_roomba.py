from mesa.time import RandomActivation          #Used for activating the agents 1 by 1 as opossed to all at the same time. Avoids multiple Roombas cleaning the same spot
from mesa.space import MultiGrid                #Allows multiple agents in a single Cell
from mesa.datacollection import DataCollector   #Helps generate graphs
from mesa import Model                          #Used for Mesa Models
from agents_roomba import Roomba, DirtyTile     #Import the Agents

class RoombaModel(Model):
    #Roomba and Dirty Tiles Model
    stepCount = 0
    def __init__(self, N, ancho, alto, numObs, turnos):
        
        #Generate the model, given the number of roombas, width, height, % of dirty tiles, and maximum steps
        self.num_agents = N
        self.grid = MultiGrid(ancho, alto, torus = False) 
        self.schedule = RandomActivation(self)
        self.running = True 
        self.steps = 0
        self.turnos = turnos
        
        #DataCollector allows us to create graphs in real time about the status of our model
        self.datacollector = DataCollector(
            {
                "Dirty": lambda m: self.count_type(m, "Dirty"),
                "Clean": lambda m: self.count_type(m, "Clean"),
                "Empty": lambda m: self.count_empty(m)
            }
        )


        #Generate all the trash tiles, using random positions
        #i=0 used for trash ids.
        i=0
        for (contents, x, y) in self.grid.coord_iter():
            if (self.random.random() <= numObs):
                a = DirtyTile(i, self)
                self.schedule.add(a)
                x_pos = self.random.randrange(self.grid.width)
                y_pos = self.random.randrange(self.grid.height)
                while (not self.grid.is_cell_empty((x_pos, y_pos))):
                    x_pos = self.random.randrange(self.grid.width)
                    y_pos = self.random.randrange(self.grid.height)
                self.grid.place_agent(a, (x_pos, y_pos))
            i+=1
        
        #Generate all roombas, starting them in (1, 1)
        for i in range(self.num_agents):
            a = Roomba(i+1000, self)
            self.schedule.add(a)
            x = 1
            y = 1
            self.grid.place_agent(a, (x, y))
        
        self.datacollector.collect(self)

    def step(self):

        #If we get the maximum number of steps, stop the model
        self.steps+=1
        if self.steps == self.turnos:
            self.running = False
        self.schedule.step()

        #Always assume that trash needs to be deleted
        # self.delete_trash(self)
        self.datacollector.collect(self)

        #If there are no dirty tiles, stop the model
        if self.count_type(self, 'Dirty') == 0:
            self.running = False
        
    # #Function to remove the Trash Agent once it's cleaned
    # @staticmethod
    # def delete_trash(model):
    #     for agent in model.schedule.agents:
    #         if agent.status == 'Clean':
    #             model.grid.remove_agent(agent)
    #             model.schedule.remove(agent)
    
    #Function to count all dirty trash tiles.
    #Helps with knowing when to stop the model and generate graphs
    
    @staticmethod
    def count_type(model, status):
        count = 0
        for agent in model.schedule.agents:
            if agent.status == status:
                count += 1
        return count

    @staticmethod
    def count_empty(model):
        count = 0
        for (contents, x, y) in model.grid.coord_iter():
            if(model.grid.is_cell_empty((x,y))):
                count+=1
        return count