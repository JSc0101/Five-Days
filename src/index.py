"""
 #!-importancion del framewwork Flask
"""
from flask import Flask, render_template

"""
 !# Inicializo la aplicacion de Flask uso: __name__ , para decirle que es una funcion princiapl
"""
app = Flask(__name__)


"""
!# ya inicilizada la aplicacion creo la primera ruta.
"""
@app.route("/")
def home():
    """
    #! - Atraves de la funcion "render_template" envio un HTML al cliente.
    """
    return render_template("index.html")


"""
#! Valido si la variable que estoy recibiendo es la principal.
"""

"""
 #! : de esta forma podemos crear mas rutas utilizando flash y renderizarlas con la funcion "render_template".
"""
@app.route("/noFound")
def notFound():
    pass
if __name__ == '__main__':
    """
        #! Arranco el servidor
    """
    app.run(debug=True)

print("Genial Has renderizado Un HTML")