from flask import Flask, request, render_template

from contenidocodigo.clases.facebook import Facebook
from contenidocodigo.clases.instagram import Instagram
from contenidocodigo.clases.twitter import Twitter


app = Flask(__name__,template_folder='contenidocodigo/html')

@app.route("/")
def redSocials():
    return render_template("start_redessociales.html") 

@app.route("/redsocial", methods=['POST'])
def mostrar_redSocials():
     # Obtener la red social seleccionada por el usuario
    redSocial_ingresada = request.form.get("redSocial")
    url_ingresada = request.form.get("url")
    # Instanciar la clase correspondiente a la red social seleccionada
    if redSocial_ingresada == "facebook":
        redSocial = Facebook(nombre="Facebook", url=url_ingresada, usuarios="2.900 millones", grupos=request.form.get("grupos"))
    elif redSocial_ingresada == "Twitter":
        redSocial = Twitter(nombre="Twitter", url=url_ingresada, usuarios="354 millones", hashtags=request.form.get("hashtags"))
    elif redSocial_ingresada == "Instagram":
        redSocial = Instagram(nombre="Instagram", url=url_ingresada, usuarios="1.336 millones", filtros=request.form.get("filtros"))

    # Renderizar la página de redes sociales con la red social seleccionada
    return render_template("redsocial.html", redSocial=redSocial)

if __name__ == '__main__':
   app.run(debug=True)