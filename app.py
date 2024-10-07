from flask import Flask, render_template, request
from functions import get_translations, data, calc, calcSelectedDrinks

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    # Obtenim l'idioma seleccionat de la petició GET o POST. Per defecte, 'es'.
    language = request.args.get("language", "es")

    if request.method == "POST":
        # Obtenim els altres valors del formulari només en cas de POST
        gender = int(request.form["gender"])
        weight = float(request.form["weight"])
        tam = int(request.form["tam"])
        drink = int(request.form["drink"])

        # Calculem els valors per a l'alcohol ingerit
        k, tma, wh, grad = data(gender, weight, tam, drink)
        hundred = 100
        density = 0.8
        cai = calc(k, tma, wh, hundred, density, grad)

        # Cridem a la funció per calcular el nombre de begudes que es poden beure
        drinks_result = calcSelectedDrinks(cai, grad)

        # Obtenim les traduccions per a l'idioma seleccionat
        translations = get_translations(language)

        # Retornem la plantilla amb el resultat del càlcul i les traduccions
        return render_template("index.html", result=drinks_result, drink=drink, translations=translations, selected_language=language)

    # Si és una petició GET o no s'ha enviat el formulari, obtenim les traduccions
    translations = get_translations(language)
    return render_template("index.html", translations=translations, selected_language=language)

if __name__ == "__main__":
    app.run(debug=True)
