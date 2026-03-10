from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():
    resultado = None

    if request.method == 'POST':
        a = float(request.form['numero_a'])
        b = float(request.form['numero_b'])
        operacao = request.form['operacao']

        if operacao == 'somar':
            resultado = a + b
        elif operacao == 'subtrair':
            resultado = a - b
        elif operacao == 'multiplicar':
            resultado = a * b
        elif operacao == 'dividir':
            if b == 0:
                resultado = 'Não foi possível dividir por zero!'
            else:
                resultado = a / b

        if isinstance(resultado, float) and resultado.is_integer():
            resultado = int(resultado)


    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)