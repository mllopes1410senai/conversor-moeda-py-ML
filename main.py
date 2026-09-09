from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/converter_moeda', methods=['POST'])
def converter_moeda():
    reais = float(request.form['reais'])

    dolares = round((reais * 5.1),2)

    return render_template('index.html', reais=reais, dolares=dolares)

#sempre por último:
if __name__ == '__main__':
    app.run(debug=True) #permite alterações e atualiza a aplicação sem precisar reiniciar