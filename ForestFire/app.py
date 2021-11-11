from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = '7110c8ae51a4b5af97be6534caef90e4bb9bdcb3380af008f90b23a5d1616bf319bc298105da20fe'

@app.route("/")
def main_page():
    return "Bienvenido, pero esta pagina no sirve de mucho."

@app.route("/simulation/")
def simulation_page():
    return "Hola"