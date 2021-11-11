from mesa import Agent

class TreeCell(Agent):
    def __init__(self, pos, model):     # Inicializacion del Agente
        super().__init__(pos, model)    # Inicializacion del agente padre
        self.pos = pos                  # Posicion del arbol
        self.condition = "Fine"         # Condicion inicial, esta bien
    
    def step(self):
        if(self.condition == "On Fire"):
            for neighbor in self.model.grid.neighbor_iter(self.pos):
                if(neighbor.condition == "Fine"):
                    neighbor.condition = "On Fire"
            self.condition = "Burned Out"
