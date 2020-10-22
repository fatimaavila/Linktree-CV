from flask import Flask, render_template
import yaml

environment="development"

app = Flask(__name__,static_url_path='/static')
data = yaml.safe_load(open("cv.yml"))
#nombre = "fsa"
#nombre=data['info_personal']['nombre']
links1={
    "Colegio La Asunción": "https://www.asuncion.edu.gt/educacion-personalizada",
    "Universidad Francisco Marroquín": "https://fce.ufm.edu/carrera/cs/"
}

links2={
    "Pinterest": "https://www.pinterest.com/faavila27/_saved/",
    "Instagram": "https://www.instagram.com/fas.atelier/",
    "¡Contáctame!": "mailto:fa.avilasua@gmail.com?Subject=¡Hola,%20desde%20mi%20pagina%20web!"
}


@app.route('/cv')
def show_cv():

    return render_template("template.html", datos = data, 
        idiomas=data['info_personal']['idiomas'], 
        intereses=data['info_personal']['intereses'], 
        tecnologias = data['info_prof']['tecnologias'], 
        referenciaslaborales = data['info_refe']['refe_labo'], 
        referenciaspersonal = data['info_refe']['refe_per'],
        links = links1)

@app.route('/')
def show_home():

    return render_template("linktree.html", linkssocial=links2)

if __name__ == "__main__":
    debug=False
    if environment == "development" or environment == "local":
        debug=True
    print("Local change")
    app.run(host="0.0.0.0")


