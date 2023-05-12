from flask import Flask, request, render_template

app = Flask(__name__,template_folder='contenidocodigo/html')

@app.route("/")
def redSocials():
    return render_template("start_redessociales.html") 

@app.route("/redsocial", methods=['POST'])
def mostrar_redSocials():
 # Obtener la red social seleccionada por el usuario
 # Insertar el código aquí
 #redSocial del start_redesociales.html
 redSocial_ingresada = request.form['redSocial']
 redSocial = {}
 redSocial['nombre'] = redSocial_ingresada
 redSocial['url'] = request.form['url']
 if redSocial_ingresada == 'facebook':
      redSocial['grupos'] = request.form['grupos']
 elif redSocial_ingresada == 'Twitter':
        redSocial['hashtags'] = request.form['hashtags']
 elif redSocial_ingresada == 'Instagram':
        redSocial['filtros'] = request.form['filtros']
 # Renderizar la página de redes sociales con la red social seleccionada
 return render_template("redsocial.html", redSocial=redSocial_ingresada)


if __name__ == '__main__':
   app.run(debug=True)