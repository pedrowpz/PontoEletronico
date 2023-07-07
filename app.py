from flask import Flask, render_template, request, redirect, url_for
import csv
import datetime

app = Flask(__name__)

# Rota para a página inicial
@app.route('/')

def index():
    return render_template('index.html')

# Rota para a página de registro de ponto
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        # Obter dados do formulário
        nome = request.form['nome']
        horario = datetime.datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

        # Registrar o ponto em um arquivo CSV
        with open("registros.csv", 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(nome, horario)
        
        return redirect(url_for('registro'))

    return render_template('registro.html')

# Rota para a página de relatório de pontos
@app.route('/relatorio')
def relatorio():
    registro = []

    # Ler os registros do arquivo CSV
    with open('registros.csv', 'r') as file:
        reader = csv.reader(file)
        registros = list(reader)

    return render_template('relatorio.html', registros=registros)

if __name__ == '__main__':
    app.run(debug=True)