from mesa.visualization.modules import CanvasGrid                   # Visualizar
from mesa.visualization.ModularVisualization import ModularServer   # Launch the Server
from mesa.visualization.UserParam import UserSettableParameter      # Generar Sliders y cosas que permiten modificacion al usuario
from model_gol import GameOfLifeModel

human_colors = {"Alive": "#00bb00", "Dead": "#3F3F3F"}

def gol_portrayal(human): # Definir cada grid
    if human is None:
        return
    
    portrayal = {           # Representacion. Objeto que usa Mesa para darle las propiedades visuales a los diferentes agentes
        "Shape": "rect",    # Figura del agente
        "w": 0.7,           # Anchura
        "h": 0.7,           # Altura
        "Layer": 0,         # Se estan encimando? Si si, el numero mas alto va primero
        "Filled": "True"
    }

    (x, y) = human.pos

    portrayal["x"] = x
    portrayal["y"] = y
    portrayal["Color"] = human_colors[human.condition]
    return portrayal

canvas_element_humans = CanvasGrid(gol_portrayal, 100, 100, 500, 500)

human_model_param = {
    "height": 100,
    "width": 100,
    "density": 0.05
}

server = ModularServer(GameOfLifeModel, [canvas_element_humans], "Game of Life", human_model_param)
server.launch()
