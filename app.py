from flask import Flask, render_template, request, url_for

app = Flask(__name__)

tool_types = {
    "TST": {"name": "Taster", "image": "TST.jpg"},
    "BOO": {"name": "Boor", "image": "BOO.jpg"},
    "ALUBOO": {"name": "Alu Boor", "image": "ALUBOO.jpg"},
    "UBOO": {"name": "Volboor", "image": "UBOO.jpg"},
    "PBOO": {"name": "Puntboor", "image": "PBOO.jpg"},
    "RUI": {"name": "Ruimer", "image": "RUI.jpg"},
    "VRZBOO": {"name": "Verzinkboor", "image": "VRZBOO.jpg"},
    "CTBOO": {"name": "Centerboor", "image": "CTBOO.jpg"},
    "NCBOO": {"name": "NC center", "image": "NCBOO.jpg"},
    "DRAFR": {"name": "Draadfrees", "image": "DRAFR.jpg"},
    "DTAP": {"name": "Doorlopende Tap", "image": "DTAP.jpg"},
    "BTAP": {"name": "Blinde Tap", "image": "BTAP.jpg"},
    "RTAP": {"name": "Roltap", "image": "RTAP.jpg"},
    "FRE": {"name": "Universeelfrees", "image": "FRE.jpg"},
    "NAFRE": {"name": "Finishfrees", "image": "NAFRE.jpg"},
    "TRFR": {"name": "Trochoidaalfrees", "image": "TRFR.jpg"},
    "DKFR": {"name": "Duikfrees", "image": "DKFR.jpg"},
    "BLFRE": {"name": "Bolfrees", "image": "BLFRE.jpg"},
    "LPFR": {"name": "Lolipop frees", "image": "LPFR.jpg"},
    "AFB": {"name": "Afbraamfrees", "image": "AFB.jpg"},
    "DAFB": {"name": "Dubbel Afbraamfrees", "image": "DAFB.jpg"},
    "PROFR": {"name": "Profielfrees Specialefrees", "image": "PROFR.jpg"},
    "HOEFR": {"name": "Hoekfrees", "image": "HOEFR.jpg"},
    "ZWAFR": {"name": "Zwaluwstaartfrees", "image": "ZWAFR.jpg"},
    "KWFR": {"name": "Kwartholfrees", "image": "KWFR.jpg"},
    "TFR": {"name": "T-frees", "image": "TFR.jpg"},
    "MTM": {"name": "Multimaster", "image": "MTM.jpg"},
    "KOTK": {"name": "Kotterkop", "image": "KOTK.jpg"},
    "GFR": {"name": "Graveerfrees", "image": "GFR.jpg"},
    "ZAAFR": {"name": "Zaagfrees", "image": "ZAAFR.jpg"},
    "WIS": {"name": "Wisselplaatfrees", "image": "WIS.jpg"},
    "VLAFR": {"name": "Vlakfrees", "image": "VLAFR.jpg"},
    "RPFR": {"name": "RondePlatenFrees", "image": "RPFR.jpg"},
    "KBRST": {"name": "Komborstel", "image": "KBRST.jpg"}
    # Dodaj pozostałe typy narzędzi
}

holder_types = {
    "OP": {"name": "Opsteekfreeshouder", "image": "OP.jpg"},
    "KR": {"name": "Krimphouder 4GR", "image": "KR.jpg"},
    "SKR": {"name": "Slim Krimphouder 3GR", "image": "SKR.jpg"},
    "SP": {"name": "ER-Spantanghouder", "image": "SP.jpg"},
    "CSP": {"name": "ER precisie-Spantanghouder– Centro-P", "image": "CSP.jpg"},
    "MSP": {"name": "ER-Mini-Spantanghouder", "image": "MSP.jpg"},
    "HY": {"name": "Hydrohouder", "image": "HY.jpg"},
    "WE": {"name": "Weldonhouder", "image": "WE.jpg"},
    "KO": {"name": "Kotterkophouder", "image": "KO.jpg"},
    "RAD": {"name": "Reducing adapters", "image": "RAD.jpg"},
    "TAP": {"name": "Taphouder", "image": "TAP.jpg"},
    "FBOO": {"name": "Fitboorhouder", "image": "FBOO.jpg"},
    "MOR": {"name": "Morsehouder", "image": "MOR.jpg"},
    "BTC": {"name": "BT Capto", "image": "BTC.jpg"}
}

materials = {
    "HM": {"name": "(VHM)", "image": "HM.jpg"},
    "HS": {"name": "(HSS)", "image": "HS.jpg"}
}

@app.route('/')
def index():
    return render_template('index.html', tool_types=tool_types, holder_types=holder_types, materials=materials)

@app.route('/generate', methods=['POST'])
def generate_description():
    material = request.form.get('material')
    tool_type = request.form.get('tool_type')
    diameter = request.form.get('diameter')
    teeth = request.form.get('teeth')
    overhang = request.form.get('overhang')
    holder_type = request.form.get('holder_type')
    holder_diameter = request.form.get('holder_diameter')
    holder_length = request.form.get('holder_length')

    description = f"{material}-{tool_type}-DC{diameter}-Z{teeth}-OH{overhang}-{holder_type}{holder_diameter}-LPR{holder_length}"
    selected_holder = holder_types[holder_type]
    return render_template('index.html', description=description, tool_types=tool_types, holder_types=holder_types, materials=materials, selected_holder=selected_holder)

if __name__ == '__main__':
    app.run(debug=True)