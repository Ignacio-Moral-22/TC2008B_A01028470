from mesa.visualization.modules import CanvasGrid                   # Visualizar
from mesa.visualization.ModularVisualization import ModularServer   # Launch the Server
from mesa.visualization.UserParam import UserSettableParameter      # Generar Sliders y cosas que permiten modificacion al usuario
from model import ForestFire

colors = {"Fine": "#00AA00", "On Fire": "#AA0000", "Burned Out": "#3F3F3F"}

def forest_portrayal(tree): # Definir cada grid
    if tree is None:
        return
    
    portrayal = {           # Representacion. Objeto que usa Mesa para darle las propiedades visuales a los diferentes agentes
        "Shape": "rect",    # Figura del agente
        "w": 0.7,           # Anchura
        "h": 0.7,           # Altura
        "Layer": 0,         # Se estan encimando? Si si, el numero mas alto va primero
        "Filled": "True"
    }

    (x, y) = tree.pos

    portrayal["x"] = x
    portrayal["y"] = y
    portrayal["Color"] = colors[tree.condition]
    return portrayal

canvas_element = CanvasGrid(forest_portrayal, 100, 100, 500, 500) # Modelo del portrayal, W y H del grid, W y H del Canvas

model_param = {
    "height": 100,
    "width": 100,
    "density": UserSettableParameter("slider", "Tree Density", 0.6, 0.01, 1.0, 0.1)
    
}

server = ModularServer(ForestFire, [canvas_element], "Forest Fire", model_param)

server = ModularServer(GameOfLifeModel, [canvas_element_humans], "Game of Life", human_model_param)
server.launch()