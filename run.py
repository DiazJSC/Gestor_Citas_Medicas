from flask import Flask, request, render_template

# Inicialización de la aplicación Flask
app = Flask(__name__)

# Ruta para la página principal (index)
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para la gestión de citas
@app.route('/citas', methods=["GET", "POST"])
def citas():
    if request.method == "POST":
        # Obtén los datos del formulario
        datos = request.form
        # Lógica para gestionar la cita
        return "Cita gestionada correctamente"
    return render_template('citas.html')

# Ruta para la generación de reportes
@app.route('/reportes', methods=["GET", "POST"])
def reportes():
    if request.method == "POST":
        # Procesar los datos enviados para generar un reporte
        datos = request.form
        return f"Reporte generado con los datos: {datos}"
    # Mostrar el formulario para generación de reportes
    return render_template('reportes.html')

# Punto de entrada de la aplicación
if __name__ == '__main__':
    app.run()
