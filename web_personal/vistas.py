from web_personal import app


@app.route("/")
@app.route("/home")
@app.route("/inicio")
def inicio():
    return "Soy la pagina de inicio"
