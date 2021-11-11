from mesa.visualization.modules import CanvasGrid, ChartModule, PieChartModule      # Visualizer and chart creator
from mesa.visualization.ModularVisualization import ModularServer                   # Launch the Server
from mesa.visualization.UserParam import UserSettableParameter                      # Generar Sliders y cosas que permiten modificacion al usuario
from model_roomba import RoombaModel
from agents_roomba import Roomba, DirtyTile

colors = {"Dirty": "brown", "Clean": "white"}
colors_pieChart = {"Dirty": "brown", "Clean": "white", "Empty": "#a2ff00"}
def roomba_portrayal(agent):
    if agent is None:
        return
    
    # All are filled circles
    portrayal = {"Shape": "circle",
                 "Filled": "true"
                }
    
    # Roombas are grey, and go on top of the dirty tiles. Is also a bit smaller for easier visualization
    if (isinstance(agent,Roomba)):
        portrayal["Color"] = "grey"
        portrayal["Layer"] = 1
        portrayal["r"] = 0.5
    
    # Dirt patches are brown. Go below the roombas, and are bigger for easier visualization.
    if (isinstance(agent, DirtyTile)):
        portrayal["Color"] = colors[agent.status]
        portrayal["Layer"] = 0
        portrayal["r"] = 1

    return portrayal

dirty_chart = ChartModule(
    [{"Label": label, "Color": color} for (label, color) in colors.items()]
)

pie_chart = PieChartModule(
    [{"Label": label, "Color": color, "Outline": "black"} for (label, color) in colors_pieChart.items()]
)

roombas = UserSettableParameter("slider", "Numero de Roombas", 10, 1, 25, 5)
ancho =  UserSettableParameter("slider", "Ancho del Grid", 10, 5, 30, 1)
alto = UserSettableParameter("slider", "Alto del Grid", 10, 5, 30, 1)
numObs = UserSettableParameter("slider", "Porcentaje de Area Sucio", 0.1, 0.05, 0.3, 0.05)
turnos = UserSettableParameter("number", "Turnos Maximos", 1000, 1, 2000, 1)
print(ancho.value)

# Parameters of the model. 10 roombas, custom size, % of dirty tiles, and number of turns
roomba_model_param = {
    "N": roombas,
    "ancho": ancho,
    "alto": alto,
    "numObs": numObs,
    "turnos": turnos
}

canvas_element_roomba = CanvasGrid(roomba_portrayal, 31, 31, 500, 500)

server = ModularServer(RoombaModel, [canvas_element_roomba, dirty_chart, pie_chart], "Roomba_Activity", roomba_model_param)
server.launch()