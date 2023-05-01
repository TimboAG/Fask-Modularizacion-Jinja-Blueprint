from flask import render_template, Blueprint

base = Blueprint('base', __name__)


@base.route("/")
@base.route("/home")
@base.route("/inicio")
def inicio():
    return render_template('inicio.html')


@base.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')


@base.route('/contact')
@base.route('/contacto')
def contacto():
    return render_template('contacto.html')
